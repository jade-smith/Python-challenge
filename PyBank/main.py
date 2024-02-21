import csv

# Path to the CSV file
file_path = "/Users/jadesmith/Desktop/ptda-dec-2023/Assignments/Module-3/03-Python/PyBank/resources/budget_data.csv"

# Initialize variables to store financial analysis
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
change_in_profit_losses = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
profit_losses_changes = []

# Read the CSV file and perform analysis
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        
        # Calculate the total profit/losses
        total_profit_losses += int(row[1])
        
        # Calculate the change in profit/losses
        if total_months > 1:
            change_in_profit_losses = int(row[1]) - previous_profit_loss
            profit_losses_changes.append(change_in_profit_losses)
        
        # Update the previous profit/losses for the next iteration
        previous_profit_loss = int(row[1])
        
        # Determine the greatest increase in profits
        if change_in_profit_losses > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change_in_profit_losses
        
        # Determine the greatest decrease in profits
        if change_in_profit_losses < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_in_profit_losses

# Calculate the average change in profit/losses
average_change = sum(profit_losses_changes) / len(profit_losses_changes)

# Formatting
financial_analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_losses}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Print the analysis to the terminal
print(financial_analysis)

# Export to .txt
with open("financial_analysis.txt", "w") as text_file:
    text_file.write(financial_analysis)

