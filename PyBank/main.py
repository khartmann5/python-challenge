# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

budget_data = os.path.join('Resources','budget_data.csv')

# Define variables
net_profit_loss = 0
current_profit_loss = 0
previous_profit_loss = 0

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
      
# write to text analysis file
# pybank_financial_analysis = os.path.join("pybank_financial_analysis.txt")
# with open(pybank_financial_analysis,"w") as outfile:
    
#     outfile.write("Financial Analysis\n")
#     outfile.write("---------------------------\n")
#     outfile.write(f"Total Months: {months}")


       



        
