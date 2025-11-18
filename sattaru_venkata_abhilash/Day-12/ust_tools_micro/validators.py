def require_fields(row, fields):
    # Loop through each required field name
    for field in fields:
        # Check if the field is missing OR the value is empty/blank
        if field not in row or row[field].strip() == "":
            return False   # Required field not found or invalid
    return True             # All required fields are present


def to_int(value):
    # Convert the given value to an integer
    # (Assumes value is numeric or numeric string)
    return int(value)