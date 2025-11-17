# Modules Task
# UST Order Processing Utility
# Modules Covered: math , datetime , os
# Business Scenario
# UST’s internal procurement team receives daily CSV files that contain:
# Order IDs
# Customer names
# Product names
# Product quantities
# Price per unit
# Order date
# A new high-priority automated tool is needed for basic processing of these CSVs.
# Your job is to create a beginner-level Python script that performs simple
# calculations and file operations using:
# math → calculate totals
# datetime.date / datetime.timedelta → validate dates, estimate delivery date
# os → create folders, check file existence, generate logs
# This represents a mini internal utility, similar to tools used inside UST Delivery
# Projects.
# Final Expected Output
# Your script will:
# 1. Create required folders
# Modules Task 1
# 2. Read a sample orders CSV
# 3. Calculate total order cost using math module
# 4. Validate order date using datetime module
# 5. Calculate estimated delivery date (skip Sundays)
# 6. Write output to a text file
# 7. Create a log file showing processed and skipped orders

import os
import csv
import math
from datetime import date,timedelta

#Current Directory
directory = "D:/ust_python_training-1/arjun_j_s/day_11/UST_Order_Processing/"

#Calculate the delivery date
def estimated_delivery(order_date):
    order_date = date.strptime(order_date,"%Y-%m-%d")
    order_date+=timedelta(days=5)
    if(order_date.weekday()==6):
        order_date+=timedelta(days=1)
    return order_date

#To validate each records
def validate_record(item):
    try:
        for data in item:

            if(data=="quantity" and int(item[data])<=0):
                return False,"Quantity is not valid"
            
            if(data=="unit_price" and int(item[data])<=0):
                return False,"Unit price not valid"
            
            #Convert str to date format and compare 
            if(data=="order_date" and date.fromisoformat(item[data])):
                today = date.today()
                if(date.strptime(item[data],"%Y-%m-%d")>today):
                    
                    return False,"Cannot order with future date"

    except Exception as e:
        return False,str(e)
    
    else:
        return True,"Succeess"

#Read the csv file
with open(directory+"input/orders.csv","r") as file:
    if not os.path.exists(directory+"logs"):
        os.mkdir(directory+"/logs")

    with open(directory+"logs/execution_log.txt","w") as log:

        #Add log 
        log.writelines(f"[{date.today()}] INFO: Started Order Processing\n")
        log.writelines(f"[{date.today()}] INFO: Folder checking completed\n")
        dict_data = csv.DictReader(file)
        header=dict_data.fieldnames

        with open(directory+"output/processed_orders.txt","w") as file1:

            with open(directory+"output/skipped_orders.txt","w") as file2:

                for data in dict_data:

                    log.writelines(f"[{date.today()}] INFO: Processing Order for {data['order_id']}\n")
                    condition,statement = validate_record(data)
                    if(condition):
                        if not os.path.exists(directory+"output"):
                            os.mkdir(directory+"/output")
                        else:
                            
                            record =f"""OrderID: {data[header[0]]}                                            
Customer: {data[header[1]]}
Product: {data[header[2]]}
Quantity: {data[header[3]]}
Unit Price: {data[header[4]]}
Total Cost: {math.ceil(int(data[header[3]])*int(data[header[4]]))}
Order Date: {data[header[5]]}
Estimated Delivery: {estimated_delivery(data[header[5]])}
--------------------------------------------------\n"""
                            #Adding the processed record
                            file1.writelines(record)
                            log.writelines(f"[{date.today()}] INFO: Order {data['order_id']} Processed Successfully\n")
                    else:
                        #Adding the skipped record
                        file2.writelines(f"Order ID: {data['order_id']} | {statement}\n")
                        log.writelines(f"[{date.today()}] WARNING: Order {data['order_id']} Skipped - {statement}\n")
                log.writelines(f"[{date.today()}] INFO: Finished Order Processing")
