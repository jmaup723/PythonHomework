import os
import csv

output_path = os.path.join("..", "Module-3","budget_data.csv")
file_to_output = os.path.join("..", "Module-3", "PyBankFINAL.txt")

Profits_Losses = []
total_months = 0
monthly_delta = []
total_profit = 0
average = []
Inc_profit = ["", 0]
Dec_profit = ["", 999999999]
net_total = 0
delta = []


with open(output_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    first = next(csvreader)
    prec_delta = int(first[1])

    for row in csvreader:    
        #Add months
        #Date.append(row[0])
        #Add Profits and Losses
        #Profits_Losses.append(row[1])
        # total
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        #net change
        average_change = int(row[1]) - prec_delta
        prec_delta = int(row[1])
        average = average + [average_change]
        monthly_delta = monthly_delta + [row[0]]
        

        if average_change > Inc_profit[1]:
            Inc_profit[0] = row[0]
            Inc_profit[1] = average_change

        if average_change < Dec_profit[1]:
            Dec_profit[0] = row[0]
            Dec_profit[1] = average_change

#Calculate the monthly delta
net_delta = sum(average) / len(average)     


output = (f"Analysis"
    f"Total Months: {total_months}"
    f"Total: ${total_profit}"
    f"Average Change: ${round(net_delta, 2)}"
    f"Greatest Increase: {Inc_profit[0]} (${Inc_profit[1]})\n"
    f"Greatest Decrease: {Dec_profit[0]} (${Dec_profit[1]})\n")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    

        
        

