# UST Healthcare (CSV Read / Write)
# # Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two reports
# patient_summary.csv — one row per patient with total_visits and total_billed 

import csv
#reading the file in read mode
with open(r"deva_prasath\day-6\ust_healthcare_visits_new.csv",mode='r') as file:
    # Read the file using csv.DictReader to parse rows as dictionaries
    
    csv_dict_reader=csv.DictReader(file)
    # Open the output CSV file in write mode ('w')
    
    with open("patient_summary.csv",mode='w',newline='') as file:
        # Initialize variables to keep track of total visits and total bill amount
        total_visits=0
        total_bill=0
        
        # Initialize an empty dictionary to store patient data
        dicti={}
        
        # Loop through each row in the input file
        for row in csv_dict_reader:
            # If the payment status is not 'Paid', set the payment flag to 'Yes'
            
            if row['payment_status']!="Paid":
                payment="Yes"
            else:
                payment="No"
                
            # If not, initialize the patient entry in the dictionary
            
            if row['patient_id'] and row['visit_type']:
                total_visits += 1
                total_bill += float(row['billed_amount'])  
                if row['patient_id'] not in dicti:
                    #adding key value pairs
                    
                    dicti[row['patient_id']] = {
                        'name': row['name'],
                        'total_visits': 0,
                        'total_bill': 0,
                        'payment_status': payment
                    }
                dicti[row['patient_id']]['total_visits'] += 1
                dicti[row['patient_id']]['total_bill'] += float(row['billed_amount'])

        writer = csv.DictWriter(file, fieldnames=["patient_id", "name", "total_visits", "total_bill", "payment_status"])
        # Write the header row in the output file
        writer.writeheader()
        # Loop through the dictionary and write each patient's summary to the output file
        for i,j in dicti.items():
            writer.writerow({
                'patient_id': i,
                'name': j['name'],
                'total_visits': j['total_visits'],
                'total_bill': j['total_bill'],
                'payment_status': j['payment_status']
            })
    
    print("File stored in patient_summary")
    
    
#Sample output
# File stored in patient_summary
