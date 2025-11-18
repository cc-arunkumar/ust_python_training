def require_fields(row,fields):
    for item in fields:
        if item not in row:
                return False
    return True
def to_int(value:str):
    try:
        if value.isdigit()==False:
            raise ValueError 
        else:
           return int(value)
    except ValueError as ve:
        return f"Invalid value: ValueError"
    
