from langchain_core.tools import tool
import arxiv
import requests
@tool
def search_arxiv(query: str) -> str:
    """Search aerospace research papers from arXiv."""
    client = arxiv.Client()                          
    search = arxiv.Search(query=query, max_results=3)
    papers = []
    for result in client.results(search):          
        papers.append(f"Title: {result.title}\nSummary: {result.summary}\n")
    return "\n\n".join(papers)

@tool
def get_nasa_data(query: str) -> str:
    """Retrieve NASA technical information."""
    
    url = f"https://images-api.nasa.gov/search?q={query}"
    response = requests.get(url)

    if response.status_code != 200:
        return "NASA API ERROR"

    data = response.json()
    items = data["collection"]["items"][:3]

    if not items:
        return "No NASA results found."

    results = []

    for item in items:
        title = item["data"][0]["title"]
        description = item["data"][0].get("description", "")
        results.append(f"{title}\n{description}")

    return "\n\n".join(results)
@tool
def rocket_exhaust_velocity(Isp: float) -> str:
    """Calculate rocket exhaust velocity using specific impulse."""

    g=9.81
    ve = Isp * g
    return f"Exhaust velocity is approximately {ve} m/s"



     


