
def require_fields(row,fields):
    for field in fields:
        if row[field].strip() == "":
            return False 
    return True 

def to_int(value):
    try:
        value = int(value)
    except Exception:
        raise ValueError
    return value 

      