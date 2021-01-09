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
profit_loss_change = 0

# Lists to store data
profit_loss_changes = []
current_profit_losses = []
net_profit_losses = []

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
        net_profit_losses.append(int(row[1]))

        # Determine current profit loss
        # current_profit_loss = net_profit_loss

        # # Calculate previous months profit loss
        # previous_profit_loss = current_profit_loss(row[1]-1)

# Sum total of net profit losses
net_profit_losses = sum(net_profit_losses)

print(net_profit_losses)

    

    


        

        
      
# write to text analysis file
# pybank_financial_analysis = os.path.join("pybank_financial_analysis.txt")
# with open(pybank_financial_analysis,"w") as outfile:
    
#     outfile.write("Financial Analysis\n")
#     outfile.write("---------------------------\n")
#     outfile.write(f"Total Months: {months}")


       



        
