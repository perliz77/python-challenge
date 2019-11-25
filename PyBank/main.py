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
# avg_changes_revenue =
# greatest_increase =
# greatest_decrease =

#to open files:
with open(input_csvfile) as data:
    csvread = csv.reader(data)
    #print(csvread)
    header = next(csvread) 
    #print(header)  

#to find the total # of months included in dataset:   
    for row in csvread:
        total_months = total_months + 1
#to find the net total amount and convert string into integer:
        total_net = total_net + int(row[1])
