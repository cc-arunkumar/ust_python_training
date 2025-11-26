import csv


cities = [
    "Bangalore",
    "Kolkata",
    "Chennai",
    "Mumbai",
    "Hyderabad",
    "Pune",
    "Chennaai" 
]


with open("vendor_master.csv","r") as file:
    read = csv.DictReader(file)
    headers = read.fieldnames

    with open("vendor_master_validated.csv","w",newline="") as validated:
        writer = csv.DictWriter(validated,headers)
        writer.writeheader()

    for row in read:
        try:
            if len(row[headers[1]]) > 100:
                raise Exception("Vendor name cannot exceed 100 characters")
            
            for char in row[headers[1]]:
                if char.isdigit():
                    raise Exception("Vendor name cannot contain numbers")

            if len(row[headers[2]]) > 100:
                raise Exception("Contact person cannot exceed 100 characters")
            
            for char in row[headers[2]]:
                if char.isdigit():
                    raise Exception("Contact person cannot contain numbers")

            if len(row[headers[3]]) != 10:
                raise Exception("Invalid Phone number")
            
            for char in row[headers[3]]:
                if not char.isdigit():
                    raise Exception("Invalid Phone number")

            if len(row[headers[4]]) != 15:
                raise Exception("Invalid GST number")
            
            for char in row[headers[4]]:
                if not char.isalnum():
                    raise Exception("Invalid GST number")

            if len(row[headers[5]].split("@")) != 2 or len(row[headers[5]].split("@")[1].split(".")) != 2:
                raise Exception("Invalid email")

            if len(row[headers[6]]) > 200:
                raise Exception("Address length exceeded")

            if row[headers[7]] not in cities:
                raise Exception("Invalid city")

            if row[headers[8]] not in [ "Active" , "Inactive" ]:
                raise Exception("Active Status not allowed")

        except Exception as e:
            print("ERROR: ",e)
        else:
            with open("vendor_master_validated.csv","a",newline="") as validated:
                writer = csv.DictWriter(validated,headers)
                writer.writerow(row)

    print("Vendor Master Validated")