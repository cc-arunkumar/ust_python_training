from typing import Dict, List


def require_fields(row: Dict[str, str], fields: List[str]) -> bool:
    for field in fields:
        if field not in row:
            return False
        value = row.get(field)
        if value is None or str(value).strip() == "":
            return False
    return True


def to_int(value: str) -> int:
    return int(value)
