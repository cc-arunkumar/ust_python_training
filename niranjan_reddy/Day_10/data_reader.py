import csv
with open("C:/Users/303467/Desktop/Python_Training/Day_10/data/emp_details.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        print(row)
