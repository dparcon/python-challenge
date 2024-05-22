import os, csv
from pathlib import Path 

#Set the path to access budget_data.csv
budget_data_path = Path("PyBank/Resources/budget_data.csv")


# Initialize variables to store financial data
total_months = 0
net_total = 0
previous_profit_change = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
profit_changes = []

#Read budget_data.csv for analysis
with open(budget_data_path, newline="", encoding="utf-8") as file:
    csvreader = csv.reader(file, delimiter=",")
    
    # Skip the header row
    next(csvreader) 
    budget_data = list(csvreader)

# Loop through each row in the CSV file
for row in budget_data:
    total_months += 1
    net_total += int(row[1])
    
    #Calculate and record changes in profit and loss
    if previous_profit_change != 0:
        change = int(row[1]) - previous_profit_change
        profit_changes.append(change)
        
        #Track greatest increase and date
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]
        
        #Track greatest decrease and date
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]
    
    #Set new previous change for consideration        
    previous_profit_change = int(row[1])

#Calculate average change
average_change = round((sum(profit_changes) / len(profit_changes)), 2)

#Print financial analysis of budget_data.csv
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Write path for new text file
output_file = Path("PyBank", "analysis", "pybank_analysis.txt")

#Write analysis to text file
with open(output_file, "w") as file:   
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {total_months}")
    file.write("\n")
    file.write(f"Total: ${net_total}")
    file.write("\n")
    file.write(f"Average Change: ${average_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")