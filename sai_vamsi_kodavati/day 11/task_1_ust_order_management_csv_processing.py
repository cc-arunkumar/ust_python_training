
import os
import csv
 
class OrderRecord:
    valid_state = [
        "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
        "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
        "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
        "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
        "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
        "Uttar Pradesh","Uttarakhand","West Bengal"
    ]
    def __init__(self, row):
        self.row = row
 
    def validate(self):
        name = self.row.get("customer_name", "").strip()
        state = self.row.get("state", "").strip()
        qty = self.row.get("quantity", "")
        price = self.row.get("price_per_unit", "")
        status = self.row.get("status", "").strip()
 
        if not any(self.row.values()):
            self.error = "Empty row"
            return False
 
        if name == "":
            self.error = "Missing customer_name"
            return False
       
        if state not in self.valid_state:
            self.error = f"Invalid state: {state}"
            return False
 
        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except:
            self.error = f"Invalid quantity: {qty}"
            return False
 
        try:
            price = float(price)
            if price < 0:
                price = abs(price)
        except:
            self.error = f"Invalid price_per_unit: {price}"
            return False
       
        total = qty * price
        status = status.upper()
 
        return {
            "order_id": self.row.get("order_id", ""),
            "customer_name": name,
            "state": state,
            "product": self.row.get("product", ""),
            "quantity": qty,
            "price_per_unit": price,
            "total_amount": total,
            "status": status
        }
   
class OrderProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.valid = []
        self.invalid = []
 
    def process(self):
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                order = OrderRecord(row)
                result = order.validate()
                if result:
                    self.valid.append(result)
                else:
                    row["error_reason"] = order.error
                    self.invalid.append(row)
        self.write_outputs()
 
    def write_outputs(self):
        with open("orders_processed.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","total_amount","status"
            ])
            for v in self.valid:
                writer.writerow(v.values())
 
        with open("orders_skipped.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","status","error_reason"
            ])
            for i in self.invalid:
                writer.writerow([
                    i.get("order_id",""),
                    i.get("customer_name",""),
                    i.get("state",""),
                    i.get("product",""),
                    i.get("quantity",""),
                    i.get("price_per_unit"),
                    i.get("status",""),
                    i.get("error_reason")])
               
        print("Valid Orders: ",len(self.valid))
        print("Skipped Orders: ",len(self.invalid))
        print("Processing Completed succesfully")
if __name__ == "__main__":
    OrderProcessor("orders_raw.csv").process()

# ---------------------------------------------------------------------------------------------

# Sample Output
# Valid Orders:  89
# Skipped Orders:  61
# Processing Completed succesfully
