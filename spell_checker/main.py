def load_dictionary():

    words = set()
    
    import os
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    DICT_FILE = os.path.join(SCRIPT_DIR, "dictionary.txt")

    with open(DICT_FILE,"r") as f:

        for line in f:
            words.add(line.strip().lower())

    return words


# calculate edit distance
def edit_distance(a,b):

    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

    for i in range(len(a)+1):
        dp[i][0] = i

    for j in range(len(b)+1):
        dp[0][j] = j

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):

            cost = 0 if a[i-1] == b[j-1] else 1

            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + cost
            )

    return dp[len(a)][len(b)]


def suggest(word,dictionary):

    suggestions = []

    for w in dictionary:

        if edit_distance(word,w) <= 2:
            suggestions.append(w)

    return suggestions[:5]


def main():

    dictionary = load_dictionary()

    while True:

        word = input("\nEnter word (or exit): ").lower()

        if word == "exit":
            break

        if word in dictionary:
            print("Correct spelling")

        else:
            print("Incorrect spelling")

            suggestions = suggest(word,dictionary)

            if suggestions:
                print("Did you mean:")
                for s in suggestions:
                    print("-",s)

            else:
                print("No suggestions found")


if __name__ == "__main__":
    main()
