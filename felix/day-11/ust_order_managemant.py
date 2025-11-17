# Day 11
# UST Order Management CSV Processing
# Scenario
# UST is working with a large Indian e-commerce marketplace that handles orders from diverse customers
# across India. The operations team receives a raw CSV export each day containing order details from multiple
# states, regions, and customer backgrounds.
# Your task is to build a Python program that reads this CSV file, validates the data, applies business rules, and
# writes two separate CSV outputs:
# 1. Cleaned and processed orders
# 2. Invalid or skipped records (due to validation failures)
# This ensures high-quality order data for downstream financial and fulfillment teams.
# Objective
# Create a Python program using Object-Oriented Programming (OOP) and proper error handling to:
# 1. Read an input CSV: orders_raw.csv
# 2. Validate and transform order data
# 3. Write valid processed orders to: orders_processed.csv
# 4. Write skipped/invalid records to: orders_skipped.csv


import csv

class MissingColumnInCsvFileError(Exception):
    pass

class BlankFieldError(Exception):
    pass

valid_state = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
class OrderRecord:
    def __init__(self,data):
        self.data = data
        
    def order_check(self):
        try:
                
            if self.data['quantity'].isdigit()==False or self.data['quantity'] == '0':
                self.data['error_reason'] = "quantity is not valid"
                return self.data
            
            if self.data['price_per_unit'] == "":
                raise BlankFieldError
            elif int(self.data['price_per_unit'])<0:
                self.data['price_per_unit'] = abs(int(self.data['price_per_unit']))
            
            if 'customer_name'not in self.data or self.data['customer_name'] == "":
                self.data['error_reason'] = "customer name missing"
                return self.data
             
            if self.data['state'] not in valid_state:
                self.data['error_reason'] = "state is not valid"
                return self.data
            
            self.data['total_amount'] = int(self.data['quantity'])*int(self.data['price_per_unit'])
            
            self.data['status'] = self.data['status'].upper()
            
        except MissingColumnInCsvFileError:
            self.data['error_reason'] = "some column is missing"
            return self.data
        
        except BlankFieldError:
            self.data['error_reason'] = "some datas are blank"
            return self.data
        
        except ValueError as v:
            self.data['error_reason'] = v
            return self.data
        
        except TypeError as t:
            self.data['error_reason'] = t
            return self.data
        
        else:
            return self.data
        


class OrderProcessor(OrderRecord):
    def __init__(self):
        skipped = 0
        processed = 0
        with open("orders_raw.csv","r") as file:
            all_data = csv.DictReader(file)
            
            for data in all_data:
                obj = OrderRecord(data)
                new_data = obj.order_check()
                
                if 'error_reason' in new_data:
                    with open("orders_skipped.csv","a",newline="") as file1:
                        write = csv.writer(file1)
                        write.writerow(data.values())
                        skipped += 1
                        
                else:
                    with open("orders_processed.csv","a",newline="") as file2:
                        write = csv.writer(file2)
                        write.writerow(data.values())
                        processed += 1
                        
            print("Processed data: ",processed)
            print("Skipped data: ",skipped)
                        
OrderProcessor()

# output

# Processed data:  89
# Skipped data:  61