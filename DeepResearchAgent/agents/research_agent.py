from langchain.tools.tavily_search import TavilySearchResults

def fetch_research_data(query):
    tool = TavilySearchResults()
    response = tool.invoke(query)
    combined_text = "\n\n".join([r['content'] for r in response])
    return combined_text
