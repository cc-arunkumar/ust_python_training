import os
import math
import datetime
import csv

today=datetime.date.today()
common_path="Day11\\task_ust_order_processing_utility"
input_file="Day11\\task_ust_order_processing_utility\\input\\orders.csv"

op_folder= common_path +"\\output"
log_folder= common_path+"\\logs"

if not os.path.exists(op_folder):
    os.makedirs(op_folder) 

if not os.path.exists(log_folder):
    os.makedirs(log_folder) 

output_file =op_folder + "\\processed_orders.txt"
log_file = log_folder + "\\execution_log.txt"
skipped_file =op_folder + "\\skipped_orders.txt"

log=open(log_file,"a")
skip=open(skipped_file,"a")

def write_log(msg):
    timestamp = today.strftime("%Y-%m-%d")
    log.write(f"[{timestamp}] {msg}\n")

write_log("INFO: Started Order Processing")
write_log("INFP: Folder check completed")

def validate_date(date_str):
    try:
        y,m,d =map(int,date_str.split("-"))
        return datetime.date(y, m, d)
    except:
        return None

def del_date(order_date):
    deleivery=order_date + datetime.timedelta(days=5)

    while deleivery.weekday() ==6:
        deleivery+=datetime.timedelta(days=1)
    
    return deleivery


with open(input_file,"r") as ip:
    reader=csv.DictReader(ip)

    for row in reader:
        order_id=row["order_id"]
        customer_name=row["customer_name"]
        product=row["product"]
        quantity=int(row["quantity"])
        unit_price=float(row["unit_price"])
        order_date=row["order_date"]

        write_log(f"Files logged In{order_id}")

        if quantity<0:
            skip.write(f"Order ID: {order_id} | Reason : Invalid quantity")
            write_log(f"Order Skipped {order_id}: Invalid Quantity")
            continue

        if unit_price<0:
            skip.write(f"Order ID :{order_id} | Reason : Unit Price is below 0")
            write_log(f"Order Skipped {order_id} | Reason : Invalid Unit Price")
            continue

        # date valdation
        order_date=validate_date(order_date)

        if order_date is None:
            skip.write(f"Order ID :{order_id} | Reason : Invalid Date")
            write_log(f"WARNING: Order Skipped {order_id} | Reason : Invalid Date")
            continue


        # future order
        if order_date>today:
            skip.write(f"Order ID :{order_id} | Reason : Order Date is in Future")
            write_log(f"Order Skipped {order_id} | Reason : Order Date in IN future")
            continue

        total_cost=math.ceil(quantity*unit_price)
        deleivery_date=del_date(order_date)

        with open(output_file,"a") as op:
            op.writelines([
                f"Order_ID :{order_id}\n",
                f"Customer :{customer_name}\n",
                f"Product :{product}\n",
                f"Quantity :{quantity}\n",
                f"Unit Price :{unit_price}\n",
                f"Total Amout :{total_cost}\n",
                f"Order Date :{order_date}\n",
                f"Estimated Deleivery :{deleivery_date}\n",
                "------------------------------------\n"
            ])
            write_log(f"INFO: Order {order_id} Processed Sucessfully")

write_log("INFO: Finished Order Processing")
log.close()
skip.close()



