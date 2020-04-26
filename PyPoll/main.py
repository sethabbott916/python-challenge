import os
import csv
totalvotes = 0
Khantick = 0
Tooleytick = 0
Correytick = 0
Litick = 0

Khancent = 0
Tooleycent = 0
Correycent = 0
Licent = 0
    


path = os.path.join("Resources", "election_data.csv")
with open (path) as datafile:

    datareader = csv.reader(datafile, delimiter=",")
    header = next(datareader)

    candidates = []

    for row in datareader:
        totalvotes = totalvotes + 1

        
        if row[2] not in candidates:
            candidates.append(row[2])



        if row[2] == "Khan":
            Khantick = Khantick + 1
        
        if row[2] == "Correy":
            Correytick = Correytick + 1
        
        if row[2] == "Li":
            Litick = Litick + 1
        
        if row[2] == "O'Tooley":
            Tooleytick = Tooleytick + 1
 
if Khantick > Tooleytick and Khantick > Correytick and Khantick > Litick:
    Winner = "Khan"
if Tooleytick > Khantick and Tooleytick > Correytick and Tooleytick > Litick:
    Winner = "O'Tooley"
if Correytick > Tooleytick and Correytick > Khantick and Correytick > Litick:
    Winner = "Correy"
if Litick > Tooleytick and Litick > Correytick and Litick > Khantick:
    Winner = "Li"


Khancent = (Khantick / totalvotes)
Tooleycent = (Tooleytick / totalvotes)
Correycent = (Correytick / totalvotes)
Licent = (Litick / totalvotes)


#Could not get the decimal place to change to 1000th place
Khancent = "{:.3%}".format(Khancent)
Tooleycent = "{:.3%}".format(Tooleycent)
Correycent = "{:.3%}".format(Correycent)
Licent = "{:.3%}".format(Licent)



print(f"Election Results")
print(f"-------------------")
print(f"Total Votes: {totalvotes}")
print(f"-------------------")
print(f"Khan: {Khancent} ({Khantick})")
print(f"Correy: {Correycent} ({Correytick})")
print(f"Li: {Licent} ({Litick})")
print(f"O'Tooley: {Tooleycent} ({Tooleytick})")
print(f"-------------------")
print(f"Winner: {Winner}")

output_path = os.path.join("Analysis", "Results.txt")
with open (output_path, "a") as f:
    print(f"Election Results", file=f)
    print(f"-------------------", file=f)
    print(f"Total Votes: {totalvotes}", file=f)
    print(f"-------------------", file=f)
    print(f"Khan: {Khancent}% ({Khantick})", file=f)
    print(f"Correy: {Correycent}% ({Correytick})", file=f)
    print(f"Li: {Licent}% ({Litick})", file=f)
    print(f"O'Tooley: {Tooleycent}% ({Tooleytick})", file=f)
    print(f"-------------------", file=f)
    print(f"Winner: {Winner}", file=f)