def require_fields(row, fields):
    missing_fields = []
    for f in fields:
        if f not in row or row[f].strip() == "":
            missing_fields.append(f)
    
    if missing_fields:
        return False, missing_fields  
    return True, []  

def to_int(value):
   
    try:
        return int(value)
    except ValueError:
        return None  
