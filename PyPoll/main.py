import os
import csv
totalvotes = 0




path = os.path.join("Resources", "election_data.csv")
with open (path) as datafile:

    datareader = csv.reader(datafile, delimiter=",")
    header = next(datareader)

    for row in datareader:
        totalvotes = len(row[1])



print(f"Total Votes: {totalvotes}")