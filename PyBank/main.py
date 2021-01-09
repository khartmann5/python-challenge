# Add Header
print("Financial Analysis\n-----------------------")

# Import the os module
import os

# Module for reading CSV files
import csv

budget_data = os.path.join('Resources','budget_data.csv')

# Lists to store data
profit_loss_changes = []
total_amount= []

# Read CSV file
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read header row
    csv_header = next(csvreader)

    # Count number of months
    months = len(list(csvreader))
    print(f"Total Months: {months}") 

    # Read each row of data
    for row in csvreader:
        
        # Append the net total amount of "Profit/Losses" over the period
        total_amount.append(int(row[1]))

        # Calculate change between months    

# Sum total of net profit losses    
total_amount = sum(total_amount)
print(total_amount)

# Calculate the average change    

# Calculate the greatest increase in profits

# Calculate the greatest decrease in profits

# Find the month of the greatest increase

# Find the month of the greatest decrease

    


        

        
      
# write to text analysis file
# pybank_financial_analysis = os.path.join("pybank_financial_analysis.txt")
# with open(pybank_financial_analysis,"w") as outfile:
    
#     outfile.write("Financial Analysis\n")
#     outfile.write("---------------------------\n")
#     outfile.write(f"Total Months: {months}")


       



        
