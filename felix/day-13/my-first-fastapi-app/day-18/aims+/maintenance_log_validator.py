import csv
from datetime import date
maintenance_type_allowed = ["Repair" , "Service" , "Upgrade"]

with open("maintenance_log.csv","r") as file:
    read = csv.DictReader(file)
    headers = read.fieldnames

    with open("maintenance_log_final.csv","w",newline="") as validated:
        writer = csv.DictWriter(validated,headers)
        writer.writeheader()

    for row in read:
        try:
            if row[headers[1]].split("-")[0] != "UST":
                raise Exception("asset tag must be start with UST-")

            if row[headers[2]] not in maintenance_type_allowed:
                raise Exception("given maintenance type is not allowed")

            for char in row[headers[3]]:
                if not char.isspace():
                    if not char.isalpha():
                        raise Exception("Vendor name cannot contain numbers")

            if len(row[headers[4]]) < 10:
                raise Exception("Discription minimum length is 10")

            if float(row[headers[5]]) <= 0:
                raise Exception("Cost must be greater than zero")

            if date.fromisoformat(row[headers[6]]) > date.today():
                raise Exception("Invalid maintanance date")

            for char in row[headers[7]]:
                if not char.isspace():
                    if not char.isalpha():
                        raise Exception("Invalid technician name")

            if row[headers[8]] not in [ "Completed" , "Pending"]:
                raise Exception("Invalid status")
            
        except Exception as e:
            print("ERROR: ",e,row[headers[0]])
        else:
            with open("maintenance_log_final.csv","a",newline="") as validated:
                writer = csv.DictWriter(validated,headers)
                writer.writerow(row)