import os
import csv

csvfile = os.path.join("budget_data.csv")
with open(csvfile, "r"):
    csvread = csv.reader(csvfile)
    



