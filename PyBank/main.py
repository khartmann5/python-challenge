# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data
    for row in csvreader:
        
        # Count number of months
        months = len(list(csvreader))
        print(f"Total Months: {months}")        