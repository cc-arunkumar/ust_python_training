import csv


patient_data = {}

with open('ust_healthcare.csv', mode="r") as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        patient_id = row[0]
        name = row[1].strip()
        billed_amount = float(row[4])
        payment_status = str(row[6]).strip().capitalize()

        if patient_id not in patient_data:
            patient_data[patient_id] = {
                'name': name,
                'total_visits': 0,
                'total_billed': 0.0,
                'payment_status': 'YES' if payment_status == 'Paid' else 'NO'
            }

        patient_data[patient_id]['total_visits'] += 1
        patient_data[patient_id]['total_billed'] += billed_amount

        if payment_status != 'Paid':
            patient_data[patient_id]['payment_status'] = 'NO'
with open('patient_summary.csv', mode="w", newline='') as second_file:
    writer = csv.writer(second_file)
    header = ['patient_id', 'name', 'total_visits', 'total_billed', 'payment_status']
    writer.writerow(header)

    for patient_id, data in patient_data.items():
        writer.writerow([
            patient_id,
            data['name'],
            data['total_visits'],
            data['total_billed'],
            data['payment_status']
        ])
