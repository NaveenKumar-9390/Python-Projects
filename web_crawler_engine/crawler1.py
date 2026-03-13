import requests
from bs4 import BeautifulSoup
import json
import urllib3

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawl(url):
    print("Crawling:", url)

    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "title": soup.title.string if soup.title else "No title",
        "links": []
    }

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            data["links"].append(href)

    # Save data to file
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Crawling finished. Data saved in output.json")

if __name__ == "__main__":
    url = input("Enter website URL (example: https://example.com): ")
    crawl(url)