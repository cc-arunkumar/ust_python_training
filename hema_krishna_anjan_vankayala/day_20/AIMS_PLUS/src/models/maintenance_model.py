from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Optional
import re

class MaintenanceLog(BaseModel):
    # Core maintenance log fields
    log_id: Optional[int] = None
    asset_tag: str = Field(..., pattern=r'^UST-')        # Must start with UST-
    maintenance_type: str                                # Repair/Service/Upgrade
    vendor_name: str                                     # Alphabets only
    description: str                                     # Minimum 10 characters
    cost: Decimal                                        # > 0, exactly two decimals
    maintenance_date: date                               # Cannot be in the future
    technician_name: str                                 # Alphabets only
    status: str                                          # Completed/Pending

    # Validation methods
    def validation_asset_tag(self):
        if not re.match(r'^UST-', self.asset_tag):
            raise ValueError("asset_tag must start with 'UST-'")

    def validation_maintenance_type(self):
        if self.maintenance_type not in ['Repair', 'Service', 'Upgrade']:
            raise ValueError("maintenance_type must be one of: Repair, Service, Upgrade")

    def validation_vendor_name(self):
        if not re.match(r'^[A-Za-z ]+$', self.vendor_name):
            raise ValueError("vendor_name must contain only alphabets and spaces")

    def validation_description(self):
        if not isinstance(self.description, str) or len(self.description.strip()) < 10:
            raise ValueError("description must be at least 10 characters")

    def validation_cost(self):
        try:
            d = Decimal(str(self.cost))
        except (InvalidOperation, ValueError, TypeError):
            raise ValueError("cost must be a decimal number")
        try:
            quant = d.quantize(Decimal('0.01'))
        except InvalidOperation:
            raise ValueError("cost must have at most two decimal places")
        if quant != d:
            raise ValueError("cost must have exactly two decimal places")
        if d <= 0:
            raise ValueError("cost must be greater than 0")

    def validation_maintenance_date(self):
        if self.maintenance_date > date.today():
            raise ValueError("maintenance_date cannot be in the future")

    def validation_technician_name(self):
        if not re.match(r'^[A-Za-z ]+$', self.technician_name):
            raise ValueError("technician_name must contain only alphabets and spaces")

    def validation_status(self):
        if self.status not in ['Completed', 'Pending']:
            raise ValueError("status must be either 'Completed' or 'Pending'")

    # Run validations on initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validation_asset_tag()
        self.validation_maintenance_type()
        self.validation_vendor_name()
        self.validation_description()
        self.validation_cost()
        self.validation_maintenance_date()
        self.validation_technician_name()
        self.validation_status()
