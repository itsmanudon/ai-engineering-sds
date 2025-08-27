import os
from tavily import TavilyClient
from dotenv import load_dotenv
import json
from openai import OpenAI
from utils import function_to_tool
from IPython.display import display, Markdown
import gradio as gr

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not set in the environment variables.")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

tavily_client = TavilyClient()
openai_client = OpenAI()



# All Functions
def flight_search(query: str) -> list:
    """
    Search for flights using the Tavily API.

    Args:
        query (str): The user's flight search query.

    Returns:
        list: The search results from the flight API.
    """
    
    response = tavily_client.search(
        query=query,
        include_domains=['skyscanner.com', 'expedia.com', 'booking.com']
    )

    results = []

    for result in response["results"]:
        results.append(result["content"])

    return results

def hotel_search(query: str) -> list:
    """
    Search for hotels using the Tavily API.

    Args:
        query (str): The user's hotel search query.

    Returns:
        list: The search results from the hotel API.
    """
    response = tavily_client.search(
        query=query,
        include_domains=['booking.com', 'airbnb.com', 'hotels.com']
    )

    results = []

    for result in response["results"]:
        results.append(result["content"])

    return results

def call_function(name, args):
    if name == "flight_search":
        return flight_search(**args)
    if name == "hotel_search":
        return hotel_search(**args)
    

def get_response(input_list, tools):
    response = openai_client.responses.create(
        model="gpt-4o-mini",
        input=input_list,
        tools=tools,
        tool_choice="auto",
        parallel_tool_calls=False
    )
    return response


def clean_history(history):
    return [
        {"role": msg["role"], "content": msg["content"]}
        for msg in history
        if "role" in msg and "content" in msg
    ]


flight_tool_schema = function_to_tool(flight_search)
hotel_tool_schema = function_to_tool(hotel_search)
tools = [flight_tool_schema, hotel_tool_schema]



# LLM Logic

system_message = """

You are a helpful travel planner and your are to assist the user in planning their travel itinerary.

You are to ask the user in a conversational manner about their travel plans and preferences, first start with their
destination, wait for their response and then ask about the dates they plan to travel, and then search for the best flights available,
build an itinerary based on their preferences and give them a summary of their travel plans.


Eg.
- Hello, I am your travel planner. Which country would you like to travel to?
- I want to travel to Japan
- What is your preferred destination in Japan?
- Tokyo
- Great! When do you plan to travel?
- I plan to travel tomorrow.

* use your search tool to search for flight deals *
* Wait until you are provided with flight options *
* use your search tool to search for hotel booking deals *
* Wait until you are provided the results of the hotel search *
* summarize results in a neatly formatted itinerary. *
* provide the itinerary to the user *

- Here is your travel itinerary for Japan:

Remember to only provide the user with the results once you have information about the flights as well as the hotels.
"""


def chat(message, history):

    history = clean_history(history)

    input_list = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    # print(input_list)
    response = get_response(input_list, tools)

    if response.output[0].type == "function_call":
        while response.output[0].type == "function_call":
            input_list += response.output

            name = response.output[0].name
            args = json.loads(response.output[0].arguments)

            results = call_function(name, args)

            input_list.append({
                "type": "function_call_output",
                "call_id": response.output[0].call_id,
                "output": str(results)
            })

            response = get_response(input_list, tools)

    return response.output_text

view = gr.ChatInterface(fn=chat, type="messages").launch()