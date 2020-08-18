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

    # Obtain total pnl for the time period in question
    total_pnl = sum(pnl)

    # Get average month-to-month change in PnL
    pnl_change = []
  
    for i in range(1, len(pnl)):
        pnl_change.append(pnl[i] - pnl[i-1])

    pnl_avgchange = round(sum(pnl_change) / len(pnl_change), 2)

    # Get greatest increase and greatest decrease in profits
    greatest_increase = max(pnl_change)
    greatest_decrease = min(pnl_change)

    # Obtain the month that saw this greatest changes in profit
    greatest_increase_month_list = []
    greatest_decrease_month_list = []
    for index, change in enumerate(pnl_change):
        if change == max(pnl_change):
            greatest_increase_month_list.append(months[index +1])
        elif change == min(pnl_change):
             greatest_decrease_month_list.append(months[index +1])

    # Convert lists in max and min into string for better display
    def convert(string_value, seperator=' '):
        return seperator.join(string_value)
    greatest_increase_month = convert(greatest_increase_month_list)
    greatest_decrease_month = convert(greatest_decrease_month_list)

    # Print output to terminal
       
    print("Financial Analysis")
    print("-"*40)
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_pnl}")
    print(f"Average Change: ${pnl_avgchange}") 
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) ")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")   

    # print output to text file

    data_analysis_text = os.path.join("Analysis", "analysis_results.txt")

    nl = "\n"
    output_file = open(data_analysis_text, "w")

    output_file.write(f"Financial Analysis {nl}")
    output_file.write(f" ---------------------------------------- {nl}")
    output_file.write(f"Total Months: {total_months} {nl}")
    output_file.write(f"Total: ${total_pnl} {nl}")
    output_file.write(f"Average Change: ${pnl_avgchange} {nl}")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) {nl}")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) {nl}")
    output_file.close()

   