#import OS with functions. Import csv module to read/write data in csv format:
import os
import csv

#files needed for input and output:
input_csvfile = os.path.join("Resources", "budget_data.csv")
output_analysis = os.path.join("Analysis", "budget_analysis.txt")

#lists to store data:
profits = []
dates = []
list_of_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]


#variables needed:
total_months = 0
total_net = 0
changes_total = 0
value = 0
change = 0

#to open files:
with open(input_csvfile) as data:
    csvread = csv.reader(data)
    
    header = next(csvread) 

    #this is january's data (1st row):
    first_row = next(csvread)  
    previous_net = int(first_row[1])
    #this is including january in count of total months: 
    total_months = total_months + 1
    #this is the total net starting with january: 
    total_net = total_net + int(first_row[1])
    
    #QUESTION 1: to find the total # of months included in dataset:     
    for row in csvread:
        total_months = total_months + 1

        #QUESTION 2: to find the net total amount and convert string into integer: 
        total_net = total_net + int(row[1])            

        #to calculate the change, then add it to list of changes:
        changes_total = int(row[1]) - previous_net

        
        # current row is now assigned to our previous_net variable
        previous_net = int(row[1])


        list_of_changes = list_of_changes + [changes_total]


        #QUESTION 4 & 5: Calculate the greatest increase in profits and greatest decrease in losses:
        if changes_total > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = changes_total

        if changes_total < greatest_decrease[1]:
            greatest_decrease[0] = row[0]  
            greatest_decrease[1] = changes_total  

        
#QUESTION 3: to find the average change in "Profit/Losses between months over entire period":
avg_change = sum(list_of_changes)/len(list_of_changes)

#Output exported to text file:
# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)
# Export the results to text file
with open(output_analysis, "w") as txt_file:
    txt_file.write(output)


""" text_file.write("Greatest Increase in Profits: "  + greatest_increase[0] +  "$" + str(greatest_increase[1] + "\n")
text_file = open("PYBank_Analysis.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("------------------------\n")
text_file.write("Total Months: " + str(total_months) + "\n")
text_file.write("Net Total Amount of Profit/Losses: " + "$" + str(total_net) + "\n")
text_file.write("Average Change: " + "$" + str(avg_change) + "\n")
#text_file.write("Greatest Increase in Profits: " + "$" + str(greatest_increase) + "\n")
text_file.write("Greatest Increase in Profits: "  + greatest_increase[0] +  "$" + (greatest_increase[1]) + "\n")
text_file.write("Greatest Increase in Profits: "  + greatest_decrease[0] +  "$" + (greatest_decrease[1]) + "\n")
#text_file.write("Greatest Decrease in Profits: " + "$" + str(greatest_decrease) + "\n")
text_file.close() """