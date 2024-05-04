# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        _ = next(rows)
        total = 0
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print("Missing data")
        return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print("Total cost:", cost)
