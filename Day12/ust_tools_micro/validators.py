# ust_tools_micro/validators.py

def require_fields(row, fields):
    for f in fields:
        if f not in row:
            return False

        value = row[f]

        if value is None or value.strip() == "":
            return False

    return True


def to_int(value):
    return int(value)
