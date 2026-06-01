from mcp.server.fastmcp import FastMCP
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

mcp = FastMCP("Web Search")

@mcp.tool()
def perform_websearch(query: str) -> str:
    """
    Performs a web search for a query
    Args:
        query: the query to web search.
    """

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that searches the web and responds to questions"
            ),
        },
        {   
            "role": "user",
            "content": (
                query
            ),
        },
    ]

    # client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")
    #Geting Openrouter API Key
    key = (os.getenv("OPENROUTER_API_KEY") or "").strip()   
    if not key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Add it to a .env file in the project root."
        )
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key,
    )
    # chat completion without streaming
    response = client.chat.completions.create(
        model="perplexity/sonar",
        messages=messages,
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run()