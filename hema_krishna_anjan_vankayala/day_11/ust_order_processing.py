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

import os,csv,datetime,math

#Creating the Structure
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/output/processed_orders.txt'):
    os.mkdir(os.path.join('UST_Order_Processing','output'))
    with open(os.getcwd()+'/UST_Order_Processing/output/processed_orders.txt','w') as file:
        pass
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/output/skipped_orders.txt'):
    with open(os.getcwd()+'/UST_Order_Processing/output/skipped_orders.txt','w') as file:
        pass
 
if not os.path.exists(os.getcwd()+'/UST_Order_Processing/logs/execution_log.txt'):
    os.mkdir(os.path.join('UST_Order_Processing','logs'))
    with open(os.getcwd()+'/UST_Order_Processing/logs/execution_log.txt','w') as file:
        pass

#Write logs functions
def write_logs(message_type,message):
    today_date = datetime.datetime.today()
    with open(os.getcwd()+'/UST_Order_Processing/logs/execution_log.txt','a') as f:
        f.writelines(f'[{today_date}] {message_type}: {message}\n')
    

skipped_list = []
processes_list = []

class Order:
    def __init__(self, order_id, customer_name, product, quantity, unit_price, order_date):
        # keep raw values; convert and validate in validate()
        self.order_id = order_id
        self.customer_name = customer_name
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.order_date = order_date
        self.total_cost = 0

    def validate(self):
 
        # Log start of validation/processing
        write_logs('INFO', f'Processing order {self.order_id}')

        # quantity
        try:
            qty = int(self.quantity)
        except Exception:
            self.reason = 'Invalid Quantity'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, reason
        if qty <= 0:
            reason = 'Invalid Quantity'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, reason

        # unit_price
        try:
            price = int(self.unit_price)
        except Exception:
            reason = 'Invalid Unit Price'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, self.reason
        if price <= 0:
            reason = 'Invalid Unit Price'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, reason

        # order_date
        try:
            
            od = datetime.datetime.strptime(self.order_date, "%Y-%m-%d")
        except Exception:
            reason = 'Invalid date'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, reason
        if datetime.datetime.today() < od:
            reason = 'Order date in the future'
            write_logs('WARNING', f"Order {self.order_id} skipped - {reason}")
            return False, reason

        # All validations passed — normalize fields
        self.quantity = qty
        self.unit_price = price
        self.order_date = od

        # compute totals and delivery date
        self.total_cost = math.ceil(self.quantity * self.unit_price)
        self.delivery_date = self.order_date + datetime.timedelta(days=5)
        # if delivery falls on Sunday (weekday 6), push to Monday
        if self.delivery_date.weekday() == 6:
            self.delivery_date += datetime.timedelta(days=1)

        write_logs('INFO', f'Order {self.order_id} processed successfully')
        return True, None

write_logs('INFO','Started Order Processing')   

#Reading orders.csv file
with open(os.getcwd()+'/UST_Order_Processing/input/orders.csv','r') as f:
    data = csv.DictReader(f)
    write_logs('INFO','Folder check completed')
    
    for row in data:
        
        order_id=row['order_id']
        write_logs('INFO',f'Processing order {order_id}')
        customer_name=row['customer_name']
        product=row['product']
        quantity=row['quantity']
        unit_price=row['unit_price']
        order_date=row['order_date']
        
        order = Order(order_id,customer_name,product,quantity,unit_price,order_date)
        
        validated, reason = order.validate()
        
        if validated:
            processes_list.append([order.order_id,order.customer_name,order.product,order.quantity,order.unit_price,order.total_cost,order.order_date.strftime("%Y-%m-%d"),order.delivery_date.strftime("%Y-%m-%d")])
        else:
            skipped_list.append([row,reason])
        write_logs('INFO',f'Order {order_id} processed successfully')
        
write_logs('INFO', 'Finished Order Processing')

#Writing skipped_orders.txt
with open(os.getcwd()+"/UST_Order_Processing/output/skipped_orders.txt","w",newline="") as file:
    for row in skipped_list:
        file.write(f"OrderID: {row[0]['order_id']} | Reason :{row[1]} \n")

#Writing processed_orders.txt
with open(os.getcwd()+"/UST_Order_Processing/output/processed_orders.txt","w",newline="") as file:
    for row in processes_list:
        file.write(f"OrderID: {row[0]} \n CustCustomer:{row[1]}\n Product: {row[2]} \n Quantity: {row[3]} \n Unit Price: {row[4]} \n Total Cost: {row[5]} \n Order Date: {row[6]} \n Estimated Delivery:{row[7]} \n ------------------------------- \n")
        
#Sample Ouputs 
# processed_orders.txt 
# OrderID: 101
# Customer: Asha Nair
# Product: Laptop
# Quantity: 2
# Unit Price: 45000
# Total Cost: 90000
# Order Date: 2025-01-10
# Estimated Delivery: 2025-01-15
# --------------------------------------------------


# skipped_orders.txt format
# OrderID: 103 | Reason: Invalid quantity
# OrderID: 104 | Reason: Invalid date
# OrderID: 105 | Reason: Order date in the future


# (logs/execution_log.txt)
# Every step must be logged:
# [2025-01-18] INFO: Started Order Processing
# [2025-01-18] INFO: Folder check completed
# [2025-01-18] INFO: Processing order 101
# Modules Task 4
# [2025-01-18] INFO: Order 101 processed successfully
# [2025-01-18] WARNING: Order 104 skipped - Invalid date
# [2025-01-18] INFO: Finished Order Processing