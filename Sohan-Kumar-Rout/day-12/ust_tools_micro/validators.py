from typing import Dict, List

def require_fields(row: Dict[str, str], fields: List[str]) -> bool:

    for field in fields:
        if field not in row or row[field].strip() == "":
            return False
    return True


#String value to int value 
def to_int(value: str) -> int:
    return int(value)

