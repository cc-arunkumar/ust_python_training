# UST Healthcare (CSV Read / Write)


import csv

# 1. Read ust_healthcare_visits.csv with csv.DictReader .

with open("ust_healthcare_visits.csv","r") as file:
    print("Data Present in ust healthcare:")
    
    # Create A DictWriter object
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row)
            
# 2. Basic validation / normalization:
# Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any
# missing → skip that row (and print a short message).
# Convert billed_amount to float (if conversion fails, skip row).
# Trim whitespace from string fields.
# Normalize payment_status to Title case (e.g., "pending" → "Pending" ).
# Normalize follow_up_required to "Yes" or "No" (treat empty as "No" ).

# Creating count 
count = {
    "skipped": 0,  
    "total": 0,   
    "processed": 0 
}

# Creating new_data list for successfully processed rows
new_data = []

# Define expected headers for the CSV files
expected_headers = ["patient_id","name","visit_date","billed_amount","payment_status"]

# Open a csv file in read mode
with open("ust_healthcare_visits.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    field_header=csv_reader.fieldnames
    
    for row in csv_reader:
        count["total"] += 1

        row = {key: val.strip() if isinstance(val, str) else val for key, val in row.items()}
        
        flag = False
        
        for field in expected_headers:
            if not row.get(field) or len(row)!=len(field_header):  
                print(f"Skipping row {count['total']} due to missing field: {field}")
                
                flag = True 
                break
        
        if flag:
            count["skipped"] += 1  
            continue  
        
        try:
                      
            row['payment_status'] = row['payment_status'].title()  
            row['follow_up_required'] = 'Yes' if row.get('follow_up_required') else 'No'
            row['billed_amount'] = float(row['billed_amount'].replace('₹', '').replace(',', ''))
            new_data.append(row)
            count["processed"] += 1 
        except ValueError:
            print(f"Skipping row {count['total']} due to invalid 'billed_amount' value: {row['billed_amount']}")
            count["skipped"] += 1  
            continue  
                       
print(f"Total rows: {count['total']}")
print(f"processed rows: {count['processed']}")
print(f"skipped rows: {count['skipped']}")

# 3. Create outputs:
# pending_payments.csv : all cleaned columns for rows where payment_status != "Paid" .
# patient_summary.csv : aggregated per patient_id with columns:
# patient_id, name, total_visits, total_billed, has_pending_payment
# total_billed formatted with 2 decimals (e.g., 7500.00 ).
# has_pending_payment = "Yes" if any visit for that patient is not Paid;
# otherwise "No" .

clean_data = [row for row in new_data if row['payment_status'] != "Paid"]

header = [
    'patient_id', 'name', 'visit_date', 'billed_amount', 
    'payment_status', 'contact', 'follow_up_required', 
    'department', 'insurance_provider'
]
           
with open("pending_payments.csv","w",newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()  
    writer.writerows(clean_data)
    
# Creating empty data dictionary
data={}

for val in new_data:
    patient_id=val["patient_id"]
    billed_amount=float(val["billed_amount"])
    if patient_id not in data:
        data[patient_id] = {
            "name": val["name"],
            "total_visits": 0,
            "total_billed": 0.0,
            "has_pending_payment": "No"
        }
        
    data[patient_id]["total_visits"]+=1
    data[patient_id]["total_billed"]+=billed_amount
    if val["payment_status"] !="Paid":
        data[patient_id]["has_pending_payment"]="Yes"
   
        
# Create or open a csv file in write mode
with open("patient_summary.csv","w",newline='') as file:
    header=["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]
    writer=csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    for patient_id,val in data.items():
        val["total_billed"]=f"{val["total_billed"]:.2f}"
    
        row={"patient_id":patient_id,**val}
        writer.writerow(row)

# 4. Console summary: print counts: processed rows, skipped rows, rows in each
# output.
# Data Present in ust healthcare:
# {'patient_id': 'P001', 'name': ' Arun Kumar ', 'visit_date': '2025-10-01', 'department': 'Cardiology', 'billed_amount': '7500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '9810012345', 'follow_up_required': 'Yes'}
# {'patient_id': 'P002', 'name': 'Riya Sharma', 'visit_date': '02-10-2025', 'department': 'Orthopedics', 'billed_amount': '12000.00 ', 'insurance_provider': 'HealthPlus', 'payment_status': ' pending ', 'contact': '9810098765', 'follow_up_required': 'No'}
# {'patient_id': 'P003', 'name': ' ', 'visit_date': '2025/10/02', 'department': 'Neurology', 'billed_amount': '3500.00', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No'}
# {'patient_id': '', 'name': 'Meena Patel', 'visit_date': '2025-10-03', 'department': 'Cardiology', 'billed_amount': '2200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No'}
# {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '2025-10-03', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes'}
# {'patient_id': 'P006', 'name': 'Neha Verma', 'visit_date': '2025-10-04', 'department': 'ENT', 'billed_amount': '4800.50', 'insurance_provider': 'MedSecure', 'payment_status': 'PAID', 'contact': '9600001111', 'follow_up_required': 'No'}
# {'patient_id': 'P007', 'name': 'Alex Johnson', 'visit_date': '10/04/2025', 'department': 'Neurology', 'billed_amount': '6000.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Pending', 'contact': '7000005555', 'follow_up_required': 'Y'}
# {'patient_id': 'P008', 'name': 'Li Wei', 'visit_date': '2025-10-05', 'department': 'Oncology', 'billed_amount': '45000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'paid ', 'contact': '6000012345', 'follow_up_required': 'Yes'}
# {'patient_id': 'P009', 'name': 'Anita Singh', 'visit_date': '2025-10-05', 'department': 'General Medicine', 'billed_amount': '900.00', 'insurance_provider': '', 'payment_status': 'unPaid', 'contact': ' 8800099999 ', 'follow_up_required': 'n'}
# {'patient_id': 'P010', 'name': 'Michael Brown', 'visit_date': '2025.10.06', 'department': 'Pediatrics', 'billed_amount': '1500.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Paid', 'contact': '7700012345', 'follow_up_required': 'No'}
# {'patient_id': 'P011', 'name': 'Sophia Lee', 'visit_date': '2025-10-06', 'department': 'Cardiology', 'billed_amount': '5200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700011111', 'follow_up_required': 'YES'}
# {'patient_id': 'P012', 'name': 'Rajesh Kumar', 'visit_date': '2025-10-07', 'department': 'General Medicine', 'billed_amount': '16000.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '7700012222', 'follow_up_required': '1'}
# {'patient_id': 'P013', 'name': 'Olga Petrova', 'visit_date': '07/10/2025', 'department': 'Endocrinology', 'billed_amount': '4200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Unpaid', 'contact': '7700013333', 'follow_up_required': 'False'}
# {'patient_id': 'P014', 'name': 'Diego Marquez', 'visit_date': '2025-10-08', 'department': 'Orthopedics', 'billed_amount': '7000.00', 'insurance_provider': 'HealthPlus', 'payment_status': ' PAID', 'contact': '8800066666', 'follow_up_required': 'No'}
# {'patient_id': 'P015', 'name': 'Ananya Rao', 'visit_date': '2025-10-08', 'department': 'Pediatrics', 'billed_amount': '1100.00', 'insurance_provider': 'ChildCare', 'payment_status': 'pending', 'contact': '8800044444', 'follow_up_required': ''}
# {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'True'}
# {'patient_id': 'P017', 'name': 'Leila Ahmed', 'visit_date': '2025-10-09', 'department': 'Dermatology', 'billed_amount': '600.00', 'insurance_provider': 'DermiCare', 'payment_status': 'unpaid', 'contact': '98100-22233', 'follow_up_required': 'yes'}
# {'patient_id': 'P018', 'name': 'Peter Clark', 'visit_date': '2025-10-10', 'department': 'Neurology', 'billed_amount': '4300.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Pending', 'contact': '98 000 33344', 'follow_up_required': 'Yse'}
# {'patient_id': 'P019', 'name': 'Maya Singh', 'visit_date': '2025/10/10', 'department': 'General Medicine', 'billed_amount': '2100.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'paid', 'contact': '9990012345', 'follow_up_required': 'no'}
# {'patient_id': 'P020', 'name': 'Oscar Wilde', 'visit_date': '2025-10-11', 'department': 'Oncology', 'billed_amount': '36000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Paid', 'contact': '7700098888', 'follow_up_required': '0'}
# {'patient_id': 'P021', 'name': 'Lina Gomez', 'visit_date': '2025-10-11', 'department': 'ENT', 'billed_amount': '2500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700097777', 'follow_up_required': '1'}
# {'patient_id': 'P022', 'name': 'Tom Hanks', 'visit_date': '2025-10-12', 'department': 'Neurology', 'billed_amount': '5000.00', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800088888', 'follow_up_required': 'No'}
# {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 'Endocrinology', 'billed_amount': '3200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No'}
# {'patient_id': 'P024', 'name': 'Raj Patel', 'visit_date': '2025-13-12', 'department': 'Orthopedics', 'billed_amount': '4100.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'PENDING', 'contact': ' +91-77 000 33333 ', 'follow_up_required': 'Yes'}
# {'patient_id': 'P025', 'name': 'Emily Stone', 'visit_date': '2025-10-13', 'department': 'Pediatrics', 'billed_amount': '900.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Paid', 'contact': '7000011111', 'follow_up_required': 'No'}
# {'patient_id': 'P026', 'name': 'Victor Hugo', 'visit_date': '2025-10-13', 'department': 'Cardiology', 'billed_amount': '9800.75', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700044444', 'follow_up_required': 'Yes'}
# {'patient_id': 'P027', 'name': 'Zara Ali', 'visit_date': '2025-10-14', 'department': 'General Medicine', 'billed_amount': '1400.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'PAID', 'contact': '8800055555', 'follow_up_required': 'No'}
# {'patient_id': 'P028', 'name': 'Ken Watanabe', 'visit_date': '2025-10-14', 'department': 'Oncology', 'billed_amount': '22000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Paid', 'contact': '60000-22222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '2025-10-15', 'department': 'ENT', 'billed_amount': ' five thousand two hundred ', 'insurance_provider': 'MedSecure', 'payment_status': ' pending ', 'contact': '6000012222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P030', 'name': 'Mira Kapoor', 'visit_date': '15/10/2025', 'department': 'Endocrinology', 'billed_amount': '3000.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Unpaid', 'contact': '7700066666', 'follow_up_required': 'No'}
# {'patient_id': 'P031', 'name': 'Sam Wilson', 'visit_date': '2025-10-16', 'department': 'Neurology', 'billed_amount': '6100.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'pending', 'contact': '8800022222', 'follow_up_required': 'yes'}
# {'patient_id': 'P032', 'name': 'Isha Verma', 'visit_date': '2025-10-16', 'department': 'General Medicine', 'billed_amount': '800.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '9900099999', 'follow_up_required': 'no'}
# {'patient_id': 'P033', 'name': 'Arjun Singh', 'visit_date': '2025-10-17', 'department': 'Cardiology', 'billed_amount': '14500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '98100 77788', 'follow_up_required': 'Yes'}
# {'patient_id': 'P034', 'name': 'Nora Bates', 'visit_date': '2025-10-17', 'department': 'Pediatrics', 'billed_amount': '1300.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Pending', 'contact': '7700077777', 'follow_up_required': 'No'}
# {'patient_id': 'P035', 'name': 'Paul Green', 'visit_date': '2025-10-18', 'department': 'Orthopedics', 'billed_amount': '5400.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '8800012345', 'follow_up_required': 'No'}
# {'patient_id': 'P036', 'name': 'Farah Khan', 'visit_date': '2025-10-18', 'department': 'ENT', 'billed_amount': '2900.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Unpaid', 'contact': '7700088888', 'follow_up_required': 'yes'}
# {'patient_id': 'P037', 'name': 'Igor Petrov', 'visit_date': '2025-10-19', 'department': 'Oncology', 'billed_amount': '52000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'PAID', 'contact': '7700090000', 'follow_up_required': 'YES'}
# {'patient_id': 'P038', 'name': 'Karen Mills', 'visit_date': '2025-10-19', 'department': 'General Medicine', 'billed_amount': '1700.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '7000023334', 'follow_up_required': 'no'}
# {'patient_id': 'P039', 'name': 'Yuki Tanaka', 'visit_date': '2025-10-19', 'department': 'Neurology', 'billed_amount': '4700.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Paid', 'contact': '6000034444', 'follow_up_required': 'No'}
# {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '2025-10-20', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700035555', 'follow_up_required': 'No'}
# {'patient_id': 'P041', 'name': 'Dev Patel', 'visit_date': '2025-10-20', 'department': 'Orthopedics', 'billed_amount': '2300.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'paid', 'contact': '98100-11122', 'follow_up_required': 'no'}
# {'patient_id': 'P042', 'name': 'Sofia Loren', 'visit_date': '2025-10-20', 'department': 'Cardiology', 'billed_amount': '18500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'PAID', 'contact': '7700001112', 'follow_up_required': 'Yes'}
# {'patient_id': 'P043', 'name': 'Imran Khan', 'visit_date': '2025-10-21', 'department': 'General Medicine', 'billed_amount': '900.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '8800077777', 'follow_up_required': 'No'}
# {'patient_id': 'P044', 'name': 'Linda Park', 'visit_date': '2025-10-21', 'department': 'ENT', 'billed_amount': '3100.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Unpaid', 'contact': '7000066666', 'follow_up_required': 'yes'}
# {'patient_id': 'P045', 'name': 'Noah Brown', 'visit_date': '2025-10-21', 'department': 'Pediatrics', 'billed_amount': '2000.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Paid', 'contact': '7700047777', 'follow_up_required': '0'}
# {'patient_id': 'P046', 'name': 'Nadia Petrova', 'visit_date': '2025-10-22', 'department': 'Endocrinology', 'billed_amount': '4500.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700048888', 'follow_up_required': 'Y'}
# {'patient_id': 'P047', 'name': 'Oscar Diaz', 'visit_date': '2025-10-22', 'department': 'Orthopedics', 'billed_amount': '8000.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '8800031111', 'follow_up_required': 'Yes'}
# {'patient_id': 'P048', 'name': 'Helena Costa', 'visit_date': '2025-10-22', 'department': 'Neurology', 'billed_amount': '2600.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Pending', 'contact': '7700023333', 'follow_up_required': 'No'}
# {'patient_id': 'P049', 'name': 'Manish Malhotra', 'visit_date': '2025-10-23', 'department': 'Cardiology', 'billed_amount': '12500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Unpaid', 'contact': '9900091111', 'follow_up_required': 'Yes'}
# {'patient_id': 'P050', 'name': 'Eva Green', 'visit_date': '2025-10-23', 'department': 'Oncology', 'billed_amount': '28000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Paid', 'contact': '7700055555', 'follow_up_required': 'Yes'}
# {'patient_id': 'P051', 'name': 'Samir Das', 'visit_date': '2025-10-23', 'department': 'General Medicine', 'billed_amount': '1900.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '9810022222', 'follow_up_required': 'no'}
# {'patient_id': 'P052', 'name': 'Priya Menon', 'visit_date': '2025-10-24', 'department': 'ENT', 'billed_amount': '2', 'insurance_provider': '700.00', 'payment_status': 'MedSecure', 'contact': 'Pending', 'follow_up_required': '7700061111', None: ['No']}
# {'patient_id': 'P053', 'name': 'Andrei Ivanov', 'visit_date': '2025-10-24', 'department': 'Neurology', 'billed_amount': '4100.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Unpaid', 'contact': '7700062222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P054', 'name': 'Lucy Hale', 'visit_date': '2025-10-24', 'department': 'Pediatrics', 'billed_amount': '1100.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Paid', 'contact': '7000033333', 'follow_up_required': 'No'}
# {'patient_id': 'P055', 'name': 'Deepak Yadav', 'visit_date': '2025-10-25', 'department': 'Orthopedics', 'billed_amount': '7200.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '8800023333', 'follow_up_required': 'Yes'}
# {'patient_id': 'P056', 'name': 'Helga Schmidt', 'visit_date': '2025-10-25', 'department': 'Oncology', 'billed_amount': '39000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'PENDING', 'contact': '6000044444', 'follow_up_required': 'Yes'}
# {'patient_id': 'P057', 'name': 'Karan Johar', 'visit_date': '2025-10-25', 'department': 'Cardiology', 'billed_amount': '4500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'pending', 'contact': '7700081111', 'follow_up_required': 'no'}
# {'patient_id': 'P058', 'name': 'Mayra Lopez', 'visit_date': '2025-10-26', 'department': 'General Medicine', 'billed_amount': '900.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'PAID', 'contact': '7700082222', 'follow_up_required': 'No'}
# {'patient_id': 'P059', 'name': 'Daniel Craig', 'visit_date': '2025-10-26', 'department': 'ENT', 'billed_amount': '3300.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Unpaid', 'contact': '7700093333', 'follow_up_required': 'Y'}
# {'patient_id': 'P060', 'name': 'Ayesha Khan', 'visit_date': '26-10-2025', 'department': 'Endocrinology', 'billed_amount': '4200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'paid', 'contact': '7700094444', 'follow_up_required': 'No'}
# {'patient_id': 'P061', 'name': 'Boris Becker', 'visit_date': '2025-10-27', 'department': 'Neurology', 'billed_amount': '1500.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Pending', 'contact': '8800045555', 'follow_up_required': 'No'}
# {'patient_id': 'P062', 'name': 'Grace Park', 'visit_date': '2025-10-27', 'department': 'Pediatrics', 'billed_amount': '800.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Paid', 'contact': '7000056666', 'follow_up_required': 'No'}
# {'patient_id': 'P063', 'name': 'Rajiv Menon', 'visit_date': '2025-10-27', 'department': 'Cardiology', 'billed_amount': '23000.00', 'insurance_provider': 'MedSecure', 'payment_status': 'PAID', 'contact': '9810033333', 'follow_up_required': 'Yes'}
# {'patient_id': 'P064', 'name': 'Sylvia Plath', 'visit_date': '2025-10-28', 'department': 'General Medicine', 'billed_amount': '600.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '7700018888', 'follow_up_required': 'No'}
# {'patient_id': 'P065', 'name': 'Marcus Aurelius', 'visit_date': '2025-10-28', 'department': 'Oncology', 'billed_amount': '34000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Unpaid', 'contact': '9990022222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P066', 'name': 'Hannah Wells', 'visit_date': '2025-10-28', 'department': 'ENT', 'billed_amount': '2700.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700024444', 'follow_up_required': 'No'}
# {'patient_id': 'P067', 'name': 'Victor Cruz', 'visit_date': '2025-10-29', 'department': 'Orthopedics', 'billed_amount': '6400.00', 'insurance_provider': 'HealthPlus', 'payment_status': ' pending ', 'contact': '7000077777', 'follow_up_required': 'YES'}
# {'patient_id': 'P068', 'name': 'Nina Simone', 'visit_date': '2025-10-29', 'department': 'Endocrinology', 'billed_amount': '3800.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Unpaid', 'contact': '7700034444', 'follow_up_required': 'No'}
# {'patient_id': 'P069', 'name': 'Omar Sy', 'visit_date': '2025-10-29', 'department': 'Neurology', 'billed_amount': '5900.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'PAID', 'contact': '8800056666', 'follow_up_required': 'Yes'}
# {'patient_id': 'P070', 'name': 'Leah Baker', 'visit_date': '2025-10-30', 'department': 'Pediatrics', 'billed_amount': '1000.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Pending', 'contact': '7700035556', 'follow_up_required': 'No'}
# {'patient_id': 'P071', 'name': 'Harish Rao', 'visit_date': '2025-10-30', 'department': 'Cardiology', 'billed_amount': '13200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '9810055555', 'follow_up_required': 'Yes'}
# {'patient_id': 'P072', 'name': 'Sonia Kapoor', 'visit_date': '2025-10-30', 'department': 'General Medicine', 'billed_amount': '1700.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '7700067777', 'follow_up_required': 'No'}
# {'patient_id': 'P073', 'name': 'Neil Armstrong', 'visit_date': '2025-10-31', 'department': 'Oncology', 'billed_amount': '47000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Paid', 'contact': '7000088888', 'follow_up_required': 'Yes'}
# {'patient_id': 'P074', 'name': 'Maya Angelou', 'visit_date': '2025-10-31', 'department': 'Neurology', 'billed_amount': '3300.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'unpaid', 'contact': '7700091112', 'follow_up_required': 'No'}
# {'patient_id': 'P075', 'name': 'Rajeshwari Pillai', 'visit_date': '2025-10-31', 'department': 'ENT', 'billed_amount': '2900.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '8800067777', 'follow_up_required': 'Yes'}
# {'patient_id': 'P076', 'name': 'Daniel Ortega', 'visit_date': '2025-11-01', 'department': 'Orthopedics', 'billed_amount': '2300.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '7700092222', 'follow_up_required': 'No'}
# {'patient_id': 'P077', 'name': 'Linda Nguyen', 'visit_date': '2025-11-01', 'department': 'Endocrinology', 'billed_amount': '4300.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '6000093333', 'follow_up_required': 'No'}
# {'patient_id': 'P078', 'name': 'Mark Ruffalo', 'visit_date': '2025-11-02', 'department': 'Cardiology', 'billed_amount': '9400.00', 'insurance_provider': 'MedSecure', 'payment_status': 'unpaid', 'contact': '7700083333', 'follow_up_required': 'yes'}
# {'patient_id': 'P079', 'name': 'Aditi Rao', 'visit_date': '2025-11-02', 'department': 'General Medicine', 'billed_amount': '700.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '7700084444', 'follow_up_required': 'No'}
# {'patient_id': 'P080', 'name': 'Chen Li', 'visit_date': '2025-11-02', 'department': 'ENT', 'billed_amount': '3050.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '6000094444', 'follow_up_required': 'No'}
# {'patient_id': 'P081', 'name': 'Olivia Wilde', 'visit_date': '2025-11-03', 'department': 'Pediatrics', 'billed_amount': '900.00', 'insurance_provider': 'ChildCare', 'payment_status': ' pending ', 'contact': '7700085555', 'follow_up_required': 'No'}
# {'patient_id': 'P082', 'name': 'Pranav Joshi', 'visit_date': '2025-11-03', 'department': 'Neurology', 'billed_amount': '6100.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Paid', 'contact': '9810066666', 'follow_up_required': 'Yes'}
# {'patient_id': 'P083', 'name': 'Samanta Fox', 'visit_date': '2025-11-03', 'department': 'Oncology', 'billed_amount': '36000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Pending', 'contact': '7700079999', 'follow_up_required': 'Yes'}
# {'patient_id': 'P084', 'name': 'Imelda Marcos', 'visit_date': '2025-11-04', 'department': 'General Medicine', 'billed_amount': '1500.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '7700069999', 'follow_up_required': 'No'}
# {'patient_id': 'P085', 'name': 'Diego Rivera', 'visit_date': '2025-11-04', 'department': 'Cardiology', 'billed_amount': '15500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'unpaid', 'contact': '8800007777', 'follow_up_required': 'Yes'}
# {'patient_id': 'P086', 'name': 'Aisha Siddiqui', 'visit_date': '2025-11-05', 'department': 'ENT', 'billed_amount': '2400.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '9810077777', 'follow_up_required': 'No'}
# {'patient_id': 'P087', 'name': 'Brian Cox', 'visit_date': '2025-11-05', 'department': 'Neurology', 'billed_amount': '1700.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Paid', 'contact': '7700059999', 'follow_up_required': 'No'}
# {'patient_id': 'P088', 'name': 'Helene Fischer', 'visit_date': '2025-11-05', 'department': 'Endocrinology', 'billed_amount': '4100.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7000095555', 'follow_up_required': 'NO'}
# {'patient_id': 'P089', 'name': 'Anil Kapoor', 'visit_date': '2025-11-06', 'department': 'Orthopedics', 'billed_amount': '7200.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'Paid', 'contact': '9900094444', 'follow_up_required': 'Yes'}
# {'patient_id': 'P090', 'name': 'Molly Ringwald', 'visit_date': '2025-11-06', 'department': 'Pediatrics', 'billed_amount': '1100.00', 'insurance_provider': 'ChildCare', 'payment_status': 'UnPaid', 'contact': '7700041111', 'follow_up_required': 'No'}
# {'patient_id': 'P091', 'name': 'Yusuf Pathan', 'visit_date': '2025-11-07', 'department': 'General Medicine', 'billed_amount': '1900.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'pending', 'contact': '9810088888', 'follow_up_required': 'yes'}
# {'patient_id': 'P092', 'name': 'Nicole Kidman', 'visit_date': '2025-11-07', 'department': 'Cardiology', 'billed_amount': '21000.00', 'insurance_provider': 'MedSecure', 'payment_status': 'PAID', 'contact': '7700021111', 'follow_up_required': 'Yes'}
# {'patient_id': 'P093', 'name': 'Raj Malhotra', 'visit_date': '2025-11-07', 'department': 'ENT', 'billed_amount': '2500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700010001', 'follow_up_required': 'No'}
# {'patient_id': 'P094', 'name': 'Tara Strong', 'visit_date': '2025-11-08', 'department': 'Neurology', 'billed_amount': '4900.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'Unpaid', 'contact': '7000019999', 'follow_up_required': 'Yes'}
# {'patient_id': 'P095', 'name': 'Victor Hugo Jr', 'visit_date': '2025-11-08', 'department': 'Oncology', 'billed_amount': '29000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'paid', 'contact': '7700002222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P096', 'name': 'Ritika Sen', 'visit_date': '2025-11-09', 'department': 'General Medicine', 'billed_amount': '850.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'pending', 'contact': '7700003333', 'follow_up_required': 'No'}
# {'patient_id': 'P097', 'name': 'Dominic Toretto', 'visit_date': '2025-11-09', 'department': 'Orthopedics', 'billed_amount': '6800.00', 'insurance_provider': 'HealthPlus', 'payment_status': 'PAID', 'contact': '8800090000', 'follow_up_required': 'Yes'}
# {'patient_id': 'P098', 'name': 'Sasha Banks', 'visit_date': '2025-11-10', 'department': 'Pediatrics', 'billed_amount': '950.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Pending', 'contact': '7700091113', 'follow_up_required': 'No'}
# {'patient_id': 'P099', 'name': 'Igor Kravitz', 'visit_date': '2025-11-10', 'department': 'Neurology', 'billed_amount': '5900.00', 'insurance_provider': 'GlobalCare', 'payment_status': 'UNPAID', 'contact': '6000015555', 'follow_up_required': 'Yes'}
# {'patient_id': 'P100', 'name': 'Ankita Sharma', 'visit_date': '2025-11-10', 'department': 'Endocrinology', 'billed_amount': '4200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '9810090000', 'follow_up_required': 'No'}
# {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'True'}
# {'patient_id': 'P037', 'name': 'Igor Petrov', 'visit_date': '2025-10-19', 'department': 'Oncology', 'billed_amount': '52000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'PAID', 'contact': '7700090000', 'follow_up_required': 'YES'}
# {'patient_id': 'P026', 'name': 'Victor Hugo', 'visit_date': '2025-10-13', 'department': 'Cardiology', 'billed_amount': '9800.75', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700044444', 'follow_up_required': 'Yes'}
# {'patient_id': 'P002', 'name': 'Riya Sharma', 'visit_date': '02-10-2025', 'department': 'Orthopedics', 'billed_amount': '12000.00 ', 'insurance_provider': 'HealthPlus', 'payment_status': ' pending ', 'contact': '9810098765', 'follow_up_required': 'No'}
# {'patient_id': 'P049', 'name': 'Manish Malhotra', 'visit_date': '2025-10-23', 'department': 'Cardiology', 'billed_amount': '12500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Unpaid', 'contact': '9900091111', 'follow_up_required': 'Yes'}
# {'patient_id': 'P093', 'name': 'Raj Malhotra', 'visit_date': '2025-11-07', 'department': 'ENT', 'billed_amount': '2500.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '7700010001', 'follow_up_required': 'No'}
# {'patient_id': 'P065', 'name': 'Marcus Aurelius', 'visit_date': '2025-10-28', 'department': 'Oncology', 'billed_amount': '34000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'Unpaid', 'contact': '9990022222', 'follow_up_required': 'Yes'}
# {'patient_id': 'P008', 'name': 'Li Wei', 'visit_date': '2025-10-05', 'department': 'Oncology', 'billed_amount': '45000.00', 'insurance_provider': 'CancerCover', 'payment_status': 'paid ', 'contact': '6000012345', 'follow_up_required': 'Yes'}
# {'patient_id': 'P090', 'name': 'Molly Ringwald', 'visit_date': '2025-11-06', 'department': 'Pediatrics', 'billed_amount': '1100.00', 'insurance_provider': 'ChildCare', 'payment_status': 'UnPaid', 'contact': '7700041111', 'follow_up_required': 'No'}
# {'patient_id': 'P034', 'name': 'Nora Bates', 'visit_date': '2025-10-17', 'department': 'Pediatrics', 'billed_amount': '1300.00', 'insurance_provider': 'ChildCare', 'payment_status': 'Pending', 'contact': '7700077777', 'follow_up_required': 'No'}


# Skipping row 3 due to missing field: name
# Skipping row 4 due to missing field: patient_id
# Skipping row 5 due to invalid 'billed_amount' value: one thousand
# Skipping row 16 due to invalid 'billed_amount' value: ₹8200.00
# Skipping row 23 due to missing field: visit_date
# Skipping row 29 due to invalid 'billed_amount' value: five thousand two hundred
# Skipping row 40 due to invalid 'billed_amount' value: 41OO.00
# Skipping row 52 due to missing field: patient_id
# Skipping row 101 due to invalid 'billed_amount' value: ₹8200.00
# Total rows: 110
# processed rows: 101
# skipped rows: 9