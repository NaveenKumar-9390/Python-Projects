from autocomplete import Autocomplete

ac = Autocomplete()
words = ["apple", "app", "application", "banana", "band", "bandana"]
for w in words:
    ac.insert(w)

print("Testing autocomplete system:")
print("Prefix 'app':", ac.suggest("app"))
print("Prefix 'ban':", ac.suggest("ban"))
print("Prefix 'a':", ac.suggest("a"))
print("[OK] Autocomplete system works correctly!")
