import csv
import os

# Valid states and union territories in India
valid_states = {
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
        "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
        "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
        "West Bengal", "Delhi", "Jammu & Kashmir", "Ladakh"
    }

class OrderRecord:
    def __init__(self, row):
        # Store the raw row from CSV
        self.row = row
        # Reason for invalid record, if any
        self.error_reason = None
        # Flag to indicate if record is valid
        self.valid = True
        # Dictionary to store processed and validated data
        self.processed_data = {}

    def validate(self):
        """Validate and process a single order record"""
        try:
            # Extract and clean fields from CSV row
            order_id = self.row.get("order_id", "").strip()
            customer_name = self.row.get("customer_name", "").strip()
            state = self.row.get("state", "").strip()
            product = self.row.get("product", "").strip()
            quantity = self.row.get("quantity", "").strip()
            price_per_unit = self.row.get("price_per_unit", "").strip()
            status = self.row.get("status", "").strip()

            # Check if row is completely empty
            if not any([order_id, customer_name, state, product, quantity, price_per_unit, status]):
                self.valid = False
                self.error_reason = "Empty row found"
                return

            # Customer name must not be empty
            if not customer_name:
                self.valid = False
                self.error_reason = "Customer not found"
                return

            # State must be in the valid_states set
            if state not in valid_states:
                self.valid = False
                self.error_reason = f"Invalid state: {state}"
                return

            # Validate quantity (must be a positive integer)
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
            except Exception:
                self.valid = False
                self.error_reason = "Invalid quantity"
                return

            # Validate price (must be a positive float)
            try:
                price_per_unit = float(price_per_unit)
                if price_per_unit <= 0:
                    raise ValueError("Price must be positive")
            except Exception:
                self.valid = False
                self.error_reason = "Invalid price"
                return

            # Normalize status to uppercase
            status = status.upper()

            # Calculate total amount
            total_amt = quantity * price_per_unit

            # Store processed data
            self.processed_data = {
                "order_id": order_id,
                "customer_name": customer_name,
                "state": state,
                "product": product,
                "quantity": quantity,
                "price_per_unit": price_per_unit,
                "status": status,
                "total_amount": total_amt
            }

        except Exception as e:
            # Catch any unexpected errors
            self.valid = False
            self.error_reason = f"Unexpected error: {e}"


class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        # Input raw CSV file
        self.input_file = input_file
        # Output file for valid orders
        self.processed_file = processed_file
        # Output file for invalid orders
        self.skipped_file = skipped_file
        # List of valid processed orders
        self.valid_orders = []
        # List of invalid/skipped orders
        self.invalid_orders = []

    def process_orders(self):
        """Read input CSV, validate orders, and separate valid/invalid ones"""
        if not os.path.exists(self.input_file):
            print(f"Error: file {self.input_file} not found")
            return

        try:
            with open(self.input_file, "r", newline="") as file:
                reader = csv.DictReader(file)

                # Ensure required columns exist in CSV
                required_columns = {
                    "order_id", "customer_name", "product",
                    "state", "status", "price_per_unit", "quantity"
                }
                if not required_columns.issubset(reader.fieldnames):
                    print("Missing required columns in CSV")
                    return

                # Process each row in CSV
                for row in reader:
                    order = OrderRecord(row)
                    order.validate()
                    if order.valid:
                        self.valid_orders.append(order.processed_data)
                    else:
                        skipped = row.copy()
                        skipped["Error Reason"] = order.error_reason
                        self.invalid_orders.append(skipped)

            # Write results to output files
            self.write_output()
        except Exception as e:
            print(f"Error processing file: {e}")

    def write_output(self):
        """Write valid and invalid orders to separate CSV files"""
        # Write valid orders
        with open(self.processed_file, "w", newline="") as outfile:
            fieldnames = [
                "order_id", "customer_name", "state", "product",
                "quantity", "price_per_unit", "status", "total_amount"
            ]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.valid_orders)

        with open(self.skipped_file, "w", newline="") as outfile:
            fieldnames = [
                "order_id", "customer_name", "state", "product",
                "quantity", "price_per_unit", "status", "Error Reason"
            ]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.invalid_orders)


        print("Processing completed")
        print(f"Processed orders: {len(self.valid_orders)}")
        print(f"Skipped orders: {len(self.invalid_orders)}")


if __name__ == "__main__":
    processor = OrderProcessor(
        "orders_raw(in).csv",          
        "orders_processed.csv",       
        "orders_skipped.csv"           
    )
    processor.process_orders()
