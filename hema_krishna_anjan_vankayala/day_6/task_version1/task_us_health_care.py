#UST HealthCare 
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .
# Copy-paste CSV data — save as
# ust_healthcare_visits.csv
# patient_id,name,visit_date,department,billed_amount,insurance_provider,payment_status,contact,follow_up_required
# P001,Arun Kumar,2025-10-01,Cardiology,7500.00,MedSecure,Paid,9810012345,Yes
# P002,Riya Sharma,2025-10-02,Orthopedics,12000.00,HealthPlus,Pending,9810098765,No
# P003,John Doe,2025-10-02,Neurology,3500.00,,Unpaid,8800123456,No
# P004,Meena Patel,2025-10-03,Cardiology,2200.00,MedSecure,Paid,7700123456,No
# P005,Suresh K,2025-10-03,General Medicine,1800.00,HealthPlus,Pending,9900112233,Yes
# P006,Neha Verma,2025-10-04,ENT,4800.50,MedSecure,Paid,9600001111,No
# P007,Alex Johnson,2025-10-04,Neurology,6000.00,GlobalCare,Pending,7000005555,Yes

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

#Validating Required Fields and Conversion of Bill Amounts to Float
with open('ust_healthcare_visits.csv','r') as file:
    li=[]
    csv_reader = csv.DictReader(file)
    value_types_for_payment = ["paid","pending","unpaid"]
    required_fields = ['patient_id','name','visit_date','billed_amount','payment_status']
    
    for row in csv_reader:
    
        if(row['patient_id']=="" or row['name']=="" or row['visit_date']=="" or row['billed_amount']=="" or row['payment_status']==""):
            print(f"Incomplete Details for the {row['patient_id']}")
            continue
            
        ld = {}
        for key,value in row.items():
            ##Removing Whitespaces for String Type
            if  isinstance(value,str):
                ld[key]=value.strip()
            else:
                ld[key] = value
                
            #Check for the Tile Case in 'payment_status'
            if key=="payment_status" and value in value_types_for_payment:
                ld[key] = value[0].upper() + value[1:]
            
            #Check for the Null Values in follow_up_required
            if key=='follow_up_required' and value=="":
                ld[key] = "No"
            
            if key=="follow_up_required" and value in ['yes','no']:
                if value=='yes':
                    ld[key] = "Yes"
                else:
                    ld[key] = "No"
        
        li.append(ld)
        
#Rewrite the Cleaned and Normalized Data into the csv file
with open('ust_healthcare_visits.csv','w',newline='') as file:
    
    header = ['patient_id','name','visit_date','department','billed_amount','insurance_provider','payment_status','contact','follow_up_required']

    csv_writer = csv.DictWriter(file, fieldnames=header)
    
    csv_writer.writeheader()
    
    csv_writer.writerows(li)  
        
        
with open('ust_healthcare_visits.csv','r') as file:
    csv_reader = csv.DictReader(file)
    pending_list = []    

    for row in csv_reader:
    
        if row['payment_status'] != "Paid":
            pending_list.append(row)

#Create A pending_payments.csv
with open("pending_payments.csv",'w',newline="") as file:
    
    #create fieldnames list
    header = ['patient_id','name','visit_date','department','billed_amount','insurance_provider','payment_status','contact','follow_up_required']
    
    #Create Dictwriter Object
    csv_writer = csv.DictWriter(file,fieldnames=header)
    
    #Write fieldnames in Header
    csv_writer.writeheader()
    
    #Write all rows in csv file
    csv_writer.writerows(pending_list)

#To Generate Patient Summary CSV File

with open('ust_healthcare_visits.csv','r') as file:
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
    

li_dict = []
for key,value in dict.items():
    new_li = []
    new_li.append(key)
    for key1,value1 in value.items():
        new_li.append(value1)
    li_dict.append(new_li)


with open('patient_summary.csv','w',newline="") as file:
    summary_header = ['patient_id','name','total_visits','total_billed','has_pending_payment']
    csv_write = csv.writer(file)
    csv_write.writerow(summary_header)
    csv_write.writerows(li_dict)
    
    
#Sample Output
#patient_summary.csv 
    # patient_id,name,total_visits,total_billed,has_pending_payment
    # P001,Arun Kumar,1,7500.0,False
    # P002,Riya Sharma,1,12000.0,True
    # P003,John Doe,1,3500.0,True
    # P004,Meena Patel,1,2200.0,False
    # P005,Suresh K,1,1800.0,True
    # P006,Neha Verma,1,4800.5,False
    # P007,Alex Johnson,1,6000.0,True

#pending_payments.csv
    # patient_id,name,visit_date,department,billed_amount,insurance_provider,payment_status,contact,follow_up_required
    # P002,Riya Sharma,2025-10-02,Orthopedics,12000.00,HealthPlus,Pending,9810098765,No
    # P003,John Doe,2025-10-02,Neurology,3500.00,,Unpaid,8800123456,No
    # P005,Suresh K,2025-10-03,General Medicine,1800.00,HealthPlus,Pending,9900112233,Yes
    # P007,Alex Johnson,2025-10-04,Neurology,6000.00,GlobalCare,Pending,7000005555,Yes

        
        