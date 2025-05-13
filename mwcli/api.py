import requests
from mwcli.config import MW_API_KEY

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json"

def fetch_definitions(word):
    if not MW_API_KEY:
        raise ValueError("MW_API_KEY not set.")
    url = f"{BASE_URL}/{word}?key={MW_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

