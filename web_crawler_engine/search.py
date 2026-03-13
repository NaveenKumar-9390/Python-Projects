import json

with open("data.json", "r", encoding="utf-8") as f:
    pages = json.load(f)

query = input("Enter search keyword: ").lower()

print("\nSearch Results:\n")

found = False
for page in pages:
    if query in page["title"].lower() or query in page["content"].lower():
        print("Title:", page["title"])
        print("URL:", page["url"])
        print("-" * 40)
        found = True

if not found:
    print("No results found.")