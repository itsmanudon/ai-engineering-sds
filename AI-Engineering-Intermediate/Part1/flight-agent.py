import os
from tavily import TavilyClient
from dotenv import load_dotenv


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not set in the environment variables.")

query = "I want to travel to tokyo and osaka tomorrow what are the best flights available"

client = TavilyClient()
response = client.search(
    query=query
)

print("Search Results: \n", response)