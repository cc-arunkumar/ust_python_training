# UST Healthcare (CSV Read / Write)
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .
# Task Requirements
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

#Defining a global counter dictionary
count={
    "skipped":0,
    "total":0,
    "processed":0
}

#Function to validate wether the row needs to be considered
def validate(item):
    #Defining the required fields
    required_items = ["patient_id","name","visit_date","billed_amount","payment_status"]

    #Defining the string fields
    string_trim = ["name","payment_status","department","insurance_provider","follow_up_required"]

    for j in required_items:
        
        try:
            #Check for value exist in the field
            if(len(str(item[j]).strip())>0 and  float(item["billed_amount"])):

                #Convert billed_amount to float upto 2 decimal
                if(j=="billed_amount" and item["billed_amount"]):
                    if(item["billed_amount"].isdigit()):
                        item["billed_amount"]=round(float(int(item["billed_amount"])),2)

                #For flushing spaces in the strings
                for st in string_trim:
                    item[st]=item[st].strip()

                #For capitalizing the first letter in payment_status
                if(j=="payment_status"):
                    item["payment_status"]=item["payment_status"].lower().capitalize()

                #For assigning No to blank follow up required field
                if(len(item["follow_up_required"].strip())==0):
                    item["follow_up_required"]="No"  

            else:
                #To find the total skipped record
                count["skipped"]+=1
                return False,f"{j} not found in the row"
        except ValueError:
            count["skipped"]+=1
            return False,f"Cannot convert bill value in the row"
        
    #To find the total processed record
    count["processed"]+=1
    return True,f"Row Processed"

#Read main csv file
with open("ust_healthcare_visits01.csv","r") as file1:
    all_data = csv.DictReader(file1)
    header = all_data.fieldnames
    
    #For storing the clean data
    clean_data=[]
    for i in all_data:
        count["total"]+=1
        l=len(header)
        #Validate function returns two values T/F and a message 
        con,stmt=validate(i)
        if(con and l==len(i.keys())):
            clean_data.append(i)
        else:
            if(stmt!="Row Processed"):
                print(f"Skipped due to {stmt}")
            else:
                print("Skipped due to extra field for row")
                count["skipped"]+=1
                count["processed"]-=1

    #Data cleaning is completed
    print("Data cleaning completed!!!")

#Open a new csv in write mode for pending payments
with open("pending_payments.csv","w",newline="") as file2:
    if clean_data:
        processed = csv.DictWriter(file2,header)
        processed.writeheader()
        #To store all those cleaned record whose status is not Paid
        for i in clean_data:
            if(i["payment_status"].capitalize()!="Paid"):
                processed.writerow(i)
        
        #Successfully created pending payments
        print("Pending Payments Created!!!!!")

#Open a new csv in write mode for patient summary
with open("patient_summary.csv","w",newline="") as file3:
    struct = {}
    header = ["patient_id","name","total_visits","total_billed","has_pending_payment"]
    summary = csv.DictWriter(file3,header)
    summary.writeheader()
    if clean_data:
        for i in clean_data:
            #Create a dict record if patient id not exist in struct
            if(i["patient_id"] not in struct):
                struct[i["patient_id"]]={
                        "name":i["name"],
                        "total_visits":0,
                        "total_billed":0,
                        "has_pending_payment":""
                    }
            #If again the same patient id comes existing record for the patient will be updated
            struct[i["patient_id"]]["has_pending_payment"]="Yes" if  i["payment_status"]=="Paid" else "No"
            struct[i["patient_id"]]["total_visits"]+=1
            struct[i["patient_id"]]["total_billed"]+=float(i["billed_amount"])
        
        #For writing into the new csv we use the data that is updated in struct
        for data in struct:
            summary.writerow({"patient_id":data,
                            "name":struct[data]["name"],
                            "total_visits":struct[data]["total_visits"],
                            "total_billed":struct[data]["total_billed"],
                            "has_pending_payment":struct[data]["has_pending_payment"]
                            })
        print("Patient Summary Created!!!!!")
print(f"Processed data : {count['processed']}")   
print(f"Skipped data : {count['skipped']}")   
print(f"Total data : {count['total']}")       

#Output
# Skipped due to name not found for in the row
# Skipped due to patient_id not found for in the row
# Skipped due to Cannot convert bill value in the row
# Skipped due to Cannot convert bill value in the row
# Skipped due to visit_date not found for in the row
# Skipped due to Cannot convert bill value in the row
# Skipped due to Cannot convert bill value in the row
# Skipped due to extra field for row
# Skipped due to Cannot convert bill value in the row
# Data cleaning completed!!!
# Pending Payments Created!!!!!
# Patient Summary Created!!!!!
# Processed data : 101
# Skipped data : 9
# Total data : 110