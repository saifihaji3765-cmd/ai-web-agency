import requests
from bs4 import BeautifulSoup

def find_clients(query):
    print("Searching for businesses...")

    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []

    for g in soup.select("a"):
        href = g.get("href")

        if href and "http" in href:
            links.append(href)

    return links


if __name__ == "__main__":
    results = find_clients("local businesses without website")

    for r in results[:10]:
        print(r)
