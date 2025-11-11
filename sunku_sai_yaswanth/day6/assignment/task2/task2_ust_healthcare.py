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

# Adjust the list of required fields to include any necessary fields
required_fields = ['patient_id', 'name', 'visit_date', 'billed_amount', 'payment_status', 'follow_up_required']

pending_rows = []
patient_summary = {}
count = {"total": 0, "processed": 0, "skipped": 0}  

with open("ust_healthcare_visits (1).csv", mode='r', newline='') as file:
    csv_dict_reader = csv.DictReader(file)
    fieldnames = csv_dict_reader.fieldnames  

    for row in csv_dict_reader:
        count["total"] += 1  # Increment total rows each time a row is read

        # Skip missing required fields (check if the fields are present and non-empty)
        if not all(row.get(field) and row[field].strip() for field in required_fields):
            print(f"Skipping row due to missing required fields: {row}")
            count["skipped"] += 1  
            continue

        # Validate billed_amount
        billed_str = row['billed_amount'].strip()
        try:
            billed_amount = float(billed_str)
        except ValueError:
            print(f"Skipping row due to invalid billed_amount: {row}")
            count["skipped"] += 1  
            continue

        # Trim whitespace for all fields and check that value is a string
        row = {key: (value.strip() if isinstance(value, str) else value) for key, value in row.items()}

        # Normalize fields
        row['payment_status'] = row['payment_status'].title()
        row['follow_up_required'] = 'Yes' if row.get('follow_up_required', '').strip().lower() == 'yes' else 'No'

        # Print cleaned row
        print(f"{row['patient_id']}, {row['name']}, {row['visit_date']}, {billed_amount}, {row['payment_status']}")

        # Track pending payments
        if row['payment_status'] != 'Paid':
            pending_rows.append(row)

        # Build patient summary
        pid = row['patient_id']
        if pid not in patient_summary:
            patient_summary[pid] = {'name': row['name'],'total_visits': 0,
                'total_billed': 0.0,'has_pending': False}

        patient_summary[pid]['total_visits'] += 1
        patient_summary[pid]['total_billed'] += billed_amount
        if row['payment_status'] != 'Paid':
            patient_summary[pid]['has_pending'] = True

        count["processed"] += 1  

# Write pending payments to CSV
with open("pending_payments.csv", mode='w', newline='') as file1:
    writer = csv.DictWriter(file1, fieldnames=fieldnames)
    writer.writeheader()

    valid_pending_rows = []
    for row in pending_rows:
        if all(key in fieldnames for key in row.keys()):
            valid_pending_rows.append(row)
        else:
            print(f"Skipping row due to invalid keys: {row}")

    writer.writerows(valid_pending_rows)

# Write patient summary to CSV
with open("patient_summary.csv", mode='w', newline='') as summaryfile:
    summary_fields = ['patient_id', 'name', 'total_visits', 'total_billed', 'has_pending']  # Corrected field name
    writer = csv.DictWriter(summaryfile, fieldnames=summary_fields)
    writer.writeheader()
    for pid, data in patient_summary.items():
        writer.writerow({
            'patient_id': pid,'name': data['name'],
            'total_visits': data['total_visits'],
            'total_billed': f"{data['total_billed']:.2f}",
            'has_pending': 'Yes' if data['has_pending'] else 'No'})

# Final summary report
print("\n--- Summary Report ---")
print("Total rows read:", count["total"])
print("Processed rows:", count["processed"])
print("Skipped rows:", count["skipped"])
print("Pending payments:", len(valid_pending_rows))  
print("Patient summary rows:", len(patient_summary))  



# P001, Arun Kumar, 2025-10-01, 7500.0, Paid
# P002, Riya Sharma, 02-10-2025, 12000.0, Pending
# Skipping row due to missing required fields: {'patient_id': 'P003', 'name': ' ', 'visit_date': '2025/10/02', 'department': 'Neurology', 'billed_amount': '3500.00', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No'}
# Skipping row due to missing required fields: {'patient_id': '', 'name': 'Meena Patel', 'visit_date': '2025-10-03', 'department': 'Cardiology', 'billed_amount': '2200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No'}
# Skipping row due to invalid billed_amount: {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '2025-10-03', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes'}
# P006, Neha Verma, 2025-10-04, 4800.5, Paid
# P007, Alex Johnson, 10/04/2025, 6000.0, Pending
# P008, Li Wei, 2025-10-05, 45000.0, Paid
# P009, Anita Singh, 2025-10-05, 900.0, Unpaid
# P010, Michael Brown, 2025.10.06, 1500.0, Paid
# P011, Sophia Lee, 2025-10-06, 5200.0, Pending
# P012, Rajesh Kumar, 2025-10-07, 16000.0, Paid
# P013, Olga Petrova, 07/10/2025, 4200.0, Unpaid
# P014, Diego Marquez, 2025-10-08, 7000.0, Paid
# Skipping row due to missing required fields: {'patient_id': 'P015', 'name': 'Ananya Rao', 'visit_date': '2025-10-08', 'department': 'Pediatrics', 'billed_amount': '1100.00', 'insurance_provider': 'ChildCare', 'payment_status': 'pending', 'contact': '8800044444', 'follow_up_required': ''}
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'True'}
# P017, Leila Ahmed, 2025-10-09, 600.0, Unpaid
# P018, Peter Clark, 2025-10-10, 4300.0, Pending
# P019, Maya Singh, 2025/10/10, 2100.0, Paid
# P020, Oscar Wilde, 2025-10-11, 36000.0, Paid
# P021, Lina Gomez, 2025-10-11, 2500.0, Pending
# P022, Tom Hanks, 2025-10-12, 5000.0, Unpaid
# Skipping row due to missing required fields: {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 'Endocrinology', 'billed_amount': '3200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No'}
# P024, Raj Patel, 2025-13-12, 4100.0, Pending
# P025, Emily Stone, 2025-10-13, 900.0, Paid
# P026, Victor Hugo, 2025-10-13, 9800.75, Pending
# P027, Zara Ali, 2025-10-14, 1400.0, Paid
# P028, Ken Watanabe, 2025-10-14, 22000.0, Paid
# Skipping row due to invalid billed_amount: {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '2025-10-15', 'department': 'ENT', 'billed_amount': ' five thousand two hundred ', 'insurance_provider': 'MedSecure', 'payment_status': ' pending ', 'contact': '6000012222', 'follow_up_required': 'Yes'}
# P030, Mira Kapoor, 15/10/2025, 3000.0, Unpaid
# P031, Sam Wilson, 2025-10-16, 6100.0, Pending
# P032, Isha Verma, 2025-10-16, 800.0, Paid
# P033, Arjun Singh, 2025-10-17, 14500.0, Paid
# P034, Nora Bates, 2025-10-17, 1300.0, Pending
# P035, Paul Green, 2025-10-18, 5400.0, Paid
# P036, Farah Khan, 2025-10-18, 2900.0, Unpaid
# P037, Igor Petrov, 2025-10-19, 52000.0, Paid
# P038, Karen Mills, 2025-10-19, 1700.0, Pending
# P039, Yuki Tanaka, 2025-10-19, 4700.0, Paid
# Skipping row due to invalid billed_amount: {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '2025-10-20', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700035555', 'follow_up_required': 'No'}
# P041, Dev Patel, 2025-10-20, 2300.0, Paid
# P042, Sofia Loren, 2025-10-20, 18500.0, Paid
# P043, Imran Khan, 2025-10-21, 900.0, Pending
# P044, Linda Park, 2025-10-21, 3100.0, Unpaid
# P045, Noah Brown, 2025-10-21, 2000.0, Paid
# P046, Nadia Petrova, 2025-10-22, 4500.0, Pending
# P047, Oscar Diaz, 2025-10-22, 8000.0, Paid
# P048, Helena Costa, 2025-10-22, 2600.0, Pending
# P049, Manish Malhotra, 2025-10-23, 12500.0, Unpaid
# P050, Eva Green, 2025-10-23, 28000.0, Paid
# P051, Samir Das, 2025-10-23, 1900.0, Paid
# P052, Priya Menon, 2025-10-24, 2.0, Medsecure
# P053, Andrei Ivanov, 2025-10-24, 4100.0, Unpaid
# P054, Lucy Hale, 2025-10-24, 1100.0, Paid
# P055, Deepak Yadav, 2025-10-25, 7200.0, Paid
# P056, Helga Schmidt, 2025-10-25, 39000.0, Pending
# P057, Karan Johar, 2025-10-25, 4500.0, Pending
# P058, Mayra Lopez, 2025-10-26, 900.0, Paid
# P059, Daniel Craig, 2025-10-26, 3300.0, Unpaid
# P060, Ayesha Khan, 26-10-2025, 4200.0, Paid
# P061, Boris Becker, 2025-10-27, 1500.0, Pending
# P062, Grace Park, 2025-10-27, 800.0, Paid
# P063, Rajiv Menon, 2025-10-27, 23000.0, Paid
# P064, Sylvia Plath, 2025-10-28, 600.0, Pending
# P065, Marcus Aurelius, 2025-10-28, 34000.0, Unpaid
# P066, Hannah Wells, 2025-10-28, 2700.0, Paid
# P067, Victor Cruz, 2025-10-29, 6400.0, Pending
# P068, Nina Simone, 2025-10-29, 3800.0, Unpaid
# P069, Omar Sy, 2025-10-29, 5900.0, Paid
# P070, Leah Baker, 2025-10-30, 1000.0, Pending
# P071, Harish Rao, 2025-10-30, 13200.0, Paid
# P072, Sonia Kapoor, 2025-10-30, 1700.0, Pending
# P073, Neil Armstrong, 2025-10-31, 47000.0, Paid
# P074, Maya Angelou, 2025-10-31, 3300.0, Unpaid
# P075, Rajeshwari Pillai, 2025-10-31, 2900.0, Pending
# P076, Daniel Ortega, 2025-11-01, 2300.0, Paid
# P077, Linda Nguyen, 2025-11-01, 4300.0, Pending
# P078, Mark Ruffalo, 2025-11-02, 9400.0, Unpaid
# P079, Aditi Rao, 2025-11-02, 700.0, Paid
# P080, Chen Li, 2025-11-02, 3050.0, Paid
# P081, Olivia Wilde, 2025-11-03, 900.0, Pending
# P082, Pranav Joshi, 2025-11-03, 6100.0, Paid
# P083, Samanta Fox, 2025-11-03, 36000.0, Pending
# P084, Imelda Marcos, 2025-11-04, 1500.0, Paid
# P085, Diego Rivera, 2025-11-04, 15500.0, Unpaid
# P086, Aisha Siddiqui, 2025-11-05, 2400.0, Pending
# P087, Brian Cox, 2025-11-05, 1700.0, Paid
# P088, Helene Fischer, 2025-11-05, 4100.0, Pending
# P089, Anil Kapoor, 2025-11-06, 7200.0, Paid
# P090, Molly Ringwald, 2025-11-06, 1100.0, Unpaid
# P091, Yusuf Pathan, 2025-11-07, 1900.0, Pending
# P092, Nicole Kidman, 2025-11-07, 21000.0, Paid
# P093, Raj Malhotra, 2025-11-07, 2500.0, Pending
# P094, Tara Strong, 2025-11-08, 4900.0, Unpaid
# P095, Victor Hugo Jr, 2025-11-08, 29000.0, Paid
# P096, Ritika Sen, 2025-11-09, 850.0, Pending
# P097, Dominic Toretto, 2025-11-09, 6800.0, Paid
# P098, Sasha Banks, 2025-11-10, 950.0, Pending
# P099, Igor Kravitz, 2025-11-10, 5900.0, Unpaid
# P100, Ankita Sharma, 2025-11-10, 4200.0, Paid
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'True'}
# P037, Igor Petrov, 2025-10-19, 52000.0, Paid
# P026, Victor Hugo, 2025-10-13, 9800.75, Pending
# P002, Riya Sharma, 02-10-2025, 12000.0, Pending
# P049, Manish Malhotra, 2025-10-23, 12500.0, Unpaid
# P093, Raj Malhotra, 2025-11-07, 2500.0, Pending
# P065, Marcus Aurelius, 2025-10-28, 34000.0, Unpaid
# P008, Li Wei, 2025-10-05, 45000.0, Paid
# P090, Molly Ringwald, 2025-11-06, 1100.0, Unpaid
# P034, Nora Bates, 2025-10-17, 1300.0, Pending
# Skipping row due to invalid keys: {'patient_id': 'P052', 'name': 'Priya Menon', 'visit_date': '2025-10-24', 'department': 'ENT', 'billed_amount': '2', 'insurance_provider': '700.00', 'payment_status': 'Medsecure', 'contact': 'Pending', 'follow_up_required': 'No', None: ['No']}

# --- Summary Report ---
# Total rows read: 110
# Processed rows: 101
# Skipped rows: 9
# Pending payments: 55
# Patient summary rows: 92