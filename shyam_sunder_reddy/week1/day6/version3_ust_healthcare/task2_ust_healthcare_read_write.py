# UST Healthcare (CSV Read / Write)
# Duration: 20–30 minutes
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .

import csv

#store the corrected data
data=[]
skips=0
#opening the csv file in read mode
with open("ust_healthcare_visits.csv","r") as file:
    #step 1: opening in the Dictreader
    reader=csv.DictReader(file) 
    header=len(reader.fieldnames)
    #step 2:Basic validation / normalization
    for i,row in enumerate(reader,start=1):
        
        # Check for extra fields (i.e., more fields than expected). If any → skip that row (and print a short message)
        if len(row)!=header:
            print("Extra field in row",row["patient_id"])
            skips+=1
            continue

        #Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any missing → skip that row (and print a short message)
        required_fields=["patient_id","name","visit_date","billed_amount","payment_status"]
        for field in required_fields:
            if row[field].strip()=="":
                print("Field Missing",row["patient_id"])
                skips+=1
                continue
        
        #strip whitespace from all fields
        for key,value in row.items():
            # print(value)
            if isinstance(value,str):
                row[key]=value.strip()
        
        
        # Convert billed_amount to float. If conversion fails → skip that row (and print a short message)
        # if row["billed_amount"].isdigit():
        #     row["billed_amount"]=float(row["billed_amount"])
        # else:
        #     skips+=1
        #     continue
        try:
            float(row["billed_amount"])
        except ValueError:
            skips+=1
            print("Not a float",row["patient_id"])
            continue
        
        # Standardize payment_status to Paid / Pending / Unpaid (case insensitive). If value is unrecognized → skip that row (and print a short message)
        row["payment_status"]=row["payment_status"].capitalize()
        
        # Standardize follow_up_required to Yes / No (case insensitive). If value is unrecognized or missing → set to No (and print a short message)
        if row["follow_up_required"]=="":
            row["follow_up_required"]="No"
        else:
            row["follow_up_required"]=row["follow_up_required"].capitalize()
        
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
        patient_dict[pid]["total_billed"]+=float(row["billed_amount"])
    
    #writing records into the file
    for pid,info in patient_dict.items():
       
        #checking if the payment is paid
        flag=any(r["patient_id"]==pid and r["payment_status"]!="Paid" for r in data)
        if flag:
            str="Yes"
        else :
            str="No"
        #format for writing into the file
        writer.writerow({
            "patient_id":pid,
            "name":info["name"],
            "total_visits":info["total_visits"],
            "total_billed":info["total_billed"],
            "has_pending_payments": str
        })
print(f"Total rows skipped during processing: {skips}")

#Sample output
# Field Missing P003
# Field Missing 
# Not a float P005
# Not a float P016
# Field Missing P023
# Not a float P029
# Not a float P040
# Extra field in row P052
# Not a float P016
# Total rows skipped during processing: 9


