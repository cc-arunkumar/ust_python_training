# Function to check if a row contains all the required fields and if those fields are not empty
def require_fields(row, fields):
    # Loop through each field in the required fields list
    for f in fields:
        # Check if the field is not in the row or if the field value is empty or contains only spaces
        if f not in row or row[f].strip() == "":
            return False 
    return True  

# Function to convert a value to an integer
def to_int(value):
    return int(value)  # Convert the input value to an integer and return it
