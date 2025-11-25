import csv   # Import the CSV module to read and write CSV files

# Dictionary to store patient summary data
patient_data = {}

# Open the healthcare CSV file in read mode
with open('ust_healthcare.csv', mode="r") as file:
    reader = csv.reader(file)   # Create a CSV reader object
    next(reader)                # Skip the header row

    # Loop through each row in the CSV file
    for row in reader:
        patient_id = row[0]                 # First column → patient ID
        name = row[1].strip()               # Second column → patient name (remove spaces)
        billed_amount = float(row[4])       # Fifth column → billed amount (convert to float)
        payment_status = str(row[6]).strip().capitalize()  # Seventh column → payment status (normalize)

        # If patient not already in dictionary, initialize their record
        if patient_id not in patient_data:
            patient_data[patient_id] = {
                'name': name,
                'total_visits': 0,
                'total_billed': 0.0,
                # Mark payment status as YES if "Paid", otherwise NO
                'payment_status': 'YES' if payment_status == 'Paid' else 'NO'
            }

        # Increment visit count for this patient
        patient_data[patient_id]['total_visits'] += 1
        # Add billed amount to total
        patient_data[patient_id]['total_billed'] += billed_amount

        # If any visit is unpaid, mark overall payment status as NO
        if payment_status != 'Paid':
            patient_data[patient_id]['payment_status'] = 'NO'

# Write summarized patient data into a new CSV file
with open('patient_summary.csv', mode="w", newline='') as second_file:
    writer = csv.writer(second_file)
    # Define header row
    header = ['patient_id', 'name', 'total_visits', 'total_billed', 'payment_status']
    writer.writerow(header)

    # Write each patient's summary data
    for patient_id, data in patient_data.items():
        writer.writerow([
            patient_id,
            data['name'],
            data['total_visits'],
            data['total_billed'],
            data['payment_status']
        ])
        
        
# =================sample input=====================
# patient_id,name,age,gender,billed_amount,disease,payment_status
# P001,John Doe,30,M,2000,Flu,Paid
# P002,Jane Smith,25,F,1500,Cold,Unpaid
# P001,John Doe,30,M,3000,Checkup,Paid
# P003,Sam Wilson,40,M,5000,Cancer,Paid
# P002,Jane Smith,25,F,2500,Checkup,Paid


# ========================sample output====================
# patient_id,name,total_visits,total_billed,payment_status
# P001,John Doe,2,5000.0,YES
# P002,Jane Smith,2,4000.0,NO
# P003,Sam Wilson,1,5000.0,YES
