# UST Healthcare (CSV Read / Write)
# Duration: 20–30 minutes
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .

import csv

#store the corrected data
data=[]
#opening the csv file in read mode
with open("ust_healthcare_visits.csv","r") as file:
    #step 1: opening in the Dictreader
    reader=csv.DictReader(file) 
    
    #step 2:Basic validation / normalization
    for i,row in enumerate(reader,start=1):
        
        #Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any missing → skip that row (and print a short message)
        if row["patient_id"]=="" or row["name"]=="" or row["visit_date"]=="" or row["billed_amount"]=="" or row["payment_status"]=="" :
            print("Field Missing")
            continue
        
        #strip whitespace from all fields
        for key in row:
            row[key]=row[key].strip()
        
        # Convert billed_amount to float. If conversion fails → skip that row (and print a short message)
        if row["billed_amount"]!="":
            row["billed_amount"]=float(row["billed_amount"])
        else:
            continue
        
        # Standardize payment_status to Paid / Pending / Unpaid (case insensitive). If value is unrecognized → skip that row (and print a short message)
        row["payment_status"]=row["payment_status"].capitalize()
        
        # Standardize follow_up_required to Yes / No (case insensitive). If value is unrecognized or missing → set to No (and print a short message)
        if row["follow_up_required"]=="yes":
            row["follow_up_required"]=="Yes"
            print("Corrected Follow up to Yes")
        if row["follow_up_required"]=="no" or row["follow_up_required"]=="":
            row["follow_up_required"]=="No"
            print("Corrected Follow up to No")
        
        data.append(row)
        
#print(data)
#Step 1: 
# pending_payments.csv : all visits where payment_status is not Paid with columns:
with open("pending_payments.csv",mode="w",newline="") as appendfile:
    header=["patient_id","name","visit_date","department","billed_amount","insurance_provider","payment_status","contact","follow_up_required"]
    writer=csv.DictWriter(appendfile,fieldnames=header)
    writer.writeheader()
    for row in data:
        if row["payment_status"]!="Paid":
            writer.writerow(row)
            
#Step 2: 
# patient_summary.csv : aggregated per patient_id with columns:
# patient_id, name, total_visits, total_billed, has_pending_payment
# total_billed formatted with  decimals 
# has_pending_payment = "Yes" if any visit for that patient is not Paid;
# otherwise "No" .
            
        
with open("patient_summary.csv",mode="w",newline="") as summaryfile:
    header=["patient_id","name","total_visits","total_billed","has_pending_payments"]
    writer=csv.DictWriter(summaryfile,fieldnames=header)
    writer.writeheader()
    
    #creating an dictionary to store patient summary
    patient_dict={}
    for row in data:
        pid=row["patient_id"]
        #if patient doesnt exist in dictionary add it
        if pid not in patient_dict:
            patient_dict[pid]={"name":row["name"],"total_visits":0,"total_billed":0.0}
        
        patient_dict[pid]["total_visits"]+=1
        patient_dict[pid]["total_billed"]+=row["billed_amount"]
    
    #writing records into the file
    for pid,info in patient_dict.items():
       
        #checking if the payment is paid
        flag=any(r["patient_id"]==pid and r["payment_status"]!="Paid" for r in data)
        if flag:
            str="Yes"
        else :
            str="No"
            
        writer.writerow({
            "patient_id":pid,
            "name":info["name"],
            "total_visits":info["total_visits"],
            "total_billed":info["total_billed"],
            "has_pending_payments": str
        })
    