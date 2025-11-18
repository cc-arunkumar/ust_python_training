

def require_fields(row,field):
    try:
        for data in row:
            if data in field:
                if(len(str(row[data]).strip()) ==0):
                    return False
            else:
                return False
    except Exception as e:
        print(str(e))
        return False
    else:
        return True
    
def to_int(value):
    try:
        value = int(value)
    except ValueError:
        return False
    else:
        return value
