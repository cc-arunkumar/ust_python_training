import csv
import re
from datetime import datetime, date
from pydantic import BaseModel, Field

# -------------------------------
# Allowed lists for validation
# -------------------------------
predefined_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}
manufacturerlist = {"Dell", "HP", "Lenovo", "Samsung", "LG"}
allowed_conditions = {"New", "Good", "Used", "Damaged"}
approved_locations = {"Trivandrum", "Bangalore", "Hyderabad", "Chennai"}
allowed_status = {"Available", "Assigned", "Repair", "Retired"}

# -------------------------------
# AssetInventory Model
# -------------------------------
class AssetInventory(BaseModel):
    asset_tag: str = Field(..., pattern=r"^UST-")
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

# -------------------------------
# CSV Processing Logic
# -------------------------------
def process_assets(input_file: str, output_file: str):
    processedlist = []
    invalidlist = []

    # Corrected path formatting
    input_file = input_file.replace("\\", "/")  # Convert backslashes to forward slashes
    output_file = output_file.replace("\\", "/")

    with open(input_file, "r") as file:
        content = csv.DictReader(file)
        for row in content:
            try:
                # Parse purchase_date from string to date object if necessary
                if isinstance(row['purchase_date'], str):
                    row['purchase_date'] = datetime.strptime(row['purchase_date'], "%Y-%m-%d").date()
                # Validate with Pydantic model
                asset = AssetInventory(**row)
                processedlist.append(asset)
            except Exception as e:
                invalidlist.append({"row": row, "error": str(e)})

    print("Valid rows:", len(processedlist))
    print("Invalid rows:", len(invalidlist))

    with open(output_file, "w", newline="") as file:
        headers = [
            "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
            "purchase_date", "warranty_years", "condition_status",
            "assigned_to", "location", "asset_status"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for asset in processedlist:
            asset_data = asset.dict()
            # Ensure the date is correctly formatted before writing to CSV
            asset_data['purchase_date'] = asset_data['purchase_date'].strftime('%Y-%m-%d')
            writer.writerow(asset_data)


if __name__ == "__main__":
    # Use raw string format for file paths or double backslashes
    process_assets(
       r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\asset_inventory.csv", 
       r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\validated_asset_inventory.csv"
    )
