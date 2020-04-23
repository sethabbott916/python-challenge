import os
import csv

budgetpath = os.path.join("Resources", "budget_data.csv")

with open (budgetpath) as bankfile:

    csvreader = csv.reader(bankfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)