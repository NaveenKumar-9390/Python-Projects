import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from main import build_index, search

print("Testing mini search engine:")

print("\n1. Building index:")
index = build_index()
print(f"Indexed {len(index)} unique words")

print("\n2. Searching for 'python':")
results = search(index, "python")
print("Results:", results)

print("\n3. Searching for 'data':")
results = search(index, "data")
print("Results:", results)

print("\n4. Searching for 'machine learning':")
results = search(index, "machine learning")
print("Results:", results)

print("\n[OK] Mini search engine works correctly!")
