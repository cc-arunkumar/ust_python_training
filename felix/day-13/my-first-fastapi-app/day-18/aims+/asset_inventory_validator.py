import csv
from datetime import datetime,date

allowed_assert_status = ["Available","Assigned","Repair","Repair"]
allowed_assert_type = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
allowed_manufacturer = ["Dell" , "HP" , "Lenovo" , "Samsung"]
condition_status_allowed = ["New" , "Good" , "Used" , "Damaged"]
location_allowed = ["TVM" , "Bangalore" , "Chennai" , "Hyderabad"]


with open("asset_inventory.csv","r") as file:
    read = csv.DictReader(file)
    headers = read.fieldnames
    headers.append("last_updated")

    with open("asset_inventory_validated.csv","w",newline="") as validated:
        writer = csv.DictWriter(validated,headers)
        writer.writeheader()

    for row in read:
        try:
            # asset_tag
            if row[headers[0]].split("-")[0] != "UST":
                raise Exception("asset tag must be start with UST-")
                
            # asset_type
            if row[headers[1]] not in allowed_assert_type:
                raise Exception("given asset type is not allowed")

            # serial_number
            if row[headers[2]] == None:
                raise Exception("Serial number cant be None")

            
            with open("asset_inventory_validated.csv","r") as validated:
                rows = csv.DictReader(validated)
                for i in rows:
                    if i[headers[2]] == row[headers[2]]:
                        raise Exception("serial_number must be unique")
            
            # manufacturer
            if row[headers[3]] == allowed_manufacturer:
                raise Exception("Manufacturer is not allowed")

            # model
            if row[headers[4]] == None:
                raise Exception("Model cannot be None")
            
            # purchase date
            if date.fromisoformat(row[headers[5]]) > date.today():
                raise Exception("Invalid purchase date")
            
            # Warrenty year
            if int(row[headers[6]])<=0 or int(row[headers[6]])>5:
                raise Exception("Invalid Warrenty year")

            # condition status
            if row[headers[7]] not in condition_status_allowed:
                raise Exception("Invalid condition status")

            # assigned to
            if headers[8] in row:
                if row[headers[8]] == "" or row[headers[8]] == None:
                    raise Exception("Invalid assigning")
            
            # asset status    
            if row[headers[10]] not in allowed_assert_status:
                raise Exception("Invalid asset status")

            # Location
            if row[headers[9]] not in location_allowed:
                raise Exception("Location not allowed")

            # last updated
            row[headers[11]] = datetime.now()

        except Exception as e:
            print("ERROR: ",e,row[headers[0]])    
        else:
            with open("asset_inventory_validated.csv","a",newline="") as validated:
                writer = csv.DictWriter(validated,headers)
                writer.writerow(row)
        
    print("Asset Inventory validation completed")