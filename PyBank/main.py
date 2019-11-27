#import OS with functions. Import csv module to read/write data in csv format:
import os
import csv

#files needed for input and output:
input_csvfile = os.path.join("Resources", "budget_data.csv")
output_analysis = os.path.join("Analysis", "budget_analysis.txt")

#variables needed:
header = next
total_months = 0
total_net = 0
changes_total = 0
# greatest_increase =
# greatest_decrease =

#to open files:
with open(input_csvfile) as data:
    csvread = csv.reader(data)
    
    header = next(csvread) 
    

#to find the total # of months included in dataset:   
    for row in csvread:
        total_months = total_months + 1
        
#to find the net total amount and convert string into integer:
        total_net = total_net + int(row[1])
        
with open(input_csvfile, "r") as data:
#to split data on delimiter (commas):
    csvread = csv.reader(data, delimiter=",")

#to skip column headers:
    header = next(csvread)
    
#to start new list for cell values in 2nd column (#s):
    new_list = []

#to find the average of the changes over the entire period:
changes_total = sum(new_list)
changes_avg = changes_total/total_months
#print(changes_avg)


