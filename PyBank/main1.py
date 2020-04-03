import os 
import csv

bank_csv = os.path.join("Resources","budget_data.csv")

with open (bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ' ',quotechar='|')

    csv_header = next(csvreader)
    for row in csvreader:
        print(row)
        # if row  
        # print(sum(row)) 