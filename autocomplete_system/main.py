from autocomplete import Autocomplete, load_words


def main():
    import sys

    ac = Autocomplete()

    # load words from a file if provided on the command line
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip()
                    if word:
                        ac.insert(word)
            print(f"Loaded words from {filepath}")
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return
    else:
        # Example word list
        words = ["apple", "app", "application", "banana", "band", "bandana"]
        for w in words:
            ac.insert(w)

    print("Type any prefix and press Enter to see suggestions. Type 'exit' to quit.")
    while True:
        prefix = input("Prefix: ")
        if prefix.lower() == "exit":
            break
        suggestions = ac.suggest(prefix)
        print("Suggestions:", suggestions)


if __name__ == "__main__":
    main()
