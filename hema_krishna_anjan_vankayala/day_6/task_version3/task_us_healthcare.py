# UST HealthCare 
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .
# Copy-paste CSV data — save as
# ust_healthcare_visits.csv
#patient_id,name,dob,gender,contact,provider_id,provider_name,department,visit_date,visit_type,diagnosis_codes,procedure_codes,billed_amount,insurance_provider,insurance_id,payment_status,discharge_date,follow_up_required,notes


# This smaller dataset keeps the same variety (Paid / Pending / Unpaid, missing insurance, decimal amounts, follow-up flags).

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
skipped_rows = 0
#Checking If a Value is Number
def is_number(s):
    try:
        float(s)  # Try converting to float
        return True
    except ValueError:
        return False
    
#Validating Required Fields and Conversion of Bill Amounts to Float
with open('ust_healthcare_visits_new.csv','r') as file:

    li=[]
    csv_reader = csv.DictReader(file)
    
    value_types_for_payment = ["Paid","Unpaid","Pending"]
    required_fields = ['patient_id','name','visit_date','billed_amount','payment_status']
    
    for row in csv_reader:
        
        if len(csv_reader.fieldnames)!= len(row):
            skipped_rows += 1 
            print(f"{row['patient_id']} Removed bacause of less/more values than expected")
            continue
        else:
            #Validating Required Fields
            is_continue = False
            for field in required_fields:
                if row[field].strip()=="":
                    skipped_rows += 1
                    is_continue = True
                    print(f"{row['patient_id']} Removed because the required field is Empty")
                    break
            if is_continue:
                continue
            if not is_number(row['billed_amount']):
                skipped_rows += 1 
                print(f"{row['patient_id']} Removed because amount is not numeric")
                continue

        # Normalize follow_up_required to "Yes" or "No" (treat empty as "No" )
        row['billed_amount'] = float(row['billed_amount'].strip())
        row['payment_status'] = row['payment_status'].strip().capitalize()

        #Normalization of follow_up_required
        if row["follow_up_required"]=="" or row["follow_up_required"]==0 or row["follow_up_required"][0]=='n' or row["follow_up_required"]=='N' or row["follow_up_required"]=="False" :
            row["follow_up_required"]="No"
        else:
            row["follow_up_required"]="Yes"

        li.append(row)
    print("Total rows skipped during processing:", skipped_rows)
  
#Rewrite the Cleaned and Normalized Data into the new cleaned csv file
with open('ust_healthcare_visits_cleaned_data.csv','w',newline='') as file:
    
    header = ['patient_id','name','visit_date','department','billed_amount','insurance_provider','payment_status','contact','follow_up_required']

    csv_writer = csv.DictWriter(file, fieldnames=header)
    
    csv_writer.writeheader()
    
    csv_writer.writerows(li)  
        
#Checking for Pending Payments 
with open('ust_healthcare_visits_cleaned_data.csv','r') as file:
    csv_reader = csv.DictReader(file)
    pending_list = []    

    for row in csv_reader:
    
        if row['payment_status'] != "Paid":
            pending_list.append(row)

#Create A pending_payments.csv
with open("new_pending_payments.csv",'w',newline="") as file:
    
    #create fieldnames list
    header = ['patient_id','name','visit_date','department','billed_amount','insurance_provider','payment_status','contact','follow_up_required']
    
    #Create Dictwriter Object
    csv_writer = csv.DictWriter(file,fieldnames=header)
    
    #Write fieldnames in Header
    csv_writer.writeheader()
    
    #Write all rows in csv file
    csv_writer.writerows(pending_list)

#To Generate Patient Summary CSV File
with open('ust_healthcare_visits_cleaned_data.csv','r') as file:
    dict = {}
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        if row['patient_id'] not in dict.keys():
            li={}
            li['name'] = row['name']
            li['visits_count'] = 1
            li['total_bill'] = float(row['billed_amount'])
            if row['payment_status'] != 'Paid':
                li['has_pending_status'] = True 
            else:
                li['has_pending_status']= False
                
            dict[row['patient_id']] = li 
        else:
            dict[row['patient_id']]['visits_count'] += 1 
            dict[row['patient_id']]['total_bill'] = dict.get(row['patient_id'])['total_bill'] + float(dict[row['patient_id']]['total_bill'])
            
            if dict[row['patient_id']]['has_pending_status'] or dict.get(row['patient_id']):
                dict[row['patient_id']]['has_pending_status'] = True 
    
# Preparing Data for Writing into patient_summary.csv
li_dict = []
for key,value in dict.items():
    new_li = []
    new_li.append(key)
    for key1,value1 in value.items():
        new_li.append(value1)
    li_dict.append(new_li)

#Writing into patient_summary.csv
with open('new_patient_summary.csv','w',newline="") as file:
    summary_header = ['patient_id','name','total_visits','total_billed','has_pending_payment']
    csv_write = csv.writer(file)
    csv_write.writerow(summary_header)
    csv_write.writerows(li_dict)
    
    
#Sample Output:
# P003 Removed because the required field is Empty
# Removed because the required field is Empty
# P005 Removed because amount is not numeric
# P016 Removed because amount is not numeric
# P023 Removed because the required field is Empty
# P029 Removed because amount is not numeric
# P040 Removed because amount is not numeric
# P052 Removed bacause of less/more values than expected
# P016 Removed because amount is not numeric
# Total rows skipped during processing: 9