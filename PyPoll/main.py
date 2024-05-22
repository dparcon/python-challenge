import os, csv
from pathlib import Path 

#Set the path to access election_data.csv
election_data_path = Path("PyPoll/Resources/election_data.csv")

# Initialize variables to store financial data
total_votes = 0
Stockham_total = 0
DeGette_total = 0
Doane_total = 0
Stockham_percent = 0
DeGette_percent = 0
Doane_percent = 0
winner = 0
candidates = []

#Read election_data.csv for analysis
with open(election_data_path, newline="", encoding="utf-8") as file:
    csvreader = csv.reader(file, delimiter=",")
    # Skip the header row
    next(csvreader) 
    election_data = list(csvreader)

# Loop through each row in the CSV file addin oneg vote to each candidates total when they receive a vote    
for row in election_data:
    total_votes += 1
    if row[2] == "Charles Casper Stockham":
        Stockham_total += 1
    if row[2] == "Diana DeGette":
        DeGette_total += 1
    if row[2] == "Raymon Anthony Doane":
        Doane_total += 1

#Calculate percentages of each candidates total votes
Stockham_percent = round((Stockham_total / total_votes)*100,3)
DeGette_percent = round((DeGette_total / total_votes)*100, 3)
Doane_percent = round((Doane_total / total_votes)*100, 3)

#Determine the winner of the election by comparing vote totals
if Stockham_total > DeGette_total and Stockham_total > Doane_total:
    winner = "Charles Casper Stockham"
if DeGette_total > Stockham_total and DeGette_total > Doane_total:
    winner = "Diana DeGette"
if Doane_total > Stockham_total  and Doane_total > DeGette_total:
    winner = "Raymon Anthony Doane"

#Print financial analysis of election_data.csv  
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_total})")
print(f"Diana DeGette: {DeGette_percent}% ({DeGette_total})")
print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_total})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Write path for new text file
output_file = Path("PyPoll", "analysis", "pypoll_analysis.txt")

#Write analysis to text file
with open(output_file, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_total})")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGette_percent}% ({DeGette_total})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_total})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")