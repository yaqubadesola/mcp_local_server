import mcp
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather conditions given a location."""
    return "The weather is sunny with a chance of rainbows!"

# 🔥 THIS WAS MISSING
if __name__ == "__main__":
    mcp.run()