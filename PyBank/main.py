import os
import csv
totalmonths = 0
budgetpath = os.path.join("Resources", "budget_data.csv")

with open (budgetpath) as bankfile:

    datareader = csv.reader(bankfile, delimiter=',')
    print(datareader)
    
    for row in datareader:
        print(row)
    
        totalmonths = totalmonths + 1
        print(f"Total Months: {totalmonths}")
