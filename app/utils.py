import wikipediaapi
import requests

# Wikipedia API setup with a User-Agent
wiki_api = wikipediaapi.Wikipedia(
    language='en',
    user_agent='AI_Agent_Project/1.0 (contact: your_email_@gmail.com)'
)

def search_wikipedia(query):
    """Search for a topic on Wikipedia."""
    page = wiki_api.page(query)
    if page.exists():
        return page.summary[:1000]  # Limit the length of the summary
    return "I couldn't find anything on Wikipedia."

def fetch_real_time_data(query):
    """Fetch real-time data from DuckDuckGo API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('AbstractText', "I couldn't fetch data at the moment.")
    return "Error fetching real-time data."
