import os 
import csv
import pandas as pd

csv_file =os.path.join('Resources','budget_data.csv')
budget_data_file = pd.read_csv(csv_file)
print(budget_data_file.head())
total_month = sum(budget_data_file['Date'].value_counts())
net_total_amount = sum(budget_data_file['Profit/Losses'])
max_profit = budget_data_file.iloc[budget_data_file['Profit/Losses'].idxmax()]
min_profit = budget_data_file.iloc[budget_data_file['Profit/Losses'].idxmin()]

average_change = int(net_total_amount/total_month)

print(f"Total Months: {total_month}")
print(f"Total: {net_total_amount}")
print(f"Average Change: ${average_change}")
print(max_profit)
print(min_profit) 

output_file = os.path.join('PyBank_Result.txt')

with open(output_file,"w") as file:
    file.write(f"Total Months: {total_month}")
    file.write("\n")
    file.write(f"Total: {net_total_amount}")
    file.write("\n")
    file.write(f"Average Change: ${average_change}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: \n{max_profit}")
    file.write("\n")
    file.write(f"Greatest Losses in Profits: \n{min_profit}") 