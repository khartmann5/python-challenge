# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

# Module for statistics
from statistics import mean

budget_data = os.path.join('Resources','budget_data.csv')

# Lists to store data
total_amount = []
total_months = []
max_month = ['',-9999999]
min_month = ['',9999999]
change_list = []

# Variables for data
previous_month = 0
current_change = 0
count = 0

# Read CSV file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read header row
    csv_header = next(csvreader)

    # Read each row of data
    for row in csvreader:
        
        # Create a count variable
        count += 1

        # Append the net total amount of "Profit/Losses" over the period
        total_amount.append(int(row[1]))

        # Keep track of number of months for variable to iterate
        total_months.append(row[0])

        # Calculate current change
        current_change = int(row[1]) - previous_month
        
        # Find the greatest increase and decrease of change between months
        if current_change > max_month[1]:
            max_month[0] = row[0]
            max_month[1] = current_change
        
        if current_change < min_month[1]:
            min_month[0] = row[0]
            min_month[1] = current_change

        # Start change list on the 3rd row for correct calculation
        if count > 1:
            change_list.append(current_change)

        # Storing previous month
        previous_month = int(row[1])

# Sum total of net profit losses    
total_amount_sum = sum(total_amount)

 # Count number of months
total_months = len(total_months)

# Calculate the average change
average_change = round(mean(change_list),2)    

# Print findings   
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount_sum}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month[0]} (${max_month[1]})")
print(f"Greatest Decrease in Profits: {min_month[0]} (${min_month[1]})")
    
# Write to text analysis file
pybank_financial_analysis = os.path.join("pybank_financial_analysis.txt")
with open(pybank_financial_analysis,"w") as outfile:
    
    outfile.write("Financial Analysis\n")
    outfile.write("---------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_amount_sum}\n")
    outfile.write(f"Average Change: ${average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {max_month[0]} (${max_month[1]})\n")
    outfile.write(f"Greatest Decrease in Profits: {min_month[0]} (${min_month[1]})")