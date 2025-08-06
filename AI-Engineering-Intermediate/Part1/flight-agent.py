# Builds an AI Agent that helps you plan your flights

from openai import OpenAI
import gradio as gr
import requests
import os

# --- Tool Classes ---

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, location):
        # Stub: Replace with actual weather API call
        # Example: requests.get(f"https://api.weatherapi.com/v1/current.json?key={self.api_key}&q={location}")
        return f"Weather info for {location} (stubbed)"

class SerpFlightsAPI:
    def __init__(self, serp_api_key):
        self.serp_api_key = serp_api_key

    def search_flights(self, origin, destination, date):
        # Stub: Replace with actual SerpAPI call for flights
        return f"Flight info from {origin} to {destination} on {date} (stubbed)"

class SerpHotelsAPI:
    def __init__(self, serp_api_key):
        self.serp_api_key = serp_api_key

    def search_hotels(self, location, checkin, checkout):
        # Stub: Replace with actual SerpAPI call for hotels
        return f"Hotel info in {location} from {checkin} to {checkout} (stubbed)"

# --- Agent Class ---

client= OpenAI()

class TripPlannerAgent:
    def __init__(self, openai_api_key, weather_api_key, serp_api_key):
        client.api_key = openai_api_key
        self.weather = WeatherAPI(weather_api_key)
        self.flights = SerpFlightsAPI(serp_api_key)
        self.hotels = SerpHotelsAPI(serp_api_key)

    def run(self, user_message, chat_history):
        # Simple tool selection logic based on keywords (expand as needed)
        if "weather" in user_message.lower():
            # Extract location (stub)
            location = "London"
            weather_info = self.weather.get_weather(location)
            return weather_info
        elif "flight" in user_message.lower():
            # Extract origin, destination, date (stub)
            origin, destination, date = "NYC", "London", "2024-07-01"
            flight_info = self.flights.search_flights(origin, destination, date)
            return flight_info
        elif "hotel" in user_message.lower():
            # Extract location, checkin, checkout (stub)
            location, checkin, checkout = "London", "2024-07-01", "2024-07-05"
            hotel_info = self.hotels.search_hotels(location, checkin, checkout)
            return hotel_info
        else:
            # Fallback to LLM for general conversation
            response = client.responses.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful travel planning assistant."},
                    *[{"role": "user", "content": m[0]} if i % 2 == 0 else {"role": "assistant", "content": m[1]} for i, m in enumerate(chat_history)],
                    {"role": "user", "content": user_message}
                ]
            )
            return response.choices[0].message.content

# --- Gradio UI ---

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-...")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "weather-api-key")
SERP_API_KEY = os.getenv("SERP_API_KEY", "serp-api-key")

agent = TripPlannerAgent(OPENAI_API_KEY, WEATHER_API_KEY, SERP_API_KEY)

def chat(user_message, history):
    if history is None:
        history = []
    response = agent.run(user_message, history)
    history.append((user_message, response))
    return response, history

with gr.Blocks() as demo:
    gr.Markdown("# ✈️ Flight & Trip Planner Chatbot")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask me about flights, hotels, or weather!")
    state = gr.State([])

    def respond(message, chat_history):
        response, chat_history = chat(message, chat_history)
        return chat_history, chat_history

    msg.submit(respond, [msg, state], [chatbot, state])

if __name__ == "__main__":
    demo.launch()