from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Optional, Literal


class StatusValidate(BaseModel):
    """
    Model used to validate asset status updates.

    Attributes:
        asset_status (Literal): Must be one of the predefined status values:
            - 'Available'
            - 'Assigned'
            - 'Repair'
            - 'Retired'
    """
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']


class AssetInventory(BaseModel):
    """
    Model representing an asset in the inventory system.

    Attributes:
        asset_tag (str): Unique identifier for the asset. Must follow the pattern 'UST-<alphanumeric>'.
        asset_type (Literal): Type of asset. Allowed values: 'Laptop', 'Monitor', 'Keyboard', 'Mouse'.
        serial_number (str): Manufacturer-provided serial number.
        manufacturer (Literal): Manufacturer name. Allowed values: 'Dell', 'HP', 'Lenovo', 'Samsung', 'LG'.
        model (str): Model name/number of the asset.
        purchase_date (date): Date when the asset was purchased. Cannot be in the future.
        warranty_years (int): Warranty period in years. Must be between 1 and 5.
        condition_status (Literal): Current condition of the asset. Allowed values: 'New', 'Good', 'Used', 'Damaged'.
        assigned_to (Optional[str]): Name of the employee the asset is assigned to. Defaults to None.
        location (Literal): Physical location of the asset. Allowed values: 'TVM', 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad'.
        asset_status (Literal): Current status of the asset. Allowed values: 'Available', 'Assigned', 'Repair', 'Retired'.
    """

    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")  # Enforces UST-prefixed asset tags
    asset_type: Literal['Laptop', 'Monitor', 'Keyboard', 'Mouse']
    serial_number: str
    manufacturer: Literal['Dell', 'HP', 'Lenovo', 'Samsung', 'LG']
    model: str
    purchase_date: date
    warranty_years: int = Field(..., ge=1, le=5)  # Warranty must be between 1 and 5 years
    condition_status: Literal['New', 'Good', 'Used', 'Damaged']
    assigned_to: Optional[str] = None
    location: Literal['TVM', 'Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']
    asset_status: Literal['Available', 'Assigned', 'Repair', 'Retired']

    @model_validator(mode="after")
    def validate_purchase_date(self):
        """
        Custom validator to ensure purchase_date is not set in the future.

        Raises:
            ValueError: If purchase_date is greater than today's date.

        Returns:
            AssetInventory: The validated model instance.
        """
        if self.purchase_date > date.today():
            raise ValueError("purchase_date cannot be in the future")
        return self