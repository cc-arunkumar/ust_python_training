import csv
with open("one.csv","r") as file:
    cs = csv.reader(file)
    for i in cs:
        print(i)