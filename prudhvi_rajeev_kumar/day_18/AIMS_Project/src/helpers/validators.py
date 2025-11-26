from datetime import date

VALID_ASSET_TYPES = {"Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"}
VALID_STATUS = {"Available", "Assigned", "Repair", "Retired"}

def validate_asset_tag(asset_tag : str) -> None:
    if not asset_tag.startswith("UST-"):
        raise ValueError("The asset Tag must start with UST-")

def validate_asset_type(asset_type : str) -> None:
    if asset_type not in VALID_ASSET_TYPES:
        raise ValueError("The asset type must be in the Valid Asset Type.")
    
def validate_asset_status(asset_status : str) -> None:
    if asset_status not in VALID_STATUS:
        raise ValueError("The asset status must be Valid.")

def validate_warranty_years(warranty_years : int) -> None:
    if not isinstance(warranty_years, int) or warranty_years <= 0:
        raise ValueError("The warranty years should be an integer and greater than 0.")
    
def validate_purchase_date(purchase_date: str) -> None:
    try:
        y, m, d = map(int, purchase_date.split("-"))
        pd = date(y, m, d)
        if pd > date.today():
            raise ValueError("Purchase date cannot be in the future.")
    except Exception:
        raise ValueError("Purchase date must be in YYYY-MM-DD format.")
        
def validate_assignment_rules(asset_status : str , assigned_to : str | None) -> None:
    if asset_status == "Assigned":
        if assigned_to is None or str(assigned_to).strip() == "":
            raise ValueError("Assigned asset must have a non-empty assigned_to.")
    elif asset_status in {"Available", "Retired"}:
        if assigned_to is not None and str(assigned_to).strip() != "":
            raise ValueError("Available/Retired assets cannot have assigned_to.")

def validate_asset_inputs(
    asset_tag: str,
    asset_type: str,
    serial_number: str,
    manufacturer: str,
    model: str,
    purchase_date: str,
    warranty_years: int,
    assigned_to: str | None,
    asset_status: str,
) -> None:
    
    validate_asset_tag(asset_tag)
    validate_asset_type(asset_type)
    validate_asset_status(asset_status)
    validate_warranty_years(warranty_years)
    validate_purchase_date(purchase_date)
    validate_assignment_rules(asset_status, assigned_to)

    # Basic required fields
    if not serial_number or not manufacturer or not model:
        raise ValueError("serial_number, manufacturer, and model are required.")