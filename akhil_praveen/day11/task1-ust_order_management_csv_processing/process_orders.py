import csv   # Import CSV module for reading/writing CSV files

# Custom exception classes
class ConversionError(Exception):
    pass

class BlankFields(Exception):
    pass

class InvalidStateNames(Exception):
    pass

class OrderRecord:
    
    def __init__(self, data):
        self.data = data   # Store row data
    
    def validate(self, count):
        # List of valid Indian states
        valid_states = {
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", 
            "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", 
            "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", 
            "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
        }

        # Validate row fields
        try:
            # Skip empty rows
            if not any(self.data.values()):
                raise BlankFields("Row is empty")

            for col in self.data:
                value = self.data[col].strip()
                
                # Validate quantity (must be positive integer)
                if col == "quantity":
                    if not value.isdigit() or int(value) <= 0:
                        raise ConversionError(f"Invalid quantity: {value}")
                
                # Validate price_per_unit (must be numeric)
                elif col == "price_per_unit":
                    try:
                        price = abs(float(value))
                    except ValueError:
                        raise ConversionError(f"Invalid price_per_unit (non-numeric): {value}")
                
                # Validate customer_name (cannot be blank)
                elif col == "customer_name" and not value:
                    raise BlankFields("Customer name is blank")
                
                # Validate state (must be in valid_states list)
                elif col == "state" and value not in valid_states:
                    raise InvalidStateNames(f"Invalid state: {value}")

        # Handle specific exceptions
        except BlankFields as e:
            return False, str(e)
        except ConversionError as e:
            return False, str(e)
        except InvalidStateNames as e:
            return False, str(e)
        except Exception as e:
            return False, f"Unknown error: {e}"
        
        return True, None   # Validation successful

class OrderProcessor:
    
    def __init__(self, input_file, processed_file, skipped_file):
        self.input_file = input_file
        self.processed_file = processed_file
        self.skipped_file = skipped_file
        self.processed_list = []   # Valid records
        self.skipped_list = []     # Invalid records
    
    def process_orders(self):
        try:
            # Read input CSV file
            with open(self.input_file, "r") as file:
                csv_reader = csv.DictReader(file)
                header = csv_reader.fieldnames + ['error_reason']  # Add error_reason for skipped records

                for row in csv_reader:
                    order = OrderRecord(row)
                    is_valid, error_reason = order.validate(len(self.processed_list) + len(self.skipped_list))
                    
                    if is_valid:
                        # Compute total_amount for valid records
                        row['total_amount'] = int(row['quantity']) * float(row['price_per_unit'])
                        row['status'] = row['status'].upper()  # Normalize status to uppercase
                        self.processed_list.append(row)
                    else:
                        # Add error reason for invalid records
                        row['error_reason'] = error_reason
                        self.skipped_list.append(row)

            # Write processed and skipped records to separate CSV files
            self._write_csv(self.processed_file, self.processed_list)
            self._write_csv(self.skipped_file, self.skipped_list)
        
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} was not found.")
        except Exception as e:
            print(f"An error occurred while processing orders: {e}")
        
        # Print summary
        print(f"Total data: {len(self.processed_list)+len(self.skipped_list)}")
        print(f"Total Processed data: {len(self.processed_list)}")
        print(f"Total Skipped data: {len(self.skipped_list)}")
        
    
    def _write_csv(self, filename, data):
        if data:
            with open(filename, "w", newline="") as file:
                csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(data)

# Usage
input_file = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day11/orders_raw.csv"
processed_file = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day11/data/orders_processed.csv"
skipped_file = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day11/data/orders_skipped.csv"

processor = OrderProcessor(input_file, processed_file, skipped_file)
processor.process_orders()

# ===========================
# Expected Output (example):
# ===========================
# Total data:  10
# Total Processed data:  7
# Total Skipped data:  3
