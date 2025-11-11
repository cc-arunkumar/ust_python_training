#   TASK_6_UST Healthcare (CSV Read / Write)
# Duration: 20–30 minutes
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


import csv
from platform import node

# Task Requirements
# 1. Read ust_healthcare_visits.csv with csv.DictReader .

with open('ust_healthcare_visits.csv',mode='r') as file:
    csv_reader=csv.reader(file)
    header = next(csv_reader)
    # for line in csv_reader:
    #     print(line)

    # 2. Basic validation / normalization:
    # 1. pending_payments.csv — visits not marked Paid.
    with open('pending_payments.csv','w',newline='') as s_file:
        second_file=csv.writer(s_file)
        # print(header)
        second_file.writerow(header)
        # ['patient_id', 'name', 'visit_date', 'department', 'billed_amount', 'insurance_provider', 'payment_status', 'contact', 'follow_up_required']

        for line in csv_reader:
            line[4]=float(line[4])
            if line[6] is not None:
                cap_val=str(line[6]).capitalize()
                line[6]=cap_val
                if line[6]=="Paid":
                    cap_val=''
                else:
                    second_file.writerow(line)












    


