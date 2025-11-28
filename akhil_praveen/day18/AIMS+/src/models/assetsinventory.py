from pydantic import BaseModel, Field, model_validator  # Import necessary classes from Pydantic for validation and modeling
from datetime import date  # Import date class to handle date-related functionalities
from typing import Optional, Literal  # Import Optional (for optional fields) and Literal (for specific string choices)

# StatusValidate model for validating the asset status field
class StatusValidate(BaseModel):
    # 'asset_status' field must be one of the specified literal values
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

# AssetInventory model to define the structure of an asset record
class AssetInventory(BaseModel):
    # 'asset_tag' field must match the given pattern (e.g., UST-XYZ123)
    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")
    
    # 'asset_type' field must be one of the specified literals
    asset_type: Literal['Laptop', 'Monitor', 'Keyboard', 'Mouse']
    
    # 'serial_number' field is required and must be a string
    serial_number: str
    
    # 'manufacturer' field must be one of the specified manufacturers
    manufacturer: Literal['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']
    
    # 'model' field is a string for the asset's model
    model: str
    
    # 'purchase_date' must be a date field (a required field)
    purchase_date: date
    
    # 'warranty_years' field must be between 1 and 5 years
    warranty_years: int = Field(..., ge=1, le=5)
    
    # 'condition_status' field must be one of the specified conditions
    condition_status: Literal['New', 'Good', 'Used', 'Damaged']
    
    # 'assigned_to' is an optional field for the person or department to whom the asset is assigned
    assigned_to: Optional[str] = None
    
    # 'location' field must be one of the specified locations
    location: Literal['TVM', 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']
    
    # 'asset_status' field must be one of the specified literals
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']
    
    # Validator to check that 'purchase_date' is not a future date
    @model_validator(mode="after")
    def validate_purchase_date(self):
        if self.purchase_date > date.today():  # Compare purchase date with today's date
            raise ValueError("purchase_date cannot be in the future")  # Raise error if the date is in the future
        return self
