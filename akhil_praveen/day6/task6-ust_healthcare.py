# UST Healthcare (CSV Read / Write)
# TASK
# 1. Read ust_healthcare_visits.csv with csv.DictReader .
# 2. Basic validation / normalization:
# Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any
# missing → skip that row (and print a short message).
# Convert billed_amount to float (if conversion fails, skip row).
# Trim whitespace from string fields.
# Normalize payment_status to Title case (e.g., "pending" → "Pending" ).
# Normalize follow_up_required to "Yes" or "No" (treat empty as "No" ).
# 3. Create outputs:
# pending_payments.csv : all cleaned columns for rows where payment_status != "Paid" .
# patient_summary.csv : aggregated per patient_id with columns:
# patient_id, name, total_visits, total_billed, has_pending_payment
# total_billed formatted with 2 decimals (e.g., 7500.00 ).
# has_pending_payment = "Yes" if any visit for that patient is not Paid;
# otherwise "No" .
# 4. Console summary: print counts: processed rows, skipped rows, rows in each
# output.

import csv
#validate function
def validate(row):
    # header to validate
    header = ["patient_id" , "name" , "visit_date" , "billed_amount" , "payment_status"]
    #string list to strip
    string_val = ["name","department","insurance_provider","payment_status","follow_up_required"]
    #validation loop for every rows
    for i in header:      
        #checking for skipping condition                
        if len(str(row[i]).strip())<=0: 
            print(f"skipped -> {i} not found in line no: {count['total']} data")
            return False
        else:
            # billed value to float
            if i=="billed_amount":
                try:
                    row["billed_amount"]=round(float(row["billed_amount"]),2)
                except ValueError:
                    print(f"skipped -> cant convert bill amount!")
                    return False
            # stripping blank space
            for j in string_val:
                row[j]=row[j].strip()
            # changing lowcasing to capitalize(first letter capitalize)
            if i=="payment_status":
                    row[i]=row[i].lower().capitalize()
            # change in follow up required blank to No
            if len(row["follow_up_required"].strip())==0:
                row["follow_up_required"]="No"
                 
    return True              
      


# create and open csv file

count={
    "skipped":0,
    "total":0,
    "processed":0}
clean_data =[]
# creating and opening data file
with open("ust_healthcare_visits1.csv","r") as file:
    # create object for file using dictreader
    csv_file = csv.DictReader(file)
    field_header = csv_file.fieldnames
    # getting each line of data from file
    for row in csv_file:
        count["total"]+=1
        skipped=0
        cond =validate(row)
        # checking for skipping rows
        if cond and len(row)==len(field_header):
            clean_data.append(row)
            count["processed"]+=1
        elif cond:
            print("skipped -> Extra field")
            count["skipped"]+=1
        else:
            count["skipped"]+=1
    print("Data cleaning completed!\n")
# Creating and opening pending payment file
with open("pending_payments.csv","w",newline="") as pending_file:
            
    # creating header
    header = field_header
    
    # create dictwriter object
    csv_file1 = csv.DictWriter(pending_file,fieldnames=header)
    
    # write the header into the csv file
    csv_file1.writeheader()
    
    for row in clean_data:
        if row["payment_status"].capitalize()!="Paid":
            # write the pending data into the csv file
            csv_file1.writerow(row)
    print("Pending payment csv created and added all the corresponding datas.\n")

# summary header values
summ_header=["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]

# creating and opening patients summary file
with open("patient_summary.csv","w",newline="") as patient_file:
            
    # creating header for dictionay csv
    header = summ_header
    
    # create dictwriter object
    csv_file = csv.DictWriter(patient_file,fieldnames=header)
    
    # write the header into the csv file
    csv_file.writeheader()
    struct = {}
    data=[]
    # adding patient summary into struct(dictionary for counting repetitive data values for a single patient)
    for i in clean_data:
        if i["patient_id"] not in struct:
            struct[i["patient_id"]]={
                "name":i["name"],
                "total_visits":0,
                "total_billed":0,
                "has_pending_payment":""
            }
        struct[i["patient_id"]]["total_visits"]+=1
        struct[i["patient_id"]]["total_billed"]+=i["billed_amount"]
        struct[i["patient_id"]]["has_pending_payment"]="Yes" if i["payment_status"]=="Paid" else "No"
    # entering data into patients summary file
    for data in struct:
        csv_file.writerow({
            "patient_id":data, "name":struct[data]["name"], "total_visits":struct[data]["total_visits"], "total_billed":struct[data]["total_billed"], "has_pending_payment":struct[data]["has_pending_payment"]
        })
    
    print("Patients summary csv created and added all the corresponding datas.\n")
print(f"Processed data: {count['processed']}\n")

print(f"Skipped data: {count["skipped"]}\n")

print(f"Total data: {count['total']}")

#output

# skipped -> name not found in line no: 3 data
# skipped -> patient_id not found in line no: 4 data
# skipped -> cant convert bill amount!
# skipped -> cant convert bill amount!
# skipped -> visit_date not found in line no: 23 data
# skipped -> cant convert bill amount!
# skipped -> cant convert bill amount!
# skipped -> Extra field
# skipped -> cant convert bill amount!
# Data cleaning completed!

# Pending payment csv created and added all the corresponding datas.

# Patients summary csv created and added all the corresponding datas.

# Processed data: 101

# Skipped data: 9

# Total data: 110