# UST Healthcare (CSV Read / Write)
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two reports
# pending_payments.csv — visits not marked Paid.




import csv
#opening the file in read mode
with open(r"deva_prasath\day-6\ust_healthcare_visits_new.csv",mode='r') as file:
    #storing in csv_dict_reader
    csv_dict_reader=csv.DictReader(file)
    
    #storing headers
    headers=csv_dict_reader.fieldnames
    
    #opening a new file named pending_payments 
    with open(r"pending_payments.csv",mode='w',newline='') as file:
        
        # Create a DictWriter object that will write dictionaries to the CSV file
        writer=csv.DictWriter(file,fieldnames=headers)
        
        # Write the header row based on the 'headers' list
        writer.writeheader()
        
        for row in csv_dict_reader:
            if row["payment_status"]!="Paid":
                #adding the rows
                writer.writerow(row)
                
    print("File stored in pending_payemnts.csv")


#Sample output
# File stored in pending_payemnts.csv    

