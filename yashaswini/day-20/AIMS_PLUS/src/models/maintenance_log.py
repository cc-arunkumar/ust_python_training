from pydantic import BaseModel, Field, model_validator
from datetime import date
from typing import Literal


class StatusValidate(BaseModel):
    """
    Model used to validate maintenance status updates.

    Attributes:
        status (Literal): Must be one of the predefined status values:
            - 'Completed'
            - 'Pending'
    """
    status: Literal['Completed', 'Pending']


class MaintenanceLog(BaseModel):
    """
    Model representing a maintenance log entry in the system.

    Attributes:
        asset_tag (str): Unique identifier for the asset. Must follow the pattern 'UST-<alphanumeric>'.
        maintenance_type (Literal): Type of maintenance performed. Allowed values: 'Repair', 'Service', 'Upgrade'.
        vendor_name (str): Name of the vendor. Only alphabets and spaces are allowed.
        description (str): Description of the maintenance activity. Must be at least 10 characters long.
        cost (float): Cost of maintenance. Must be greater than 0.
        maintenance_date (date): Date when the maintenance was performed. Cannot be in the future.
        technician_name (str): Name of the technician. Only alphabets and spaces are allowed.
        status (Literal): Current status of the maintenance. Allowed values: 'Completed', 'Pending'.
    """

    asset_tag: str = Field(..., pattern=r"^UST-[A-Za-z0-9-]+$")  # Enforces UST-prefixed asset tags
    maintenance_type: Literal['Repair', 'Service', 'Upgrade']
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Vendor name must contain only letters and spaces
    description: str = Field(..., min_length=10)  # Minimum length ensures meaningful description
    cost: float = Field(..., gt=0)  # Cost must be positive
    maintenance_date: date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")  # Technician name must contain only letters and spaces
    status: Literal['Completed', 'Pending']

    @model_validator(mode="after")
    def validate_maintenance_date(self):
        """
        Custom validator to ensure maintenance_date is not set in the future.

        Raises:
            ValueError: If maintenance_date is greater than today's date.

        Returns:
            MaintenanceLog: The validated model instance.
        """
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")
        return self