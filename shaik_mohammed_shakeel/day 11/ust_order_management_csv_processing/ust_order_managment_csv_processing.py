import os
import csv
 
class OrderRecord:
    # List of valid Indian states for validation
    valid_state = [
        "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
        "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
        "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
        "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
        "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
        "Uttar Pradesh","Uttarakhand","West Bengal"
    ]

    def __init__(self, row):
        # Store each CSV row as a dictionary
        self.row = row
 
    def validate(self):
        # Extract and clean fields
        name = self.row.get("customer_name", "").strip()
        state = self.row.get("state", "").strip()
        qty = self.row.get("quantity", "")
        price = self.row.get("price_per_unit", "")
        status = self.row.get("status", "").strip()
 
        # Check if row is completely empty
        if not any(self.row.values()):
            self.error = "Empty row"
            return False
 
        # Customer name required
        if name == "":
            self.error = "Missing customer_name"
            return False
       
        # Validate state
        if state not in self.valid_state:
            self.error = f"Invalid state: {state}"
            return False
 
        # Validate quantity (must be positive integer)
        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except:
            self.error = f"Invalid quantity: {qty}"
            return False
 
        # Validate price (convert negative to positive)
        try:
            price = float(price)
            if price < 0:
                price = abs(price)
        except:
            self.error = f"Invalid price_per_unit: {price}"
            return False
       
        # Calculate total amount
        total = qty * price
        status = status.upper()  # normalize status
 
        # Return cleaned and validated record
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
        # CSV file path
        self.filename = filename
        # Valid and invalid order lists
        self.valid = []
        self.invalid = []
 
    def process(self):
        # Read CSV using DictReader
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            # Validate row-by-row
            for row in reader:
                order = OrderRecord(row)
                result = order.validate()

                if result:
                    self.valid.append(result)
                else:
                    # Attach error to row for output
                    row["error_reason"] = order.error
                    self.invalid.append(row)

        # Write output CSV files
        self.write_outputs()
 
    def write_outputs(self):
        # Write validated records to CSV
        with open("orders_processed.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "order_id","customer_name","state","product",
                "quantity","price_per_unit","total_amount","status"
            ])
            for v in self.valid:
                writer.writerow(v.values())
 
        # Write rejected records to CSV
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
                    i.get("error_reason")
                ])
               
        # Print summary
        print("Valid Orders: ", len(self.valid))
        print("Skipped Orders: ", len(self.invalid))
        print("Processing Completed successfully")

# Main script entry
if __name__ == "__main__":
    OrderProcessor("orders_raw.csv").process()

# ---------------------------------------------------------------------------------------------
 
# Sample Output
# Valid Orders:  89
# Skipped Orders:  61
# Processing Completed succesfully