# validators.py

def require_fields(row: dict[str, str], fields: list[str]) -> bool:
    """Return True if all required fields exist and are not empty."""
    for f in fields:
        if f not in row or row[f].strip() == "":
            return False
    return True

def to_int(value: str) -> int:
    """Convert string to integer. Let ValueError propagate on failure."""
    return int(value)
