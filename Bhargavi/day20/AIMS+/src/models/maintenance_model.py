import csv
from datetime import datetime, date
from pydantic import BaseModel, Field, model_validator
from typing import Optional

# -------------------------------
# Maintenance Log Model with Validations
# -------------------------------
class MaintenanceLogModel(BaseModel):
    # Defining fields for the maintenance log model
    log_id: Optional[int] = 0
    asset_tag: str = Field(..., description="Asset tag must start with 'UST-'")
    maintenance_type: str = Field(..., description="Must be 'Repair', 'Service', or 'Upgrade'")
    vendor_name: str = Field(..., description="Vendor name must only contain alphabets and spaces")
    description: str = Field(..., min_length=10, description="Description must have at least 10 characters")
    cost: float = Field(..., gt=0, description="Cost must be a positive number")
    maintenance_date: date = Field(..., description="Maintenance date cannot be in the future")
    technician_name: str = Field(..., description="Technician name must only contain alphabets and spaces")
    status: str = Field(..., description="Status must be 'Completed' or 'Pending'")

    # Model validator to check and validate the fields after initial validation
    @model_validator(mode="after")
    def validate_asset_tag(self):
        # Validate asset_tag starts with 'UST-'
        if not self.asset_tag.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        
        # Validate maintenance_type
        valid_types = ["Repair", "Service", "Upgrade"]
        if self.maintenance_type not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")

        # Validate vendor_name (only alphabets and spaces allowed)
        if any(char.isdigit() for char in self.vendor_name) or not all(char.isalpha() or char.isspace() for char in self.vendor_name):
            raise ValueError("vendor_name must only contain alphabets and spaces")

        # Validate cost (must be greater than 0)
        if self.cost <= 0:
            raise ValueError("cost must be greater than 0")

        # Validate maintenance_date (can't be in the future)
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be a future date")

        # Validate technician_name (only alphabets and spaces allowed)
        if any(char.isdigit() for char in self.technician_name) or not all(char.isalpha() or char.isspace() for char in self.technician_name):
            raise ValueError("technician_name must only contain alphabets and spaces")

        # Validate status (must be 'Completed' or 'Pending')
        if self.status not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")

        return self


# -------------------------------
# CSV Processing Logic
# -------------------------------
def process_maintenance_logs(input_file: str, output_file: str):
    processedlist = []  # List to store valid logs
    invalidlist = []    # List to store invalid logs

    # Correct file paths (convert backslashes to forward slashes for consistency)
    input_file = input_file.replace("\\", "/")
    output_file = output_file.replace("\\", "/")

    # Open and read the CSV file
    with open(input_file, "r") as file:
        content = csv.DictReader(file)  # Read CSV content as dictionaries
        for row in content:
            try:
                # Validate the row using Pydantic model
                maintenance_log = MaintenanceLogModel(**row)
                processedlist.append(maintenance_log)  # Add valid rows to the list
            except Exception as e:
                # Add invalid rows with error message to invalid list
                invalidlist.append({"row": row, "error": str(e)})

    # Print the count of valid and invalid rows
    print("Valid rows:", len(processedlist))
    print("Invalid rows:", len(invalidlist))

    # Write the valid rows to a new output CSV file
    with open(output_file, "w", newline="") as file:
        headers = [
            "log_id", "asset_tag", "maintenance_type", "vendor_name", "description",
            "cost", "maintenance_date", "technician_name", "status"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  # Write headers to output file
        for log in processedlist:
            log_data = log.model_dump()  # Use model_dump() to get data from Pydantic model
            writer.writerow(log_data)  # Write each valid log to CSV

# Main function to run the processing
if __name__ == "__main__":
    process_maintenance_logs(
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\maintenance_log.csv",  # Input CSV file path
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_maintenance_log.csv"  # Output CSV file path
    )
#output
# Valid rows: 92
# Invalid rows: 26