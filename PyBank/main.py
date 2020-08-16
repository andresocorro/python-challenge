# Import necessary modules to run code
import os
import csv


# Go to file with data
pnl_csv = os.path.join("Resources","budget_data.csv")


all_rows = []
total_pnl = 0

# Open file with csvreader
with open(pnl_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)
    
    for row in csv_reader:
    #  Add rows to get total number of rows
        all_rows.append(row)
        total_months = len(all_rows)
    
    # Sum pnl column to obtain total change   
        total_pnl += int(row[1])
    
    print(total_months)
    print(total_pnl)