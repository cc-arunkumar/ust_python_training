from typing import List

def require_fields(row:dict,fields:List[str])->bool:
    return all(row.get(field) and row[field].strip() for field in fields)

def to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Cannot convert '{value}' to integer")