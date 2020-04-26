import os
import csv
totalmonths = 0
totalprofits = 0
totalchange = 0
currentprofit = 867884
change = 0
averagechange = 0
increase = "0"
increasedate = "blank"
decrease = "0"
decreasedate = "blank"

#Talked to instructor in class about this problem. Tried his solution and it broke my code
#I'm turning it in with the broken part of the code as pseudocode
#FirstLoop = True


budgetpath = os.path.join("Resources", "budget_data.csv")

profits = []

with open (budgetpath) as bankfile:



    datareader = csv.reader(bankfile, delimiter=',')
    

    
    header = next(datareader)

 


    for row in datareader:

        #if FirstLoop is True:
           #currentprofit = int(row[1])
            #FirstLoop is False
            
        totalmonths = totalmonths + 1
        profits = int(row[1])
        date = str(row[0])
        totalprofits = totalprofits + profits
        change = profits - currentprofit
        

        if float(increase) > change:
            increase = change
            increasedate = date

        if float(decrease) < change:
            decrease = change
            decreasedate = date


        totalchange = totalchange + change
        currentprofit = profits
        
        
    averagechange = totalchange / (totalmonths - 1)
    Greatcurrency = "${:,.2f}".format(float(increase))
    Lowcurrency = "${:,.2f}".format(float(decrease))
    Totalcurrency = "${:,.2f}".format(totalprofits)
    Averagecurrency = "${:,.2f}".format(averagechange)


print("Financial Analysis")
print("------------------")
print(f"Total Months: {totalmonths}")
print(f"Total Profits/Losses: ({Totalcurrency})")
print(f"Average Change: ({Averagecurrency})")
print(f"Greatest Increase in Profits: {decreasedate} ({Lowcurrency})")
print(f"Greatest Decrease in Profits: {increasedate} ({Greatcurrency})")

output_path = os.path.join("Analysis", "Results.txt")
with open(output_path, "a") as f:
    print("Financial Analysis", file=f)
    print("------------------", file=f)
    print(f"Total Months: {totalmonths}", file=f)
    print(f"Total Profits/Losses: ({Totalcurrency})", file=f)
    print(f"Average Change: ({Averagecurrency})", file=f)
    print(f"Greatest Increase in Profits: {decreasedate} ({Lowcurrency})", file=f)
    print(f"Greatest Decrease in Profits: {increasedate} ({Greatcurrency})", file=f)