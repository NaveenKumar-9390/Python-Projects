import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "prices.csv")

prices = []

with open(CSV_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        prices.append(float(row["price"]))


def average_price():
    return sum(prices) / len(prices)


def max_price():
    return max(prices)


def min_price():
    return min(prices)


def best_profit():
    min_price = prices[0]
    max_profit = 0

    for p in prices:
        if p < min_price:
            min_price = p

        profit = p - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


print("Average Price:", average_price())
print("Highest Price:", max_price())
print("Lowest Price:", min_price())
print("Best Profit:", best_profit())
