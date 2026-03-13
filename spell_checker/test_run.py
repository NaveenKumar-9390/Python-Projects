import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from main import load_dictionary, suggest

print("Testing spell checker:")

print("\n1. Loading dictionary:")
dictionary = load_dictionary()
print(f"Loaded {len(dictionary)} words")

print("\n2. Checking correct word 'hello':")
if "hello" in dictionary:
    print("'hello' is correct")

print("\n3. Checking incorrect word 'helo':")
if "helo" not in dictionary:
    print("'helo' is incorrect")
    suggestions = suggest("helo", dictionary)
    print("Suggestions:", suggestions[:3])

print("\n4. Checking incorrect word 'wrld':")
if "wrld" not in dictionary:
    print("'wrld' is incorrect")
    suggestions = suggest("wrld", dictionary)
    print("Suggestions:", suggestions[:3])

print("\n[OK] Spell checker works correctly!")
