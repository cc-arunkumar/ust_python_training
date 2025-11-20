import os
import csv
import math
from datetime import date,timedelta

current = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day11/module/task1-ust_order_processing_utility"

# Checking if output folder exists in current dir else creating one

if not os.path.exists(current+"/output"):
    os.mkdir(current+"/output")
else:
    print("Folder exists!")
 
    
# Validation function 
def validate(row):
    try:
        for data in row:
            if data == "quantity" and int(row[data])<=0:
                return False,"Quantity is less than 1"
            if data == "unit_price" and int(row[data])<=0:
                return False,"Unit price is less than 1"
            if data == "order_date" and date.fromisoformat(row[data]):
                today = date.today()
                if date.strptime(row[data],"%Y-%m-%d")>today:
                    return False,"Date is in the future"
                    
            
    except Exception as e:
        return False,str(e)
    else:
        return True,"Validated"

# reading orders file
with open(current+"/input/orders.csv","r") as file:
    # Checking if logs folder exists in current dir else creating one
    if not os.path.exists(current+"/logs"):
        os.makedirs(current+"/logs")
    # opening excution file to write execution details
    
    with open(current+"/logs/execution_log.txt","w") as log:
        
        log.writelines(f"[{date.today()}] INFO: Started Order Processing\n")
        log.writelines(f"[{date.today()}] INFO: Folder Check Completed\n")
        
        # opening processed file for writing processed data
        with open(current+"/output/processed_orders.txt","w") as file1:
            
            # opening skipped file for writing processed data
            with open(current+"/output/skipped_orders.txt","w") as file2:
                
                csv_file = csv.DictReader(file)
                header = csv_file.fieldnames
                for row in csv_file:
                    
                    log.writelines(f"[{date.today()}] INFO: Processing Order for {row[header[0]]}\n")
                    condition,reason = validate(row)
                    if condition:
                        # calculating total cost for every row
                        row["total_cost"] = math.ceil(int(row[header[3]]) * int(row[header[4]]))
                        # calculating delivery date for every row 
                        delivery = date.strptime(row[header[5]],"%Y-%m-%d") + timedelta(days=5)
                        # checking for sunday and adding 1 more day if exists
                        if delivery.weekday() == 6:
                            delivery = delivery + timedelta(days=1)
                        row["delivery_date"] = delivery 
                        
                        log.writelines(f"[{date.today()}] INFO: Order {row[header[0]]} Processed successfully\n")
                        file1.write(f"""Order_id: {row[header[0]]}
Customer: {row[header[1]]}
Product: {row[header[2]]}
Quantity: {row[header[3]]}
Unit Price: {row[header[4]]}
Total Cost: {row["total_cost"]}
Order Date: {row[header[5]]}
Estimated Delivery: {row["delivery_date"]}
-------------------------------------------------\n""")
                    else:
                        
                        log.writelines(f"[{date.today()}] WARNING: Order {row[header[0]]} Skipped - {reason}\n")
                        file2.write(f"""Order_id: {row[header[0]]}: {reason}\n""")
        log.writelines(f"[{date.today()}]  INFO: Finished Order Processing\n")