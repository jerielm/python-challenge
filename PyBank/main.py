#import modules
import os 
import csv

#declare records
total_number_of_months = 0
net_total_amount = 0
changes_list = []
increases = ["",0]
decreases = ["", 99999999999999999999]
month_of_change = []

#data file
file = os.path.join("Resources/budget_data.csv")

#open csv
with open(file) as budget_data:
    data = csv.reader(budget_data)
    header = next(data)

    #remove first row
    csvreader = next(data)
    total_number_of_months += 1
    net_total_amount += int(csvreader[1])
    previous_net_total = int(csvreader[1])

    for row in data:
        #total amount of revenue
        total_number_of_months +=1
        net_total_amount += int(row[1])

        #net changes
        net_changes = int(row[1]) - previous_net_total
        previous_net_total = int(row[1])
        month_of_change += [row[0]]
        changes_list += [net_changes]

        #greatest increase
        if net_changes > increases[1]:
            increases[0] = row[0]
            increases[1] = net_changes

        #greatest decrease
        if net_changes < decreases[1]:
            decreases[0] = row[0]
            decreases[1] = net_changes

#average of net changes
avg_net_changes = sum(changes_list) / len(changes_list)

 
print(f"Financial Analysis")
print(f"----------------------------------------")
print(f"Total Number of Months: {total_number_of_months}")
print(f"Total Revenue: ${net_total_amount}")
print(f"Average Change in Revenue: ${avg_net_changes}")
print(f"Largest Increase in Profits: ${increases[1]}")
print(f"Largest Decrease in Profits: ${decreases[1]}")



textfile = os.path.join("Analysis","PyBank_analysis.txt")
#create writer object
with open(textfile, 'w', newline='') as txtFile:
    txtFile.write(f"Financial Analysis\n")
    txtFile.write(f"----------------------------------------\n")
    txtFile.write(f"Total Number of Months: {total_number_of_months}\n")
    txtFile.write(f"Total Revenue: ${net_total_amount}\n")
    txtFile.write(f"Average Change in Revenue: ${avg_net_changes}\n")
    txtFile.write(f"Largest Increase in Profits: ${increases[1]}\n")
    txtFile.write(f"Largest Decrease in Profits: ${decreases[1]}\n")