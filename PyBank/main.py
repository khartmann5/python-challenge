# Import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)