from collections import Counter
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "access.log")


def analyze_logs():

    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    with open(LOG_FILE, "r") as f:

        for line in f:

            parts = line.split()

            if len(parts) != 4:
                continue

            ip, method, url, status = parts

            ip_counter[ip] += 1
            url_counter[url] += 1
            status_counter[status] += 1

    return ip_counter, url_counter, status_counter


def main():

    ip_counter, url_counter, status_counter = analyze_logs()

    print("\nTop IP Addresses")
    for ip, count in ip_counter.most_common():
        print(ip, "->", count, "requests")

    print("\nMost Accessed URLs")
    for url, count in url_counter.most_common():
        print(url, "->", count)

    print("\nStatus Code Counts")
    for status, count in status_counter.items():
        print(status, "->", count)


if __name__ == "__main__":
    main()
