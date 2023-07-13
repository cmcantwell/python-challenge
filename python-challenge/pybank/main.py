# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join( 'Resources', 'budget_data.csv')
file_to_output= os.path.join("analysis/budget_data.txt")
#set variabales
total_of_months=0
total_profits=0
changes_in_month=[]
previous_profits=0
change_profits=0
profit_change_list=[]
average_change=0
max_increase=["", 0]
max_decrease=["",99999999]
# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:
       # print(row)
        #The total number of months included in the dataset
        total_of_months=total_of_months+1
      
        total_profits=total_profits +int(row[1])
        if total_of_months >1:


            change_profits=int(row[1])-previous_profits
            profit_change_list.append(change_profits)
            if(change_profits>max_increase[1]):
                max_increase[0]=row[0]
                max_increase[1]=change_profits  

            if(change_profits<max_decrease[1]):
                max_decrease[0]=row[0]
                max_decrease[1]=change_profits

        previous_profits=int(row[1])
        
        #profit_change_list=profit_change_list + [change_profits]
        #changes_in_month=changes_in_month +[row[0]]
        


average_change=round(sum(profit_change_list)/len(profit_change_list),2)
# print(total_of_months)
# print(total_profits)
# #print(change_profits)
# print(average_change)
# print(max_increase)
# print(max_decrease)

output_txt=(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_of_months}\n"
f"Total: ${total_profits}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})"
)
print(output_txt)
with open(file_to_output,"w") as output_file:
    output_file.write(output_txt)