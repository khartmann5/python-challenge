# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

budget_data = os.path.join('Resources','budget_data.csv')

# Set initial variables

# Define lists
total = 0

# read CSV file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    #read header row
    csv_header = next(csvreader)

    # Count number of months
    months = len(list(csvreader))
    print(f"Total Months: {months}")   
    
    # # Read each row of data
    for row in csvreader:
        
    # Sum the net total amount of "Profit/Losses" over the period
        total += int(row[1])
        print(f"Total: ${total}")

       



        
