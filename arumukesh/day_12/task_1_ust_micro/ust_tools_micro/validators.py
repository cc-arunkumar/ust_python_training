def require_fields(row: dict[str, str], fields: list[str]) -> bool:
    
    # Returns True only if all fields exist and are non-empty.
    
    return all(field in row and row[field].strip() for field in fields)


def to_int(value: str) -> int:
  
    # Convert string to integer. Let ValueError bubble up naturally.

    return int(value)
