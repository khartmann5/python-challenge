# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# Define total
total = 0

# read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read header row
    csv_header = next(csvreader)
    
    # Read each row of data
    for row in csvreader:
        
        # Count number of months
        months = len(list(csvreader))+1
        print(f"Total Months: {months}")     

        # Sum the net total amount of "Profit/Losses" over the period and define total
        total += float(row[1])
        print(f"Total: ${total}")