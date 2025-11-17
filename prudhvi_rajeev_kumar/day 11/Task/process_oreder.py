import csv
# The list of all the valid indian states.
VALID_INDIAN_STATES = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
    'Kerala', 'Madhya Pradesh', 'Manipur', 'Meghalaya', 'Mizoram',
    'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi']

class OrderRecord:
    def __init__(self, row):
        self.row = row
        self.valid = False
        self.error_reason = None
        self.processed = None
        self.validate()

    def validate(self):
        try:
            # Checking for empty row.
            if not any(self.row.values()):
                raise ValueError("Empty row")

            # Customer name should not be blank.
            customer_name = self.row['customer_name'].strip()
            if not customer_name:
                raise ValueError("Customer name cannot be blank")

            # Checking the valid indian states.
            state = self.row['state'].strip()
            if state not in VALID_INDIAN_STATES:
                raise ValueError(f"Invalid state: {state}")

            # checking for the quantity to be positive integer.
            try:
                quantity = int(self.row['quantity'])
                if quantity <= 0:
                    raise ValueError("Quantity must be positive")
                elif quantity == '':
                    raise ValueError("The Quantity must have some value.")
            except Exception:
                raise ValueError(f"Invalid quantity: {self.row['quantity']}")

            # Price per unit
            if self.row['price_per_unit'].strip() == "":
                raise ValueError("Price per unit is blank")
            try:
                price_per_unit = float(self.row['price_per_unit'])
                if price_per_unit < 0:
                    price_per_unit = abs(price_per_unit)
                elif price_per_unit == 0:
                    raise ValueError("Price per unit must be positive")
            except Exception:
                raise ValueError(f"Invalid price_per_unit: {self.row['price_per_unit']}")

            # Compute total
            total_amount = quantity * price_per_unit

            # Normalize status
            status = self.row['status'].strip().upper()

            # Build processed record
            self.processed = {
                'order_id': self.row['order_id'],
                'customer_name': customer_name,
                'state': state,
                'product': self.row['product'],
                'quantity': quantity,
                'price_per_unit': price_per_unit,
                'total_amount': total_amount,
                'status': status
            }
            self.valid = True

        except ValueError as e:
            self.error_reason = str(e)

class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.valid_orders = []
        self.invalid_orders = []

    def read_and_process(self):
        with open(self.input_file, mode="r", newline="", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)
            required_columns = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status"]
            for col in required_columns:
                if col not in reader.fieldnames:
                    raise ValueError(f"Missing required column: {col}")

            for row in reader:
                order = OrderRecord(row)
                if order.valid:
                    self.valid_orders.append(order.processed)
                else:
                    row['error_reason'] = order.error_reason
                    self.invalid_orders.append(row)

    def write_outputs(self):
        # Writing all the valid orders to processed file.
        with open(self.processed_file, mode="w", newline="", encoding="utf-8") as outfile:
            fieldnames = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "total_amount", "status"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.valid_orders)

        # Writing all the invalid orders to skipped file.
        with open(self.skipped_file, mode="w", newline="", encoding="utf-8") as skipfile:
            fieldnames = ["order_id", "customer_name", "state", "product", "quantity", "price_per_unit", "status", "error_reason"]
            writer = csv.DictWriter(skipfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.invalid_orders)


if __name__ == "__main__":
    processor = OrderProcessor("orders_raw.csv", "orders_processed.csv", "orders_skipped.csv")
    processor.read_and_process()
    processor.write_outputs()
    print(f"Processed Orders: {len(processor.valid_orders)}")
    print(f"Skipped Orders: {len(processor.invalid_orders)}")


#Sample Output:
# Processed Orders: 89
# Skipped Orders: 61

