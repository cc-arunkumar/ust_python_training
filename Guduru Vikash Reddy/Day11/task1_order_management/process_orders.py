import csv
import os

#Valid Indian states
VALID_STATES = {
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
    
}

class OrderRecord:
    def __init__(self, row):
        self.row = row
        self.cleaned = {}
        self.error_reason = None

    def is_valid(self):
        try:
            # Skip completely empty rows
            if not any(value.strip() for value in self.row.values()):
                self.error_reason = "Empty row"
                return False

            # Validate customer_name
            customer_name = self.row.get("customer_name", "").strip()
            if not customer_name:
                self.error_reason = "Missing customer_name"
                return False

            # Validate state
            state = self.row.get("state", "").strip()
            if state not in VALID_STATES:
                self.error_reason = f"Invalid state: {state}"
                return False

            # Validate quantity
            quantity_str = self.row.get("quantity", "").strip()
            if not quantity_str.isdigit() or int(quantity_str) <= 0:
                self.error_reason = f"Invalid quantity: {quantity_str}"
                return False
            quantity = int(quantity_str)

            # Validate price_per_unit
            price_str = self.row.get("price_per_unit", "").strip()
            try:
                price = float(price_str)
                if price <= 0:
                    price = abs(price)
            except:
                self.error_reason = f"Invalid price_per_unit: {price_str}"
                return False

            # Normalize status
            status = self.row.get("status", "").strip().upper()

            # Compute total_amount
            total_amount = quantity * price

            # Store cleaned data
            self.cleaned = {
                "order_id": self.row.get("order_id", "").strip(),
                "customer_name": customer_name,
                "state": state,
                "product": self.row.get("product", "").strip(),
                "quantity": quantity,
                "price_per_unit": price,
                "total_amount": total_amount,
                "status": status
            }
            return True

        except Exception as e:
            self.error_reason = f"Unexpected error: {str(e)}"
            return False

class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.valid_orders = []
        self.invalid_orders = []

    def process_orders(self):
        if not os.path.exists(self.input_file):
            print(f" Error: File '{self.input_file}' not found.")
            return

        try:
            with open(self.input_file, newline='', ) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    order = OrderRecord(row)
                    if order.is_valid():
                        self.valid_orders.append(order.cleaned)
                    else:
                        row["error_reason"] = order.error_reason
                        self.invalid_orders.append(row)

            self.write_outputs()

            # Print summary
            total = len(self.valid_orders) + len(self.invalid_orders)
            print(f"\nProcessing Summary")
            print(f"----------------------")
            print(f"Total records processed: {total}")
            print(f"Valid orders: {len(self.valid_orders)}")
            print(f"Invalid/skipped orders: {len(self.invalid_orders)}")

        except Exception as e:
            print(f"Error reading file: {str(e)}")

    def write_outputs(self):
        # Write valid orders
        with open(self.processed_file, "w", newline='') as file:
            fieldnames = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "total_amount", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.valid_orders)

        # Write invalid orders
        with open(self.skipped_file, "w", newline='') as file:
            fieldnames = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status", "error_reason"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.invalid_orders)

if __name__ == "__main__":
    processor = OrderProcessor(
        input_file="orders_raw.csv",
        processed_file="orders_processed.csv",
        skipped_file="orders_skipped.csv"
    )
    processor.process_orders()