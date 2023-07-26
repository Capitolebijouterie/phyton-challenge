import csv
import os

bank=os.path.join("Resources","budget_data.csv")
with open(bank,'r') as file: 
 
    csvreader = csv.reader(file)
    header = next (csvreader)
    first = next(csvreader)
    number_months = +1 
    total = 0.0
    net_change_list = []
    previous_net_change= int(first[1])
    for row in csvreader:
        number_months = number_months + 1
        total += int(row[1])
        net_change = int(row[1]) - previous_net_change
        previous_net_change = int(row[1])
        net_change_list.append(net_change)
    averagenet_change = sum(net_change_list)/number_months
    print (averagenet_change)

print(f'Total Number of Months: {number_months}')

print (f'Profit/Losses: {total}' )








