def require_fields(row, fields):
    for field in fields:
        if field not in row or row[field].strip() == "":
            return False
    return True

def to_int(value):
    return int(value)
