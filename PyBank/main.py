#import OS with functions. Import csv module to read/write data in csv format:
import os
import csv

#files needed for input and output:
input_csvfile = os.path.join("Resources", "budget_data.csv")
output_analysis = os.path.join("Analysis", "budget_analysis.txt")


#variables needed:
total_months = 0
total_net = 0
changes_total = 0
list_of_changes = []
value = 0
change = 0
profits = []
# greatest_increase =
# greatest_decrease =

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
    
    #to find the total # of months included in dataset:                 111111111111111111111111111111
    for row in csvread:
        total_months = total_months + 1

        #to find the net total amount and convert string into integer:   22222222222222222222222222222
        total_net = total_net + int(row[1])              

        # Calculate the change, then add it to list of changes:
        changes_total = int(row[1]) - previous_net
        profits.append(changes_total)
        previous_net = int(row[1])
        
        #Find the average change in "Profit/Losses between months over entire period" 3333333333333333333333
        avg_change = sum(profits)/len(profits)
        
    
    #to find the greatest increases/greatest decrease in profits (date & amount) over entire period:
    
#greatest_increase = max(new_list)
#greatest_decrease = min(new_list)