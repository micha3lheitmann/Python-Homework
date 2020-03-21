import os
import csv
file = os.path.join("..", "PyFinances", "Finances.csv")
with open(r"C:\Users\penny\Desktop\PyChallenge\PyFinances\Finances.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #create empty lists to add the csv values  
    month_count = []
    profit = []
    change_profit = []
    
                      
    #iterate through the values and add them to the empty list using .append
    for row in csvreader:
        month_count.append(row[1])
        profit.append(int(row[0]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#evaluate the max and min from the list made
increase = max(change_profit)
decrease = min(change_profit)

#using the index, 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# f-strings provide a concise and convenient way to embed python expressions inside string literals for formatting

print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

# The “w” option will delete any previous existing file and create a new file to write.

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write("Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")