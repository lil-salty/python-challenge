# -*- coding: UTF-8 -*-


# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
total_change = 0
average_change=0
previous_profit = 0
# Add more variables to track other necessary financial data
net_change_list = []
months = []
great_inc = ["",0]
great_dec = ["",0]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int (first_row[1])
    previous_profit= int (first_row[1])

    # Process each row of data
    for row in reader:
        month =row[0]
        profit=int(row[1])
        
        # Track the total
        total_months += 1
        total_net +=profit
        
        # Track the net change
        if previous_profit !=0:
            net_change =profit-previous_profit
            net_change_list.append(net_change)
            months.append(month)

        # Calculate the greatest increase in profits (month and amount)
        if net_change > great_inc[1]:
            great_inc =[month,net_change]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < great_dec[1]:
            great_dec =[month,net_change]
            
        previous_profit=profit


# Calculate the average net change across the months
average_change=sum(net_change_list)/len(net_change_list)


# Generate the output summary
output = (f"Financial Analysis\n"
          f"----------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_net:,.2f}\n"
          f"Average Change: ${average_change:,.2f}\n"
          f"Greatest Increase in Profits: {great_inc[0]} (${int(great_inc[1]):,.2f})\n"
          f"Greatest Decrease in Profits: {great_dec[0]} (${int(great_dec[1]):,.2f})\n")

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
