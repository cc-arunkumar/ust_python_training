import csv
import os

# List of valid states for validation
VALID_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# -------------------------------
# OrderRecord class: represents a single order row and validates it
# -------------------------------
class OrderRecord:
    def __init__(self, row):
        self.row = row                  # Store raw row data from CSV
        self.error_reason = None        # Reason for invalid order (if any)
        self.valid = self.validate()    # Run validation immediately

    def validate(self):
        try:
            # Check customer name
            if not self.row.get("customer_name"):
                self.error_reason = "Missing customer_name"
                return False

            # Validate state
            if self.row.get("state") not in VALID_STATES:
                self.error_reason = "Invalid state"
                return False

            # Validate quantity
            try:
                self.row["quantity"] = int(self.row.get("quantity"))
                if self.row["quantity"] <= 0:
                    self.error_reason = "quantity must be positive"
                    return False
            except (ValueError, TypeError):
                self.error_reason = "quantity not a number"
                return False

            # Validate price per unit
            try:
                self.row["price_per_unit"] = abs(float(self.row.get("price_per_unit")))
                if self.row["price_per_unit"] <= 0:
                    self.error_reason = "price must be positive"
                    return False
            except (ValueError, TypeError):
                self.error_reason = "price not a number"
                return False

            # Calculate total amount
            self.row["total_amount"] = self.row["quantity"] * self.row["price_per_unit"]

            # Validate status
            if self.row.get("status"):
                self.row["status"] = self.row["status"].upper()  # Normalize to uppercase
            else:
                self.error_reason = "Missing status"
                return False

            return True  # All validations passed

        except Exception as e:
            # Catch any unexpected errors
            self.error_reason = str(e)
            return False

# -------------------------------
# OrderProcessor class: processes all orders from input file
# -------------------------------
class OrderProcessor:
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file            # Input raw orders file
        self.processed_file = processed_file    # Output file for valid orders
        self.skipped_file = skipped_file        # Output file for invalid orders
        self.processed_count = 0                # Counter for valid orders
        self.skipped_count = 0                  # Counter for invalid orders

    def process_order(self):
        # Open input and output files
        with open(self.input_file, newline="", encoding="utf-8") as infile, \
            open(self.processed_file, "w", newline="", encoding="utf-8") as valid_out, \
            open(self.skipped_file, "w", newline="", encoding="utf-8") as invalid_out:

            # Read input file with tab delimiter
            reader = csv.DictReader(infile, delimiter="\t")

            # Define headers for valid and invalid output files
            valid_fields = ["order_id", "customer_name", "state", "product",
                            "quantity", "price_per_unit", "total_amount", "status"]
            invalid_fields = ["order_id", "customer_name", "state", "product",
                              "quantity", "price_per_unit", "status", "error_reason"]

            # Create CSV writers
            valid_writer = csv.DictWriter(valid_out, fieldnames=valid_fields)
            invalid_writer = csv.DictWriter(invalid_out, fieldnames=invalid_fields)

            # Write headers to output files
            valid_writer.writeheader()
            invalid_writer.writeheader()

            # Process each row in input file
            for row in reader:
                order = OrderRecord(row)  # Validate order
                if order.valid:
                    valid_writer.writerow(order.row)   # Write valid order
                    self.processed_count += 1
                else:
                    row["error_reason"] = order.error_reason  # Add error reason
                    invalid_writer.writerow(row)             # Write invalid order
                    self.skipped_count += 1

        # Print summary after processing
        print(f"Processing complete: {self.processed_count} valid orders, {self.skipped_count} skipped orders.")

# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    # Create processor with input and output file paths
    processor = OrderProcessor("orders_raw.csv", "orders_processed.csv", "orders_skipped.csv")
    processor.process_order()  # Run processing
    
    
    #  if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$", v):
    #     raise ValueError("Invalid email format (must end with .com)")
    # return v 