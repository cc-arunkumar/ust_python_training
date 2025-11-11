import csv

# Read ust_healthcare_visits.csv with csv.DictReader
with open(r"deva_prasath\day-6\ust_healthcare_visits.csv","r") as file:
    print("Data Present in ust healthcare:")
    
    # Create A DictWriter object
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row)

# Creating count 
count = {
    "skipped": 0,  
    "total": 0,   
    "processed": 0 
}

# Creating new_data list for processed rows
data = []
# Define expected headers for the CSV files
headers = ["patient_id","name","visit_date","billed_amount","payment_status"]
# Open a csv file in read mode
with open(r"deva_prasath\day-6\ust_healthcare_visits.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    field_header=csv_reader.fieldnames
    
    #iterating thrugh csv_reader
    for row in csv_reader:
        count["total"] += 1

        row = {key: val.strip() if isinstance(val, str) else val for key, val in row.items()}
        
        #setting a boolean value to a variable
        flag = False
        
        #iterating through the headers
        for field in headers:
            if not row.get(field) or len(row)!=len(field_header):  
                print(f"Skipping row {count['total']} due to missing field: {field}")
                #status changed to true
                flag = True 
                break
        
        if flag:
            #increamenting skipped count
            count["skipped"] += 1  
            continue  
        
        try:
            #converting to title case
            row['payment_status'] = row['payment_status'].title()
            #changing to yes and no  
            row['follow_up_required'] = 'Yes' if row.get('follow_up_required') else 'No'
            #replacing special symbols
            row['billed_amount'] = float(row['billed_amount'].replace('₹', '').replace(',', ''))
            data.append(row)
            #incrementing processed count
            count["processed"] += 1 
        except ValueError:
            print(f"Skipping row {count['total']} due to invalid 'billed_amount' value: {row['billed_amount']}")
            count["skipped"] += 1  
            continue  

                     
print(f"Total rows: {count['total']}")
print(f"processed rows: {count['processed']}")
print(f"skipped rows: {count['skipped']}")

#Sample output

# Skipping row 3 due to missing field: name
# Skipping row 4 due to missing field: patient_id
# Skipping row 5 due to invalid 'billed_amount' value: one thousand
# Skipping row 16 due to invalid 'billed_amount' value: â‚¹8200.00
# Skipping row 23 due to missing field: visit_date
# Skipping row 29 due to invalid 'billed_amount' value: five thousand two hundred
# Skipping row 40 due to invalid 'billed_amount' value: 41OO.00
# Skipping row 52 due to missing field: patient_id
# Skipping row 101 due to invalid 'billed_amount' value: â‚¹8200.00
# Total rows: 110
# processed rows: 101
# skipped rows: 9
