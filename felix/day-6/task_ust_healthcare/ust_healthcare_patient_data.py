# Create outputs for ust healthcare

import csv
    
    
# Reading whole file

with open("ust_healthcare_visits (1).csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 

skipped_rows = 0
processed_rows = 0
with open("ust_healthcare_visits (1).csv","r") as file:
    
    reader = csv.DictReader(file)
    next(reader)
    
    # Patients with ther important data
    print("Patients with ther important data...")
    
    for row in reader:
        # checking if any important fields are missing
        if 'patient_id' not in row or 'name' not in row or 'visit_date' not in row or 'billed_amount' not in row or 'payment_status' not in row or 'insurance_provider' not in row:
            print("Field are missing")
            continue
        else:
            print(row['patient_id'],row['name'],row['visit_date'],row['billed_amount'],row['payment_status'])

with open("ust_healthcare_visits (1).csv","r") as file:
    reader1 = csv.DictReader(file)
    next(reader1)
    for row in reader1:
        
        # for key in row:
        #     if not row[key]:
        #         # skipped_rows+=1
        #         continue
        
        # checking is fields are missing
        if not row['insurance_provider'] or row['follow_up_required'] == 0 or not row['visit_date']:
            skipped_rows += 1
            continue
        
        # chechking that if the bill amount if convertable to float
        try:
            if len(row['name'])>0 and float(row['billed_amount']):
                row['billed_amount'] = float(row['billed_amount'])
        except ValueError:
            # print("Value error")
            skipped_rows += 1
            continue
        
        # Triming whitespace
        for key in row:
            if type(row[key]) == str:
                row[key] = row[key].strip()

        
        # Normalise payment status to title case
        row['payment_status'] = row['payment_status'].capitalize()
        
        # Normalise followups
        if not row['follow_up_required']:
            row['follow_up_required'] = "No"
            
        processed_rows += 1
        
print("\n")
        
print("Skipped rows: ",skipped_rows)
print("Processed rows: ",processed_rows)

print("\n")
# opening patient data file
with open("ust_healthcare_visits.csv","r") as file:
    reader = csv.DictReader(file)
    # storing of headers
    header = reader.fieldnames
    with open("pending_payments.csv","w",newline="") as file1:
        writer = csv.DictWriter(file1,header)
        writer.writeheader()
        for row in reader:
            if row['payment_status'].title() != 'Paid':
                writer.writerow(row)

print("Pending payments data is generated...")            
# patient summery


with open("ust_healthcare_visits.csv","r") as file:
    reader = csv.DictReader(file)
    d={}
    for row in reader:
        if row["payment_status"] != 'paid':
            payment = 'Yes'
        else:
            payment = 'No'
        # print(row['patient_id'])
        if row['patient_id'] in d:
            d[row['patient_id']][1] += 1
            d[row['patient_id']][2] += row['billed_amount']
            d[row['patient_id']][3] = payment
        else:
            d[row['patient_id']] = [row['name'],1,row['billed_amount'],payment]
        # d[row['patient_id']] = [d.get(d[row['patient_id']][1],0)+1,d.get(d[row['patient_id']][2],0)+row['billed_amount'],payment]

with open("patient_summary.csv","w",newline='') as file:
    writer = csv.writer(file)
    main_list = []
    for i in d:
        list = []
        list.append(i)
        list.extend(d[i])
        main_list.append(list)
    writer.writerows(main_list)
    print("Patient summary generated successfully...")
    
# output

# ['patient_id', 'name', 'visit_date', 'department', 'billed_amount', 'insurance_provider', 'payment_status', 'contact', 'follow_up_required']
# ['P001', ' Arun Kumar ', '2025-10-01', 'Cardiology', '7500.00', 'MedSecure', 'Paid', '9810012345', 'Yes']
# ['P002', 'Riya Sharma', '02-10-2025', 'Orthopedics', '12000.00 ', 'HealthPlus', ' pending ', '9810098765', 'No']
# ['P003', ' ', '2025/10/02', 'Neurology', '3500.00', '', 'Unpaid', '8800123456', 'No']
# ['', 'Meena Patel', '2025-10-03', 'Cardiology', '2200.00', 'MedSecure', 'Paid', '7700123456', 'No']
# ['P005', 'Suresh K', '2025-10-03', 'General Medicine', 'one thousand', 'HealthPlus', 'Pending', '9900112233', 'Yes']
# ['P006', 'Neha Verma', '2025-10-04', 'ENT', '4800.50', 'MedSecure', 'PAID', '9600001111', 'No']  
# ['P007', 'Alex Johnson', '10/04/2025', 'Neurology', '6000.00', 'GlobalCare', 'Pending', '7000005555', 'Y']
# ['P008', 'Li Wei', '2025-10-05', 'Oncology', '45000.00', 'CancerCover', 'paid ', '6000012345', 'Yes']
# ['P009', 'Anita Singh', '2025-10-05', 'General Medicine', '900.00', '', 'unPaid', ' 8800099999 ', 'n']
# ['P010', 'Michael Brown', '2025.10.06', 'Pediatrics', '1500.00', 'ChildCare', 'Paid', '7700012345', 'No']
# ['P011', 'Sophia Lee', '2025-10-06', 'Cardiology', '5200.00', 'MedSecure', 'Pending', '7700011111', 'YES']
# ['P012', 'Rajesh Kumar', '2025-10-07', 'General Medicine', '16000.00', 'HealthPlus', 'Paid', '7700012222', '1']
# ['P013', 'Olga Petrova', '07/10/2025', 'Endocrinology', '4200.00', 'EndoCare', 'Unpaid', '7700013333', 'False']
# ['P014', 'Diego Marquez', '2025-10-08', 'Orthopedics', '7000.00', 'HealthPlus', ' PAID', '8800066666', 'No']
# ['P015', 'Ananya Rao', '2025-10-08', 'Pediatrics', '1100.00', 'ChildCare', 'pending', '8800044444', '']
# ['P016', 'Sunil Sharma', '2025-10-09', 'Cardiology', 'â‚¹8200.00', 'MedSecure', 'Paid', '+91-98 100 12345', 'True']
# ['P017', 'Leila Ahmed', '2025-10-09', 'Dermatology', '600.00', 'DermiCare', 'unpaid', '98100-22233', 'yes']
# ['P018', 'Peter Clark', '2025-10-10', 'Neurology', '4300.00', 'GlobalCare', 'Pending', '98 000 33344', 'Yse']
# ['P019', 'Maya Singh', '2025/10/10', 'General Medicine', '2100.00', 'HealthPlus', 'paid', '9990012345', 'no']
# ['P020', 'Oscar Wilde', '2025-10-11', 'Oncology', '36000.00', 'CancerCover', 'Paid', '7700098888', '0']
# ['P021', 'Lina Gomez', '2025-10-11', 'ENT', '2500.00', 'MedSecure', 'Pending', '7700097777', '1']['P022', 'Tom Hanks', '2025-10-12', 'Neurology', '5000.00', '', 'Unpaid', '8800088888', 'No']    
# ['P023', 'Sana Khan', '', 'Endocrinology', '3200.00', 'EndoCare', 'Paid', '7700022222', 'No']    
# ['P024', 'Raj Patel', '2025-13-12', 'Orthopedics', '4100.00', 'HealthPlus', 'PENDING', ' +91-77 000 33333 ', 'Yes']
# ['P025', 'Emily Stone', '2025-10-13', 'Pediatrics', '900.00', 'ChildCare', 'Paid', '7000011111', 
# 'No']
# ['P026', 'Victor Hugo', '2025-10-13', 'Cardiology', '9800.75', 'MedSecure', 'Pending', '7700044444', 'Yes']
# ['P027', 'Zara Ali', '2025-10-14', 'General Medicine', '1400.00', 'HealthPlus', 'PAID', '8800055555', 'No']
# ['P028', 'Ken Watanabe', '2025-10-14', 'Oncology', '22000.00', 'CancerCover', 'Paid', '60000-22222', 'Yes']
# ['P029', 'Liu Chen', '2025-10-15', 'ENT', ' five thousand two hundred ', 'MedSecure', ' pending ', '6000012222', 'Yes']
# ['P030', 'Mira Kapoor', '15/10/2025', 'Endocrinology', '3000.00', 'EndoCare', 'Unpaid', '7700066666', 'No']
# ['P031', 'Sam Wilson', '2025-10-16', 'Neurology', '6100.00', 'GlobalCare', 'pending', '8800022222', 'yes']
# ['P032', 'Isha Verma', '2025-10-16', 'General Medicine', '800.00', 'HealthPlus', 'Paid', '9900099999', 'no']
# ['P033', 'Arjun Singh', '2025-10-17', 'Cardiology', '14500.00', 'MedSecure', 'Paid', '98100 77788', 'Yes']
# ['P034', 'Nora Bates', '2025-10-17', 'Pediatrics', '1300.00', 'ChildCare', 'Pending', '7700077777', 'No']
# ['P035', 'Paul Green', '2025-10-18', 'Orthopedics', '5400.00', 'HealthPlus', 'Paid', '8800012345', 'No']
# ['P036', 'Farah Khan', '2025-10-18', 'ENT', '2900.00', 'MedSecure', 'Unpaid', '7700088888', 'yes']
# ['P037', 'Igor Petrov', '2025-10-19', 'Oncology', '52000.00', 'CancerCover', 'PAID', '7700090000', 'YES']
# ['P038', 'Karen Mills', '2025-10-19', 'General Medicine', '1700.00', 'HealthPlus', 'Pending', '7000023334', 'no']
# ['P039', 'Yuki Tanaka', '2025-10-19', 'Neurology', '4700.00', 'GlobalCare', 'Paid', '6000034444', 'No']
# ['P040', 'Rachel Adams', '2025-10-20', 'Endocrinology', '41OO.00', 'EndoCare', 'Pending', '7700035555', 'No']
# ['P041', 'Dev Patel', '2025-10-20', 'Orthopedics', '2300.00', 'HealthPlus', 'paid', '98100-11122', 'no']
# ['P042', 'Sofia Loren', '2025-10-20', 'Cardiology', '18500.00', 'MedSecure', 'PAID', '7700001112', 'Yes']
# ['P043', 'Imran Khan', '2025-10-21', 'General Medicine', '900.00', 'HealthPlus', 'Pending', '8800077777', 'No']
# ['P044', 'Linda Park', '2025-10-21', 'ENT', '3100.00', 'MedSecure', 'Unpaid', '7000066666', 'yes']
# ['P045', 'Noah Brown', '2025-10-21', 'Pediatrics', '2000.00', 'ChildCare', 'Paid', '7700047777', 
# '0']
# ['P046', 'Nadia Petrova', '2025-10-22', 'Endocrinology', '4500.00', 'EndoCare', 'Pending', '7700048888', 'Y']
# ['P047', 'Oscar Diaz', '2025-10-22', 'Orthopedics', '8000.00', 'HealthPlus', 'Paid', '8800031111', 'Yes']
# ['P048', 'Helena Costa', '2025-10-22', 'Neurology', '2600.00', 'GlobalCare', 'Pending', '7700023333', 'No']
# ['P049', 'Manish Malhotra', '2025-10-23', 'Cardiology', '12500.00', 'MedSecure', 'Unpaid', '9900091111', 'Yes']
# ['P050', 'Eva Green', '2025-10-23', 'Oncology', '28000.00', 'CancerCover', 'Paid', '7700055555', 
# 'Yes']
# ['P051', 'Samir Das', '2025-10-23', 'General Medicine', '1900.00', 'HealthPlus', 'Paid', '9810022222', 'no']
# ['P052', 'Priya Menon', '2025-10-24', 'ENT', '2', '700.00', 'MedSecure', 'Pending', '7700061111', 'No']
# ['P053', 'Andrei Ivanov', '2025-10-24', 'Neurology', '4100.00', 'GlobalCare', 'Unpaid', '7700062222', 'Yes']
# ['P054', 'Lucy Hale', '2025-10-24', 'Pediatrics', '1100.00', 'ChildCare', 'Paid', '7000033333', 'No']
# ['P055', 'Deepak Yadav', '2025-10-25', 'Orthopedics', '7200.00', 'HealthPlus', 'Paid', '8800023333', 'Yes']
# ['P056', 'Helga Schmidt', '2025-10-25', 'Oncology', '39000.00', 'CancerCover', 'PENDING', '6000044444', 'Yes']
# ['P057', 'Karan Johar', '2025-10-25', 'Cardiology', '4500.00', 'MedSecure', 'pending', '7700081111', 'no']
# ['P058', 'Mayra Lopez', '2025-10-26', 'General Medicine', '900.00', 'HealthPlus', 'PAID', '7700082222', 'No']
# ['P059', 'Daniel Craig', '2025-10-26', 'ENT', '3300.00', 'MedSecure', 'Unpaid', '7700093333', 'Y']
# ['P060', 'Ayesha Khan', '26-10-2025', 'Endocrinology', '4200.00', 'EndoCare', 'paid', '7700094444', 'No']
# ['P061', 'Boris Becker', '2025-10-27', 'Neurology', '1500.00', 'GlobalCare', 'Pending', '8800045555', 'No']
# ['P062', 'Grace Park', '2025-10-27', 'Pediatrics', '800.00', 'ChildCare', 'Paid', '7000056666', 'No']
# ['P063', 'Rajiv Menon', '2025-10-27', 'Cardiology', '23000.00', 'MedSecure', 'PAID', '9810033333', 'Yes']
# ['P064', 'Sylvia Plath', '2025-10-28', 'General Medicine', '600.00', 'HealthPlus', 'Pending', '7700018888', 'No']
# ['P065', 'Marcus Aurelius', '2025-10-28', 'Oncology', '34000.00', 'CancerCover', 'Unpaid', '9990022222', 'Yes']
# ['P066', 'Hannah Wells', '2025-10-28', 'ENT', '2700.00', 'MedSecure', 'Paid', '7700024444', 'No']['P067', 'Victor Cruz', '2025-10-29', 'Orthopedics', '6400.00', 'HealthPlus', ' pending ', '7000077777', 'YES']
# ['P068', 'Nina Simone', '2025-10-29', 'Endocrinology', '3800.00', 'EndoCare', 'Unpaid', '7700034444', 'No']
# ['P069', 'Omar Sy', '2025-10-29', 'Neurology', '5900.00', 'GlobalCare', 'PAID', '8800056666', 'Yes']
# ['P070', 'Leah Baker', '2025-10-30', 'Pediatrics', '1000.00', 'ChildCare', 'Pending', '7700035556', 'No']
# ['P071', 'Harish Rao', '2025-10-30', 'Cardiology', '13200.00', 'MedSecure', 'Paid', '9810055555', 'Yes']
# ['P072', 'Sonia Kapoor', '2025-10-30', 'General Medicine', '1700.00', 'HealthPlus', 'Pending', '7700067777', 'No']
# ['P073', 'Neil Armstrong', '2025-10-31', 'Oncology', '47000.00', 'CancerCover', 'Paid', '7000088888', 'Yes']
# ['P074', 'Maya Angelou', '2025-10-31', 'Neurology', '3300.00', 'GlobalCare', 'unpaid', '7700091112', 'No']
# ['P075', 'Rajeshwari Pillai', '2025-10-31', 'ENT', '2900.00', 'MedSecure', 'Pending', '8800067777', 'Yes']
# ['P076', 'Daniel Ortega', '2025-11-01', 'Orthopedics', '2300.00', 'HealthPlus', 'Paid', '7700092222', 'No']
# ['P077', 'Linda Nguyen', '2025-11-01', 'Endocrinology', '4300.00', 'EndoCare', 'Pending', '6000093333', 'No']
# ['P078', 'Mark Ruffalo', '2025-11-02', 'Cardiology', '9400.00', 'MedSecure', 'unpaid', '7700083333', 'yes']
# ['P079', 'Aditi Rao', '2025-11-02', 'General Medicine', '700.00', 'HealthPlus', 'Paid', '7700084444', 'No']
# ['P080', 'Chen Li', '2025-11-02', 'ENT', '3050.00', 'MedSecure', 'Paid', '6000094444', 'No']     
# ['P081', 'Olivia Wilde', '2025-11-03', 'Pediatrics', '900.00', 'ChildCare', ' pending ', '7700085555', 'No']
# ['P082', 'Pranav Joshi', '2025-11-03', 'Neurology', '6100.00', 'GlobalCare', 'Paid', '9810066666', 'Yes']
# ['P083', 'Samanta Fox', '2025-11-03', 'Oncology', '36000.00', 'CancerCover', 'Pending', '7700079999', 'Yes']
# ['P084', 'Imelda Marcos', '2025-11-04', 'General Medicine', '1500.00', 'HealthPlus', 'Paid', '7700069999', 'No']
# ['P085', 'Diego Rivera', '2025-11-04', 'Cardiology', '15500.00', 'MedSecure', 'unpaid', '8800007777', 'Yes']
# ['P086', 'Aisha Siddiqui', '2025-11-05', 'ENT', '2400.00', 'MedSecure', 'Pending', '9810077777', 
# 'No']
# ['P087', 'Brian Cox', '2025-11-05', 'Neurology', '1700.00', 'GlobalCare', 'Paid', '7700059999', 'No']
# ['P088', 'Helene Fischer', '2025-11-05', 'Endocrinology', '4100.00', 'EndoCare', 'Pending', '7000095555', 'NO']
# ['P089', 'Anil Kapoor', '2025-11-06', 'Orthopedics', '7200.00', 'HealthPlus', 'Paid', '9900094444', 'Yes']
# ['P090', 'Molly Ringwald', '2025-11-06', 'Pediatrics', '1100.00', 'ChildCare', 'UnPaid', '7700041111', 'No']
# ['P091', 'Yusuf Pathan', '2025-11-07', 'General Medicine', '1900.00', 'HealthPlus', 'pending', '9810088888', 'yes']
# ['P092', 'Nicole Kidman', '2025-11-07', 'Cardiology', '21000.00', 'MedSecure', 'PAID', '7700021111', 'Yes']
# ['P093', 'Raj Malhotra', '2025-11-07', 'ENT', '2500.00', 'MedSecure', 'Pending', '7700010001', 'No']
# ['P094', 'Tara Strong', '2025-11-08', 'Neurology', '4900.00', 'GlobalCare', 'Unpaid', '7000019999', 'Yes']
# ['P095', 'Victor Hugo Jr', '2025-11-08', 'Oncology', '29000.00', 'CancerCover', 'paid', '7700002222', 'Yes']
# ['P096', 'Ritika Sen', '2025-11-09', 'General Medicine', '850.00', 'HealthPlus', 'pending', '7700003333', 'No']
# ['P097', 'Dominic Toretto', '2025-11-09', 'Orthopedics', '6800.00', 'HealthPlus', 'PAID', '8800090000', 'Yes']
# ['P098', 'Sasha Banks', '2025-11-10', 'Pediatrics', '950.00', 'ChildCare', 'Pending', '7700091113', 'No']
# ['P099', 'Igor Kravitz', '2025-11-10', 'Neurology', '5900.00', 'GlobalCare', 'UNPAID', '6000015555', 'Yes']
# ['P100', 'Ankita Sharma', '2025-11-10', 'Endocrinology', '4200.00', 'EndoCare', 'Paid', '9810090000', 'No']
# ['P016', 'Sunil Sharma', '2025-10-09', 'Cardiology', 'â‚¹8200.00', 'MedSecure', 'Paid', '+91-98 100 12345', 'True']
# ['P037', 'Igor Petrov', '2025-10-19', 'Oncology', '52000.00', 'CancerCover', 'PAID', '7700090000', 'YES']
# ['P026', 'Victor Hugo', '2025-10-13', 'Cardiology', '9800.75', 'MedSecure', 'Pending', '7700044444', 'Yes']
# ['P002', 'Riya Sharma', '02-10-2025', 'Orthopedics', '12000.00 ', 'HealthPlus', ' pending ', '9810098765', 'No']
# ['P049', 'Manish Malhotra', '2025-10-23', 'Cardiology', '12500.00', 'MedSecure', 'Unpaid', '9900091111', 'Yes']
# ['P093', 'Raj Malhotra', '2025-11-07', 'ENT', '2500.00', 'MedSecure', 'Pending', '7700010001', 'No']
# ['P065', 'Marcus Aurelius', '2025-10-28', 'Oncology', '34000.00', 'CancerCover', 'Unpaid', '9990022222', 'Yes']
# ['P008', 'Li Wei', '2025-10-05', 'Oncology', '45000.00', 'CancerCover', 'paid ', '6000012345', 'Yes']
# ['P090', 'Molly Ringwald', '2025-11-06', 'Pediatrics', '1100.00', 'ChildCare', 'UnPaid', '7700041111', 'No']
# ['P034', 'Nora Bates', '2025-10-17', 'Pediatrics', '1300.00', 'ChildCare', 'Pending', '7700077777', 'No']
# Patients with ther important data...
# P002 Riya Sharma 02-10-2025 12000.00   pending
# P003   2025/10/02 3500.00 Unpaid
#  Meena Patel 2025-10-03 2200.00 Paid
# P005 Suresh K 2025-10-03 one thousand Pending
# P006 Neha Verma 2025-10-04 4800.50 PAID
# P007 Alex Johnson 10/04/2025 6000.00 Pending
# P008 Li Wei 2025-10-05 45000.00 paid 
# P009 Anita Singh 2025-10-05 900.00 unPaid
# P010 Michael Brown 2025.10.06 1500.00 Paid
# P011 Sophia Lee 2025-10-06 5200.00 Pending
# P012 Rajesh Kumar 2025-10-07 16000.00 Paid
# P013 Olga Petrova 07/10/2025 4200.00 Unpaid
# P014 Diego Marquez 2025-10-08 7000.00  PAID
# P015 Ananya Rao 2025-10-08 1100.00 pending
# P016 Sunil Sharma 2025-10-09 â‚¹8200.00 Paid
# P017 Leila Ahmed 2025-10-09 600.00 unpaid
# P018 Peter Clark 2025-10-10 4300.00 Pending
# P019 Maya Singh 2025/10/10 2100.00 paid
# P020 Oscar Wilde 2025-10-11 36000.00 Paid
# P021 Lina Gomez 2025-10-11 2500.00 Pending
# P022 Tom Hanks 2025-10-12 5000.00 Unpaid
# P023 Sana Khan  3200.00 Paid
# P024 Raj Patel 2025-13-12 4100.00 PENDING
# P025 Emily Stone 2025-10-13 900.00 Paid
# P026 Victor Hugo 2025-10-13 9800.75 Pending
# P027 Zara Ali 2025-10-14 1400.00 PAID
# P028 Ken Watanabe 2025-10-14 22000.00 Paid
# P029 Liu Chen 2025-10-15  five thousand two hundred   pending
# P030 Mira Kapoor 15/10/2025 3000.00 Unpaid
# P031 Sam Wilson 2025-10-16 6100.00 pending
# P032 Isha Verma 2025-10-16 800.00 Paid
# P033 Arjun Singh 2025-10-17 14500.00 Paid
# P034 Nora Bates 2025-10-17 1300.00 Pending
# P035 Paul Green 2025-10-18 5400.00 Paid
# P036 Farah Khan 2025-10-18 2900.00 Unpaid
# P037 Igor Petrov 2025-10-19 52000.00 PAID
# P038 Karen Mills 2025-10-19 1700.00 Pending
# P039 Yuki Tanaka 2025-10-19 4700.00 Paid
# P040 Rachel Adams 2025-10-20 41OO.00 Pending
# P041 Dev Patel 2025-10-20 2300.00 paid
# P042 Sofia Loren 2025-10-20 18500.00 PAID
# P043 Imran Khan 2025-10-21 900.00 Pending
# P044 Linda Park 2025-10-21 3100.00 Unpaid
# P045 Noah Brown 2025-10-21 2000.00 Paid
# P046 Nadia Petrova 2025-10-22 4500.00 Pending
# P047 Oscar Diaz 2025-10-22 8000.00 Paid
# P048 Helena Costa 2025-10-22 2600.00 Pending
# P049 Manish Malhotra 2025-10-23 12500.00 Unpaid
# P050 Eva Green 2025-10-23 28000.00 Paid
# P051 Samir Das 2025-10-23 1900.00 Paid
# P052 Priya Menon 2025-10-24 2 MedSecure
# P053 Andrei Ivanov 2025-10-24 4100.00 Unpaid
# P054 Lucy Hale 2025-10-24 1100.00 Paid
# P055 Deepak Yadav 2025-10-25 7200.00 Paid
# P056 Helga Schmidt 2025-10-25 39000.00 PENDING
# P057 Karan Johar 2025-10-25 4500.00 pending
# P058 Mayra Lopez 2025-10-26 900.00 PAID
# P059 Daniel Craig 2025-10-26 3300.00 Unpaid
# P060 Ayesha Khan 26-10-2025 4200.00 paid
# P061 Boris Becker 2025-10-27 1500.00 Pending
# P062 Grace Park 2025-10-27 800.00 Paid
# P063 Rajiv Menon 2025-10-27 23000.00 PAID
# P064 Sylvia Plath 2025-10-28 600.00 Pending
# P065 Marcus Aurelius 2025-10-28 34000.00 Unpaid
# P066 Hannah Wells 2025-10-28 2700.00 Paid
# P067 Victor Cruz 2025-10-29 6400.00  pending
# P068 Nina Simone 2025-10-29 3800.00 Unpaid
# P069 Omar Sy 2025-10-29 5900.00 PAID
# P070 Leah Baker 2025-10-30 1000.00 Pending
# P071 Harish Rao 2025-10-30 13200.00 Paid
# P072 Sonia Kapoor 2025-10-30 1700.00 Pending
# P073 Neil Armstrong 2025-10-31 47000.00 Paid
# P074 Maya Angelou 2025-10-31 3300.00 unpaid
# P075 Rajeshwari Pillai 2025-10-31 2900.00 Pending
# P076 Daniel Ortega 2025-11-01 2300.00 Paid
# P077 Linda Nguyen 2025-11-01 4300.00 Pending
# P078 Mark Ruffalo 2025-11-02 9400.00 unpaid
# P079 Aditi Rao 2025-11-02 700.00 Paid
# P080 Chen Li 2025-11-02 3050.00 Paid
# P081 Olivia Wilde 2025-11-03 900.00  pending
# P082 Pranav Joshi 2025-11-03 6100.00 Paid
# P083 Samanta Fox 2025-11-03 36000.00 Pending
# P084 Imelda Marcos 2025-11-04 1500.00 Paid
# P085 Diego Rivera 2025-11-04 15500.00 unpaid
# P086 Aisha Siddiqui 2025-11-05 2400.00 Pending
# P087 Brian Cox 2025-11-05 1700.00 Paid
# P088 Helene Fischer 2025-11-05 4100.00 Pending
# P089 Anil Kapoor 2025-11-06 7200.00 Paid
# P090 Molly Ringwald 2025-11-06 1100.00 UnPaid
# P091 Yusuf Pathan 2025-11-07 1900.00 pending
# P092 Nicole Kidman 2025-11-07 21000.00 PAID
# P093 Raj Malhotra 2025-11-07 2500.00 Pending
# P094 Tara Strong 2025-11-08 4900.00 Unpaid
# P095 Victor Hugo Jr 2025-11-08 29000.00 paid
# P096 Ritika Sen 2025-11-09 850.00 pending
# P097 Dominic Toretto 2025-11-09 6800.00 PAID
# P098 Sasha Banks 2025-11-10 950.00 Pending
# P099 Igor Kravitz 2025-11-10 5900.00 UNPAID
# P100 Ankita Sharma 2025-11-10 4200.00 Paid
# P016 Sunil Sharma 2025-10-09 â‚¹8200.00 Paid
# P037 Igor Petrov 2025-10-19 52000.00 PAID
# P026 Victor Hugo 2025-10-13 9800.75 Pending
# P002 Riya Sharma 02-10-2025 12000.00   pending
# P049 Manish Malhotra 2025-10-23 12500.00 Unpaid
# P093 Raj Malhotra 2025-11-07 2500.00 Pending
# P065 Marcus Aurelius 2025-10-28 34000.00 Unpaid
# P008 Li Wei 2025-10-05 45000.00 paid
# P090 Molly Ringwald 2025-11-06 1100.00 UnPaid
# P034 Nora Bates 2025-10-17 1300.00 Pending


# Skipped rows:  9
# Processed rows:  100


# Pending payments data is generated...
# Patient summary generated successfully...