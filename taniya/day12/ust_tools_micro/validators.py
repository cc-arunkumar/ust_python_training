from .csv_utils import read_csv
def required_fields(row: dict[str, str], fields: list[str]) -> bool:
    return all(row.get(field, "").strip() for field in fields)

def to_integer(value):
    return int(value)