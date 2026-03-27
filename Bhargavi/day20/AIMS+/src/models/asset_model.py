import csv
import re
from datetime import datetime, date
from pydantic import BaseModel, Field

# -------------------------------
# Allowed lists for validation
# -------------------------------
predefined_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}  # Allowed asset types
manufacturerlist = {"Dell", "HP", "Lenovo", "Samsung", "LG"}  # Allowed manufacturers
allowed_conditions = {"New", "Good", "Used", "Damaged"}  # Allowed asset conditions
approved_locations = {"Trivandrum", "Bangalore", "Hyderabad", "Chennai"}  # Approved locations
allowed_status = {"Available", "Assigned", "Repair", "Retired"}  # Allowed asset statuses

# -------------------------------
# AssetInventory Model
# -------------------------------
class AssetInventory(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-")  # asset_tag must start with 'UST-'
    asset_type: str  # Asset type (Laptop, Monitor, etc.)
    serial_number: str  # Serial number (alphanumeric and hyphen)
    manufacturer: str  # Manufacturer name
    model: str  # Model name
    purchase_date: date  # Date of purchase
    warranty_years: int  # Warranty years (1 to 5)
    condition_status: str  # Condition of the asset
    assigned_to: str | None = None  # Employee name the asset is assigned to (optional)
    location: str  # Location of the asset (e.g., Bangalore, Chennai)
    asset_status: str  # Status of the asset (Available, Assigned, etc.)

    # Constructor to validate fields after the model is initialized
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_asset_type()
        self.validate_serial_number()
        self.validate_manufacturer()
        self.validate_model()
        self.validate_purchase_date()
        self.validate_warranty_years()
        self.validate_condition_status()
        self.validate_assigned_to()
        self.validate_location()
        self.validate_asset_status()

    # Validator methods for each field
    def validate_asset_type(self):
        if self.asset_type not in predefined_types:
            raise ValueError(f"Invalid asset_type: {self.asset_type}")

    def validate_serial_number(self):
        if not re.match(r"^[A-Za-z0-9-]+$", self.serial_number):  # Valid serial number format
            raise ValueError(f"Invalid serial_number: {self.serial_number}")

    def validate_manufacturer(self):
        if self.manufacturer not in manufacturerlist:  # Check if manufacturer is valid
            raise ValueError(f"Invalid manufacturer: {self.manufacturer}")

    def validate_model(self):
        if not self.model.strip():  # Ensure model is not empty
            raise ValueError("Model cannot be empty")

    def validate_purchase_date(self):
        if self.purchase_date > datetime.today().date():  # Purchase date cannot be in the future
            raise ValueError("Purchase date cannot be in the future")

    def validate_warranty_years(self):
        if not (1 <= self.warranty_years <= 5):  # Warranty years must be between 1 and 5
            raise ValueError("Warranty years must be between 1 and 5")

    def validate_condition_status(self):
        if self.condition_status not in allowed_conditions:  # Validate condition status
            raise ValueError(f"Invalid condition_status: {self.condition_status}")

    def validate_assigned_to(self):
        if self.assigned_to and len(self.assigned_to.strip()) < 2:  # Ensure assigned_to is a valid name
            raise ValueError("Assigned_to must be a valid name")

    def validate_location(self):
        if self.location not in approved_locations:  # Check if location is valid
            raise ValueError(f"Invalid location: {self.location}")

    def validate_asset_status(self):
        if self.asset_status not in allowed_status:  # Validate asset status
            raise ValueError(f"Invalid asset_status: {self.asset_status}")

# -------------------------------
# CSV Processing Logic
# -------------------------------
def process_assets(input_file: str, output_file: str):
    processedlist = []  # List to store valid assets
    invalidlist = []  # List to store invalid rows

    # Open and read the input CSV file
    with open(input_file, "r") as file:
        content = csv.DictReader(file)  # Reading the CSV data into a dictionary
        for row in content:
            try:
                # Try creating an AssetInventory object (will validate automatically)
                asset = AssetInventory(**row)
                processedlist.append(asset)  # Add valid assets to the list
            except Exception as e:
                # If validation fails, add the row and error to invalid list
                invalidlist.append({"row": row, "error": str(e)})

    # Print number of valid and invalid rows
    print("Valid rows:", len(processedlist))
    print("Invalid rows:", len(invalidlist))

    # Write valid assets to the output CSV file
    with open(output_file, "w", newline="") as file:
        headers = [
            "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
            "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for asset in processedlist:
            # Write each asset to the output file
            writer.writerow(asset.__dict__)

# -------------------------------
# Run the processing
# -------------------------------
if __name__ == "__main__":
    # Call the function to process the assets
    process_assets(
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\asset_inventory.csv",  # Input file path
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_inventory.csv"  # Output file path
    )

# #output
# Valid rows: 62
# Invalid rows: 38