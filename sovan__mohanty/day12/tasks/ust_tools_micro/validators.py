# ust_tools_micro/validators.py

from typing import Dict, List

def require_fields(row: Dict[str, str], fields: List[str]) -> bool:
    for field in fields:
        if field not in row or row[field].strip() == "":
            return False
    return True


def to_int(value: str) -> int:
    return int(value)
