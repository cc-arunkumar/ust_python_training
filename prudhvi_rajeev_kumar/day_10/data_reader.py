import csv

with open("data/emp_details.csv", mode ='r')as file:

  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)