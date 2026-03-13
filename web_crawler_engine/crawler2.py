import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

visited = set()

def crawl(url, depth):
    if depth == 0 or url in visited:
        return

    print("Crawling:", url)
    visited.add(url)

    try:
        response = requests.get(url, verify=False, timeout=5)
    except:
        print("Failed to crawl:", url)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title"
    print("Title:", title)

    for link in soup.find_all("a"):
        href = link.get("href")

        if href and href.startswith("http"):
            crawl(href, depth - 1)


if __name__ == "__main__":
    start_url = input("Enter starting URL: ")
    depth = int(input("Enter depth (example 2): "))
    crawl(start_url, depth)
    print("Finished crawling.")