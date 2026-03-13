import requests
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

visited = set()
pages = []

def crawl(url, depth):
    if depth == 0 or url in visited:
        return

    print("Crawling:", url)
    visited.add(url)

    try:
        response = requests.get(url, verify=False, timeout=5)
    except:
        print("Failed:", url)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title"
    text = soup.get_text()

    pages.append({
        "url": url,
        "title": title,
        "content": text[:500]  # save first 500 chars
    })

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            crawl(href, depth - 1)


if __name__ == "__main__":
    start_url = input("Enter starting URL: ")
    depth = int(input("Enter depth (example 2): "))

    crawl(start_url, depth)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, indent=4)

    print("Crawling done. Data saved in data.json")