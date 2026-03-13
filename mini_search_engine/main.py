import os
import re
from collections import defaultdict

DOC_FOLDER = "documents"


# tokenize words
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())


# build inverted index
def build_index():

    index = defaultdict(set)

    for filename in os.listdir(DOC_FOLDER):

        path = os.path.join(DOC_FOLDER, filename)

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()
            words = tokenize(text)

            for word in words:
                index[word].add(filename)

    return index


def search(index, query):

    words = tokenize(query)

    results = None

    for word in words:

        if word in index:

            if results is None:
                results = index[word]

            else:
                results = results.intersection(index[word])

        else:
            return set()

    return results if results else set()


def main():

    print("Building search index...\n")

    index = build_index()

    while True:

        query = input("Search (type 'exit' to quit): ")

        if query == "exit":
            break

        results = search(index, query)

        if results:
            print("Results found in files:")
            for r in results:
                print("-", r)

        else:
            print("No results found")


if __name__ == "__main__":
    main()
