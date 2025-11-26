import csv
from datetime import date

location_allowed = ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]

with open("employee_directory.csv","r") as file:
    read = csv.DictReader(file)
    headers = read.fieldnames

    with open("employee_derectory_validated.csv","w",newline="") as validated:
        writer = csv.DictWriter(validated,headers)
        writer.writeheader()

    for row in read:
        try:
            if row[headers[0]].split("-")[0] != "USTEMP":
                raise Exception("asset tag must be start with USTEMP-")

            if row[headers[1]] == None:
                raise Exception("Name cannot be a None value")

            if len(row[headers[2]].split("@")) != 2 or len(row[headers[2]].split("@")[1].split(".")) != 2:
                raise Exception("Invalid email")

            if len(row[headers[3]]) != 10:
                raise Exception("Invalid Phone number")

            if row[headers[5]] not in location_allowed:
                raise Exception("Location not allowed")

            if date.fromisoformat(row[headers[6]]) > date.today():
                raise Exception("Invalid join date")

            if row[headers[7]] not in [ "Active" , "Resigned" ]:
                raise Exception("Status not allowed")

        except Exception as e:
            print("ERROR: ",e)
        else:
            with open("employee_derectory_validated.csv","a",newline="") as validated:
                writer = csv.DictWriter(validated,headers)
                writer.writerow(row)
