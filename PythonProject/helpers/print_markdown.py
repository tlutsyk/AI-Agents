from rich.console import Console
from rich.markdown import Markdown

console = Console()
def print_markdown(text: str):
    md = Markdown(text)
    console.print(md)