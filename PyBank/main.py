# Import necessary modules to run code
import os
import csv

# Go to file with data
pnl_csv = os.path.join("Resources","budget_data.csv")

# Open file with csvreader

with open(pnl_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        total_months = len(list(csv_reader))
        print(total_months)
