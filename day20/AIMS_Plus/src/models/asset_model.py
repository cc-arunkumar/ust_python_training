import csv
import re
from datetime import datetime, date
from pydantic import BaseModel, Field

# -----------------------------
# Predefined validation sets
# -----------------------------
predefined_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}          # Allowed asset types
manufacturerlist = {"Dell", "HP", "Lenovo", "Samsung", "LG"}           # Allowed manufacturers
allowed_conditions = {"New", "Good", "Used", "Damaged"}                # Allowed condition statuses
approved_locations = {"Trivandrum", "Bangalore", "Hyderabad", "Chennai"}  # Allowed locations
allowed_status = {"Available", "Assigned", "Repair", "Retired"}        # Allowed asset statuses


# -----------------------------
# AssetInventory Model
# -----------------------------
class AssetInventory(BaseModel):
    """
    Pydantic model for validating asset inventory records.
    Each field is validated against predefined rules.
    """
    asset_tag: str = Field(..., pattern=r"^UST-")   # Must start with "UST-"
    asset_type: str
    serial_number: str
    manufacturer: str
    model: str
    purchase_date: date
    warranty_years: int
    condition_status: str
    assigned_to: str | None = None
    location: str
    asset_status: str

    def __init__(self, **data):
        """
        Override __init__ to run custom validation methods
        after Pydantic's built-in validation.
        """
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

    # -----------------------------
    # Custom validation methods
    # -----------------------------
    def validate_asset_type(self):
        if self.asset_type not in predefined_types:
            raise ValueError(f"Invalid asset_type: {self.asset_type}")

    def validate_serial_number(self):
        if not re.match(r"^[A-Za-z0-9-]+$", self.serial_number):
            raise ValueError(f"Invalid serial_number: {self.serial_number}")

    def validate_manufacturer(self):
        if self.manufacturer not in manufacturerlist:
            raise ValueError(f"Invalid manufacturer: {self.manufacturer}")

    def validate_model(self):
        if not self.model.strip():
            raise ValueError("Model cannot be empty")

    def validate_purchase_date(self):
        if self.purchase_date > datetime.today().date():
            raise ValueError("Purchase date cannot be in the future")

    def validate_warranty_years(self):
        if not (1 <= self.warranty_years <= 5):
            raise ValueError("Warranty years must be between 1 and 5")

    def validate_condition_status(self):
        if self.condition_status not in allowed_conditions:
            raise ValueError(f"Invalid condition_status: {self.condition_status}")

    def validate_assigned_to(self):
        if self.assigned_to and len(self.assigned_to.strip()) < 2:
            raise ValueError("Assigned_to must be a valid name")

    def validate_location(self):
        if self.location not in approved_locations:
            raise ValueError(f"Invalid location: {self.location}")

    def validate_asset_status(self):
        if self.asset_status not in allowed_status:
            raise ValueError(f"Invalid asset_status: {self.asset_status}")


# -----------------------------
# Function: Process assets from CSV
# -----------------------------
def process_assets(input_file: str, output_file: str):
    """
    Reads raw asset data from a CSV file, validates each row using AssetInventory,
    separates valid and invalid rows, and writes valid rows to a new CSV file.
    """
    processedlist = []  # Valid assets
    invalidlist = []    # Invalid assets with error details

    # Step 1: Read input CSV
    with open(input_file, "r") as file:
        content = csv.DictReader(file)
        for row in content:
            try:
                # Validate row using AssetInventory model
                asset = AssetInventory(**row)  
                processedlist.append(asset)
            except Exception as e:
                # Capture invalid rows with error message
                invalidlist.append({"row": row, "error": str(e)})

    # Step 2: Print summary
    print("Valid rows:", len(processedlist))
    print("Invalid rows:", len(invalidlist))

    # Step 3: Write valid rows to output CSV
    with open(output_file, "w", newline="") as file:
        headers = [
            "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
            "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for asset in processedlist:
            writer.writerow(asset.__dict__)  # Write validated asset data


# -----------------------------
# Run the script
# -----------------------------
if __name__ == "__main__":
    process_assets(
        "C:/Users/Administrator/Documents/Himavarsha/ust_python_training/himavarsha/day20/AIMS_Plus/database/sampledata/raw_csv/asset_inventory_raw.csv",
        "C:/Users/Administrator/Documents/Himavarsha/ust_python_training/himavarsha/day20/AIMS_Plus/database/sampledata/final_csv/valid_asset.csv"
    )
