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

#  print counts: processed rows, skipped rows, rows in each
# output.
processed_rows=0
skipped_rows=0
rows=0
with open("ust_healthcare_visits.csv","r",newline='') as file:
    csv_dict_reader=csv.DictReader(file)
    

# Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any
# missing → skip that row (and print a short message).

# patient_id,name,dob,gender,contact,provider_id,provider_name,department,visit_date,visit_type,diagnosis_codes,procedure_codes,billed_amount,insurance_provider,insurance_id,payment_status,discharge_date,follow_up_required,notes

with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
        if 'patient_id'not in row or 'name' not in row or 'dob' not in row or 'gender' or 'contact' not in row or 'provider_id' not in row or 'provider_name'  or   'department' not in row or 'visit_date' not in row or 'visit_type' not in row or 'diagnosis_codes' not in row or 'procedure_codes' not in row or 'billed_amount' not in row or 'insurance_provider' not in row or 'insurance_id' not in row or 'payment_status' not in row or 'discharge_date' not in row or 'follow_up_required' not in row or 'notes' not in row :
            skipped_rows+1
        else:
            processed_rows+=1

             
# Convert billed_amount to float (if conversion fails, skip row).

with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
        if float(row['billed_amount']):
            row["billed_amount"]=float(row["billed_amount"])
            processed_rows+=1
        else:
            skipped_rows+=1


###  Trim white spaces for all strings 
with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
        for key in row:
            row[key]=row[key].strip()
# Normalize payment_status to Title case (e.g., "pending" → "Pending" ).
with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
            s=row["payment_status"]
            row["payment_status"]=s.title()


# Normalize follow_up_required to "Yes" or "No" (treat empty as "No" ).
with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
        if row['follow_up_required']=='':
            row["follow_up_required"]="No"
            



data=[]
with open("ust_healthcare_visits.csv","r") as file:
    csv_reader=csv.DictReader(file)
    next(csv_reader)
    for row in csv_reader:
        if row['payment_status']!="Paid":
            data.append(row)
pending_payment_size=len(data)

with open("pending_payments.csv","w",newline='') as file:
    header=["patient_id","name","dob","gender","contact","provider_id","provider_name","department","visit_date","visit_type","diagnosis_codes","procedure_codes","billed_amount","insurance_provider","insurance_id","payment_status","discharge_date","follow_up_required","notes"]
    # using the dictwriter for writing the values into the csv output file
    writer=csv.DictWriter(file,fieldnames=header)
    # writing the header
    writer.writeheader()
    # writing the dictionary of employee values into th eoutput csv file
    writer.writerows(data)
    
#using dict to get and lists 

my_dict={}
with open("ust_healthcare_visits.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if my_dict.get(row[0]):
            list1=my_dict[row[0]]
            list1[1]+=1
            list1[2]+=float(row[12])
        
        else:
            my_dict[row[0]]=[row[1],0,row[12],row[15]]
            
patient_summary_dat_Size=len(my_dict)
with open("patient_summary.csv","w",newline='') as file:
    header=["name","visits","billed_amount","payment_status"]
    # using the dictwriter for writing the values into the csv output file
    writer=csv.DictWriter(file,fieldnames=header)
    # writing the header
    writer.writeheader()
    # writing the dictionary of employee values into th eoutput csv file
    for key, values in my_dict.items():
        writer.writerow({"name": values[0],"visits": values[1],"billed_amount": float(values[2]),"payment_status": values[3]
    })

    


# printing the total upto 2 decimal points 
for key,values in my_dict.items():
    values[2]=round(float(values[2]),2)
    
# has_pending_payment = "Yes" if any visit for that patient is not Paid; otherwise "No" .
                  
with open("ust_healthcare_visits.csv","r") as file:
    csv_dict_reader=csv.DictReader(file)
    next(csv_dict_reader)
    for row in csv_dict_reader:
        # Normalize payment_status
        status = row["payment_status"].strip().title()

        # Add new column based on condition
        if status == "Pending":
            row["has_pending_payment"] = "Yes"
        else:
            row["has_pending_payment"] = "No"



    
                
print(f"The processed rows={processed_rows}")
print(f"The skipped_rows={skipped_rows} ")
print(f"the pending_payments.cs output size:{pending_payment_size}")
print(f"The patient_Summary.csv output size:{patient_summary_dat_Size}")
                
                
                
# sample execution
# Making out the summary ======================
# The processed rows=99
# The skipped_rows=0 
# the pending_payments.cs output size:55
# The patient_Summary.csv output size:100