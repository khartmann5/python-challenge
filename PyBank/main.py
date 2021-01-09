# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

budget_data = os.path.join('Resources','budget_data.csv')

# Lists to store data
profit_loss_changes = []
total_amount = []
total_months = []

# Read CSV file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read header row
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data
    for row in csvreader:
        
        # Append the net total amount of "Profit/Losses" over the period
        total_amount.append(int(row[1]))

        # keep track of number of months for variable to iterate
        total_months.append(row[1])

        # Calculate change between months    

# Sum total of net profit losses    
total_amount_sum = sum(total_amount)
# print(total_amount_sum)

 # Count number of months
total_months = len(total_months)
# print(total_months)

# Calculate the average change
# use mean function?    

# Calculate the greatest increase in profits
# use max function?

# Calculate the greatest decrease in profits
# use min function

# Find the month of the greatest increase
# index to find the month?

# Find the month of the greatest decrease

# Print findings   


        

        
      
# write to text analysis file
# pybank_financial_analysis = os.path.join("pybank_financial_analysis.txt")
# with open(pybank_financial_analysis,"w") as outfile:
    
#     outfile.write("Financial Analysis\n")
#     outfile.write("---------------------------\n")
#     outfile.write(f"Total Months: {months}")