import os
import csv
totalmonths = 0
totalprofits = 0
currentprofit = 0
totalchange = 0
change = 0
averagechange = 0
increase = 0
increasedate = "blank"
decrease = 0
decreasedate = "blank"


budgetpath = os.path.join("Resources", "budget_data.csv")

profits = []

with open (budgetpath) as bankfile:



    datareader = csv.reader(bankfile, delimiter=',')
    

    
    header = next(datareader)

    for row in datareader:
    
        totalmonths = totalmonths + 1
        profits = int(row[1])
        date = str(row[0])
        totalprofits = totalprofits + profits

        

        change = profits - currentprofit
        currentprofit = profits

        if change > increase:
            increase = change
            increasedate = date

        if change < decrease:
            decrease = change
            decreasedate = date


        totalchange = totalchange + change
        
        
    

averagechange = totalchange / totalmonths
print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalmonths}")
print(f"Total Profits/Losses: {totalprofits}")
print(f"Average Change: {averagechange}")
print(f"Greatest Increase in Profits: {increasedate} {increase}")
print(f"Greatest Decrease in Profits: {decreasedate} {decrease}")


