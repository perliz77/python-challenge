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
        #print("Total Months: ", total_months)

        #QUESTION 2: to find the net total amount and convert string into integer: 
        total_net = total_net + int(row[1])    
        #print("Total: " + "$", total_net)         

        #to calculate the change, then add it to list of changes:
        changes_total = int(row[1]) - previous_net
        profits.append(changes_total)
        previous_net = int(row[1])
        
        #QUESTION 3: to find the average change in "Profit/Losses between months over entire period" 
        avg_change = sum(profits)/len(profits)
        #print("Average Change: " + "$", avg_change)
    
#QUESTION 4 & 5: Greatest increase in profits and greatest decrease in losses(amount):        
    greatest_increase = max(profits) 
    #print("Greatest Increase in Profits: " + "$", greatest_increase)
    greatest_decrease = min(profits)
    #print("Greatest Decrease in Profits: " + "$", greatest_decrease)
    
    
    
 #QUESTION 4 & 5: Greatest increase in profits and greatest decrease in losses(date): 
    #greatest_index = profits.index(greatest_increase)                             
    #increase_date = date[list_of_changes.index(greatest_increase)]
    #print(increase_date)
