def require_fields(row: dict[str, str], fields: list[str]) -> bool:
    for field in fields:
        if field not in row or row[field].strip() == "":
            return False
    return True

def to_int(value: str) -> int:
    return int(value)
