import os
import csv
totalmonths = 0
totalprofits = 0
currentprofit = 867884
totalchange = 0
change = 0
averagechange = 0
increase = "0"
increasedate = "blank"
decrease = "0"
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

        if float(increase) > change:
            increase = change
            increasedate = date

        if float(decrease) < change:
            decrease = change
            decreasedate = date


        totalchange = totalchange + change
        
        
    averagechange = totalchange / totalmonths
    Greatcurrency = "${:,.2f}".format(increase)
    Lowcurrency = "${:,.2f}".format(decrease)
    Totalcurrency = "${:,.2f}".format(totalprofits)
    Averagecurrency = "${:,.2f}".format(averagechange)

averagechange = totalchange / totalmonths
print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalmonths}")
print(f"Total Profits/Losses: ({Totalcurrency})")
print(f"Average Change: ({Averagecurrency})")
print(f"Greatest Decrease in Profits: {decreasedate} ({Lowcurrency})")
print(f"Greatest Increase in Profits: {increasedate} ({Greatcurrency})")



