from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("local-server")

NOTES_FILE = Path(__file__).parent / "notes.txt"

@mcp.tool()
def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    Args:
        content: The text content to append.
    """

    try:
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Content appended to {NOTES_FILE}."
    except Exception as e:
        return f"Error appending to file {NOTES_FILE}: {e}"


@mcp.tool()
def read_notes() -> str:
    """
    Reads and returns the contents of the user's local notes.
    """
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.read()
        return notes if notes else "No notes found."
    except FileNotFoundError:
        return "No notes file found."
    except Exception as e:
        return f"Error reading file {NOTES_FILE}: {e}"


if __name__ == "__main__":
    mcp.run()