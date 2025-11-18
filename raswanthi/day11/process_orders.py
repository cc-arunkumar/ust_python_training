import csv

#considering valid states 
valid_states = [
    "Tamil Nadu", "Punjab", "Gujarat", "Uttar Pradesh", "Maharashtra", "Ladakh", "Karnataka",
    "Delhi", "Kerala", "Rajasthan", "West Bengal"
]

class OrderRecord:
    def __init__(self, row):
        self.row = row
        self.error_reason = None
        self.is_valid = False
        self.processed_data = None
        self.validate_and_transform()

    #validation logic
    def validate_and_transform(self):
        try:
            order_id = self.row["order_id"].strip()
            customer_name = self.row["customer_name"].strip()
            state = self.row["state"].strip()
            product = self.row["product"].strip()
            quantity = self.row["quantity"].strip()
            price_per_unit = self.row["price_per_unit"].strip()
            status = self.row["status"].strip()
        except KeyError as e:
            self.error_message = f"Missing column: {str(e)}"
            return

        if not any([order_id, customer_name, state, product, quantity, price_per_unit, status]):
            self.error_message = "Empty row"
            return
        
        if customer_name == "":
            self.error_message = "Missing customer_name"
            return

       
        if state not in valid_states:
            self.error_message = f"Invalid state: {state}"
            return

        try:
            quantity = int(quantity)
            if quantity <= 0:
                self.error_message = "Invalid quantity"
                return
        except Exception:
            self.error_message = "Quantity not numeric"
            return

        try:
            price_per_unit = float(price_per_unit)
            if price_per_unit == 0:
                self.error_message = "Invalid price_per_unit"
                return
            if price_per_unit=="":
                self.error_message="Missing price_per_unit"
                return
            if price_per_unit < 0:
                price_per_unit = abs(price_per_unit)
        except Exception:
            self.error_message= "Price not numeric"
            return
        
        #calculating total amount
        total_amount = quantity * price_per_unit

    
        status = status.upper()
       
        self.is_valid = True
        self.processed_data = {
            "order_id": order_id,
            "customer_name": customer_name,
            "state": state,
            "product": product,
            "quantity": quantity,
            "price_per_unit": price_per_unit,
            "total_amount": total_amount,
            "status": status
        }


class OrderProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.valid_orders = []
        self.invalid_orders = []

    #processing order function
    def process_orders(self):
        try:
            with open(self.input_file, mode="r", newline="", encoding="utf-8") as inpfile:
                reader = csv.DictReader(inpfile)

                required_columns = ["order_id", "customer_name", "state", "product",
                                    "quantity", "price_per_unit", "status"]

                # Check for missing columns
                for col in required_columns:
                    if col not in reader.fieldnames:
                        print(f"Error: Missing column {col} in CSV")
                        return

                for row in reader:
                    order = OrderRecord(row)
                    if order.is_valid:
                        self.valid_orders.append(order.processed_data)
                    else:
                        row["error_reason"] = order.error_reason
                        self.invalid_orders.append(row)
                        

        except FileNotFoundError:
            print(f"Error: File {self.input_file} not found")
        except Exception as e:
            print(f"Reading file - Error {str(e)}")

    def write_output(self):
        if self.valid_orders:
            with open("orders_processed.csv", mode="w", newline="") as outfile:
                field_names = ["order_id", "customer_name", "state", "product",
                               "quantity", "price_per_unit", "total_amount", "status"]
                writer = csv.DictWriter(outfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(self.valid_orders)

        if self.invalid_orders:
            with open("orders_skipped.csv", mode="w", newline="") as outfile:
                field_names = ["order_id", "customer_name", "state", "product",
                               "quantity", "price_per_unit", "status", "error_reason"]
                writer = csv.DictWriter(outfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(self.invalid_orders)


if __name__ == "__main__":
    processor = OrderProcessor("orders_raw.csv")
    processor.process_orders()
    processor.write_output()

    print("Processing complete.")
    print(f"Processed rows: {len(processor.valid_orders)}")
    print(f"Skipped rows: {len(processor.invalid_orders)}")
