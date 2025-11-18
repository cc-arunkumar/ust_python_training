def require_fields(row,fields):
    #checking if all fields are required
    for f in fields:
        if f not in row or row[f].strip() == "":
            return False
    return True

def to_int(value):
    #converting to int
    return int(value)
