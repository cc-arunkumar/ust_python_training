#validators.py
# Create a require fields  method
def require_fields(row, fields):
    for field in fields:
        if field not in row or row[field].strip() == "":
            raise ValueError(f"Missing required field: {field}")
    return True
    
def to_int(value):
    try:
        return int(value)
    except ValueError :
        print("Error: Doesn't convert to int")

    