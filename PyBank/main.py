# Import necessary modules to run code
import os
import csv


# Go to file with data
pnl_csv = os.path.join("Resources","budget_data.csv")



# Open file with csvreader
with open(pnl_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)

    # Create lists for each column to split data in two different lists
    months = []
    pnl = []
    
    for row in csv_reader:
    #  Add rows to get total number of rows
        months.append(row[0])
        pnl.append(int(row[1]))

    # Obtain total months of data
    total_months = len(months)
    # print(total_months)

    # Obtain total pnl for the time period in question
    total_pnl = sum(pnl)
    print(f"${total_pnl}")
  
    