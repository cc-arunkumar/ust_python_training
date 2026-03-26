# Check if all required fields exist and are not empty
def required_fields(row, fields):
    for f in fields:
        if f not in row or row[f].strip() == "":
            return False
    return True

# Convert string to integer, raise ValueError if invalid
def to_int(value):
    try:
        return int(value)
    except Exception:
        raise ValueError