
import os
import logging
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

tavily_key = os.getenv("TAVILY_APY_KEY")

def search_web(query: str) -> str:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    
    Args:
        query: The search query to look up
        
    Returns:
        str: The search results as a string
    """
    tavily_tool = TavilySearch(
        api_key=tavily_key,  # Need to pass the API key
        max_results=10
    )
    
    # Perform the search and return results
    results = tavily_tool.invoke(query)
    return str(results)