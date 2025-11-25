from csv_utils import read_csv, write_csv   # Import helper functions for reading/writing CSV

# Utility function to safely convert a string to integer
def to_int(value: str) -> int | None:
    try:
        return int(value)   # Try converting to integer
    except (TypeError, ValueError):
        return None         # Return None if conversion fails
        

# Function to check if required fields exist and are non-empty in each row
def required_fileds(data: list[dict[str, str]], required_fields: list[str]) -> bool:
    for row in data:   # Iterate through each row (dict) in the CSV data
        to_int(row.get("available_stock", ""))   # Attempt conversion (not used further here)
        for field in required_fields:   # Check each required field
            if field not in row or row[field] == '':
                return False   # Fail immediately if field missing or empty
    return True   # Return True if all rows contain required fields
