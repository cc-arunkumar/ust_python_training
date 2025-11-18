

def required_fields(data,fields):
    for item in fields:
        if item not in data:
            return False
    return True

def to_int(value):
    try:
        return int(value)
    except ValueError as e:
        return e
    