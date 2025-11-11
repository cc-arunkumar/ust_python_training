#========================= UST Healthcare (CSV Read / Write)================================
from collections import defaultdict
import csv

#Step 1 : Importing the CSV and taking variables for diffrent csv files.

Input_File = "ust_healthcare_visits_.csv"
Output_File = "pending_payments.csv"
Patient_File = "patient_summary.csv"

required_feilds = [ 'patient_id' , 'name' , 'visit_date' , 'billed_amount' , 'payment_status' ]

#Step 2 : Taking some of the necessary counters and values :

processed_rows = 0
skipped_rows = 0
pending_rows = []
patient_summary = defaultdict(lambda: {
    "name": "",
    "total_visits": 0,
    "total_billed": 0.0,
    "has_pending_payment": False
})

#Step 3: Using the DictReader to read the Values of the Input File.
with open(Input_File, newline="") as infile:
    reader = csv.DictReader(infile)
    all_fields = reader.fieldnames
    for row in reader:
    #Skip the rows that have the null value :
    #Skipping the row because of extra data.
        if None in row:
            print("Skipping row (extra column found):", row)
            skipped_rows += 1
            continue
    #Skipping the row because of missing data.
        missing = [field for field in required_feilds if not row.get(field) or not row[field].strip()]
        if missing:
            print(f"Skipping row (missing required fields {missing}):", row)
            skipped_rows += 1
            continue
        
    #Try Catch Block used for checking of Value Errors in the Billing Amount.
        try:
            billed_amount = float(row["billed_amount"].strip())
        except ValueError:
            print("Skipping row (invalid billed_amount):", row)
            skipped_rows += 1
            continue
    

#Step 4 : Stripping the Values with the (,).
        patient_id = row["patient_id"]
        name = row["name"].strip()
        visit_date = row["visit_date"].strip()
        payment_status_raw = row["payment_status"].strip()
#Making the Payment status to lowercase as asked in the problem statement.

        if not payment_status_raw or payment_status_raw.lower() == "no":
            payment_status = "No"
        elif payment_status_raw.lower() in ["pending", "yes", "follow_up_required"]:
            payment_status = "Pending"
        else:
            payment_status = payment_status_raw.title()

#Step 5 : Updating the Patient Summary and adding the values in that file.
        cleaned_row = {
            "patient_id": patient_id,
            "name": name,
            "visit_date": visit_date,
            "billed_amount": f"{billed_amount:.2f}",
            "payment_status": payment_status
            
        }
        
        
        #Taking the values and adding it into the csv file.
        summary = patient_summary[patient_id]
        summary["name"] = name
        summary["total_visits"] += 1
        summary["total_billed"] += billed_amount
        if payment_status == "Pending":
            summary["has_pending_payment"] = True
        row["billed_amount"] = f"{billed_amount:.2f}"
        row[payment_status] = payment_status
        
        if payment_status != "Paid":
            pending_rows.append(cleaned_row) 
        processed_rows += 1
     
 
# Step 6 : Adding the Patients Summary and into a new file   
with open(Patient_File, "w", newline="") as outfile:
    fieldnames = ["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for pid, summary in patient_summary.items():
        writer.writerow({
            "patient_id": pid,
            "name": summary["name"],
            "total_visits": summary["total_visits"],
            "total_billed": f"{summary['total_billed']:.2f}",
            "has_pending_payment": "Yes" if summary["has_pending_payment"] else "No"
        })

#Step 7 : Adding the Pending Payments into a csv file.
with open(Output_File, 'w', newline='') as output_file:
    
    writer = csv.DictWriter(output_file, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(pending_rows)


#Step 8 : Printing the Console Output.
print("<======================== Console Summary ================================>")
print("Processed rows:", processed_rows)
print("Skipped rows:", skipped_rows)
print("Rows in pending_payments.csv:", len(pending_rows))
print("Rows in patient_summary.csv:", len(patient_summary))



#Console Output:
# <======================== Console Summary ================================>
# Processed rows: 103
# Skipped rows: 7
# Rows in pending_payments.csv: 58
# Rows in patient_summary.csv: 94