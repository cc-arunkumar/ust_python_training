import csv
import os

# -----------------------------------------------------------
# OrderRecord class: Validates and transforms a single record
# -----------------------------------------------------------

class OrderRecord:

    VALID_STATES = {
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
        "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
        "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi", "Ladakh", "Jammu & Kashmir"
    }

    def __init__(self, row):
        self.row = row
        self.cleaned = {}
        self.error_reason = None

    def is_empty_row(self):
        return all(str(v).strip() == "" for v in self.row.values())

    def validate(self):

        if self.is_empty_row():
            self.error_reason = "Empty row"
            return False

        # Customer Name
        customer_name = self.row.get("customer_name", "").strip()
        if not customer_name:
            self.error_reason = "Missing customer_name"
            return False

        # State validation
        state = self.row.get("state", "").strip()
        if state not in self.VALID_STATES:
            self.error_reason = f"Invalid state: {state}"
            return False

        # Quantity validation
        qty_raw = self.row.get("quantity", "").strip()
        try:
            qty = int(qty_raw)
            if qty <= 0:
                raise ValueError
        except:
            self.error_reason = f"Invalid quantity: {qty_raw}"
            return False

        # Price validation
        price_raw = self.row.get("price_per_unit", "").strip()

        if price_raw == "":
            self.error_reason = "Missing price_per_unit"
            return False

        try:
            price = float(price_raw)
            if price < 0:
                price = abs(price)   # convert negative → positive
            if price == 0:
                raise ValueError
        except:
            self.error_reason = f"Invalid price: {price_raw}"
            return False

        # Compute total_amount
        total_amount = qty * price

        # Normalize status to UPPERCASE
        status = self.row.get("status", "").strip().upper()

        # Store cleaned record
        self.cleaned = {
            "order_id": self.row.get("order_id", ""),
            "customer_name": customer_name,
            "state": state,
            "product": self.row.get("product", ""),
            "quantity": qty,
            "price_per_unit": price,
            "total_amount": total_amount,
            "status": status
        }

        return True


# -----------------------------------------------------------
# OrderProcessor class: Reads, validates, writes output
# -----------------------------------------------------------

class OrderProcessor:

    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file

        self.valid_records = []
        self.invalid_records = []

    def read_file(self):

        if not os.path.exists(self.input_file):
            print(f"ERROR: File not found {self.input_file}")
            return False

        try:
            with open(self.input_file, mode="r", encoding="utf-8", newline="") as f:
                reader = csv.DictReader(f)

                required = {
                    "order_id", "customer_name", "state", "product",
                    "quantity", "price_per_unit", "status"
                }

                if not required.issubset(set(reader.fieldnames)):
                    print("ERROR: Missing required columns.")
                    print("Found columns:", reader.fieldnames)
                    return False

                for row in reader:

                    order = OrderRecord(row)

                    if order.validate():
                        self.valid_records.append(order.cleaned)
                    else:
                        row["error_reason"] = order.error_reason
                        self.invalid_records.append(row)

        except Exception as e:
            print("ERROR reading file:", e)
            return False

        return True

    def write_output(self):

        # Valid records → orders_processed.csv
        with open(self.processed_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "order_id", "customer_name", "state", "product",
                "quantity", "price_per_unit", "total_amount", "status"
            ])
            writer.writeheader()
            writer.writerows(self.valid_records)

        # Skipped records → orders_skipped.csv
        with open(self.skipped_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "order_id", "customer_name", "state", "product",
                "quantity", "price_per_unit", "status", "error_reason"
            ])
            writer.writeheader()
            writer.writerows(self.invalid_records)

    def run(self):
        print("Processing:", self.input_file)

        if self.read_file():
            self.write_output()
            print(f"Valid records:{len(self.valid_records)}")
            print(f"Skipped records: {len(self.invalid_records)}")


# MAIN

if __name__ == "__main__":
    processor = OrderProcessor(
        input_file="DAY 11\\tasks\\orders_raw.csv",
        processed_file="orders_processed.csv",
        skipped_file="orders_skipped.csv"
    )
    processor.run()




























# import csv
# import os

# #CLAss order for checking and Validation

# class OrderDetails:

#     STATES_VALID={
#         "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh","Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
#         "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur","Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
#         "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura","Uttar Pradesh", "Uttarakhand", "West Bengal", "Delhi"
#     }

#     def __init__(self,row):
#         self.row=row
#         self.cleaned={}
#         self.error_caused_by=None

#     def is_empty(self):
#         return all(value.strip()=="" for value in self.row.values())
    
#     def validation(self):
#         if self.is_empty():
#             self.error_caused_by="Empty row"
#             return False
    
#         # CUstomer Name validation
#         name=self.row.get("customer_name","").strip()
#         if name=="":
#             self.error_caused_by ="Customer Name is Missing"
#             return False
        
#         #Validating states

#         state=self.row.get("state","").strip()
#         if state not in self.STATES_VALID:
#             self.error_caused_by=f"Invalid states :{state}"
#             return False
        

#         #Quality validation

#         q=self.row.get("quantity","")

#         try:
#             q=int(q)
#             if q<=0:
#                 raise ValueError
#         except:
#             self.error_caused_by=f"Invalid Quality: {q}"
#             return False
        
#         #price

#         p=self.row.get("price_per_unit","")

#         try:
#             p=float(p)
#             if p==0:
#                 self.error_caused_by="Invalid Price"
        
#         except:
#             self.error_caused_by=f"Invalid Price :{p}"
#             return False
        
#         # Normalise the sttus
#         status=self.row.get("status","").strip().upper()

#         # Organising ete cleaned rows
#         self.cleaned={
#             "order_id":self.row.get("order_id","").strip(),
#             "customer_name":name,
#             "state":state,
#             "product":self.row.get("product","").strip(),
#             "quantity":q,
#             "price_per_unit":p,
#             "total_amount":q*p,
#             "status":status

#         }
#         return True
    

# class orderProcess:
#     def __init__(self,input_file="DAY 11\tasks\\orders_raw.csv",op_clear="DAY 11\\tasks\\orders_processed.csv",op_unclear="DAY 11\\tasks\\orders_skipped.csv"):
#         self.input_file=input_file
#         self.op_clear=op_clear
#         self.op_unclear=op_unclear
#         self.valid=[]
#         self.invalid=[]
    
#     def readFile(self):
#         if not os.path.exists(self.input_file):
#             print("Input File not Found")
#             return False
        
#         try:
#             with open(self.input_file,newline='',encoding='utf-8') as f:
#                 reader=csv.DictReader(f)

#                 required_colums={"order_id","customer_name","state","product","quantity","price_per_unit","status"}
#                 if not required_colums.issubset(reader.fieldnames):
#                     print("Missing required columns.")
#                     print("Found:", reader.fieldnames)
#                     return False
                
#                 for row in reader:
#                     order=OrderDetails(row)
#                     if order.validation():
#                         self.valid.append(order.cleaned)
                    
#                     else:
#                         row["error_reason"]=order.error_caused_by
#                         self.invalid.append(row)
                
#             return True
        
#         except Exception as e:
#             print(f"Error in {f}")
#             return False
    

#     def writeFile(self):

#         with open(self.op_clear,"w",newline='',encoding='utf-8') as f:
#             writer=csv.DictWriter(f, fieldnames=[ "order_id","customer_name","state","product",
#                 "quantity","price_per_unit","total_amount","status"
#             ])
#             writer.writeheader()
#             writer.writerows(self.valid)
    
#         with open(self.op_unclear,"w",newline='',encoding='utf-8') as f:
#             writer=csv.DictWriter(f, fieldnames=[ "order_id","customer_name","state","product",
#                 "quantity","price_per_unit","total_amount","status"
#             ])
#             writer.writeheader()
#             writer.writerrows(self.invalid)
    
#     def run(self):
#         print("Reading file:", self.input_file)
#         if self.readFile():
#             self.writeFile()
#             # print("Process complete")
#             print("Valid records:", len(self.valid))
#             print("Skipped records:", len(self.invalid))
        



    