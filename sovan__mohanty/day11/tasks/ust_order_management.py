#Task UST Order Management CSV Processing

#importing CSV file
import csv

#List of Valid Indian States
valid_states = [
    "andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh",
    "goa", "gujarat", "haryana", "himachal pradesh", "jharkhand",
    "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur",
    "meghalaya", "mizoram", "nagaland", "odisha", "punjab",
    "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura",
    "uttar pradesh", "uttarakhand", "west bengal"
]

#Order Record Class
class OrderRecord:
    def __init__(self, row):
        self.row = row
        self.error_reason = None
        self.valid = False
        self.cleaned = None
    #Validating the rows
    def validate_and_transform(self):
        try:
           
            if not any(self.row.values()):
                self.error_reason = "Empty row"
                return
            order_id = self.row.get("order_id", "").strip()
            customer_name = self.row.get("customer_name", "").strip()
            state = self.row.get("state", "").strip().lower()
            product = self.row.get("product", "").strip()
            quantity = self.row.get("quantity", "").strip()
            price_per_unit = self.row.get("price_per_unit", "").strip()
            status = self.row.get("status", "").strip()

            if not customer_name:
                self.error_reason = "Missing customer_name"
                return

            if state not in valid_states:
                self.error_reason = f"Invalid state: {state}"
                return

            try:
                quantity = int(quantity)
                if quantity <= 0:
                    self.error_reason = "Quantity must be positive"
                    return
            except Exception:
                self.error_reason = "Invalid quantity format"
                return

            try:
                price_per_unit = float(price_per_unit)
                if price_per_unit == 0:
                    self.error_reason = "Price per unit must be positive"
                    return
                if price_per_unit < 0:
                    price_per_unit = abs(price_per_unit)
            except Exception:
                self.error_reason = "Invalid price format"
                return
            total_amount = quantity * price_per_unit
            status = status.upper()

            self.cleaned = {
                "order_id": order_id,
                "customer_name": customer_name,
                "state": state.title(),  
                "product": product,
                "quantity": quantity,
                "price_per_unit": price_per_unit,
                "total_amount": total_amount,
                "status": status
            }
            self.valid = True

        except Exception as e:
            self.error_reason = f"Unexpected error: {str(e)}"

#Creating Class OrderProcessor
class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.valid_orders = []
        self.invalid_orders = []
    #Reading and processing the order_raw(in).csv file
    def read_and_process(self):
        try:
            with open(self.input_file, mode="r", newline="") as f:
                reader = csv.DictReader(f)
                required_cols = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status"]

                for col in required_cols:
                    if col not in reader.fieldnames:
                        raise KeyError(f"Missing column: {col}")

                for row in reader:
                    order = OrderRecord(row)
                    order.validate_and_transform()
                    if order.valid:
                        self.valid_orders.append(order.cleaned)
                    else:
                        row["error_reason"] = order.error_reason
                        self.invalid_orders.append(row)

        except FileNotFoundError:
            print(f" File not found: {self.input_file}")
        except KeyError as e:
            print(f" CSV missing required column: {e}")
        except Exception as e:
            print(f"Unexpected error while reading file: {e}")
    #Writing the datas in orders_processed.csv
    def write_outputs(self):
        if self.valid_orders:
            with open(self.processed_file, mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.valid_orders[0].keys())
                writer.writeheader()
                writer.writerows(self.valid_orders)
        #Writing datas in orders_skipped.csv
        if self.invalid_orders:
            with open(self.skipped_file, mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.invalid_orders[0].keys())
                writer.writeheader()
                writer.writerows(self.invalid_orders)


if __name__ == "__main__":
    processor = OrderProcessor("orders_raw(in).csv", "orders_processed.csv", "orders_skipped.csv")
    processor.read_and_process()
    processor.write_outputs()

    print(" Processing complete")
    print(f"Processed orders: {len(processor.valid_orders)}")
    print(f"Skipped orders: {len(processor.invalid_orders)}")

#Sample Execution
# Processing complete
# Processed orders: 89
# Skipped orders: 61