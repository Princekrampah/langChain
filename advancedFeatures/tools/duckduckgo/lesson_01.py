# pip install duckduckgo-search
from langchain.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

print(search.run("What it the capital of Kenya"))