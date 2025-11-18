from ust_tools_micro.class_utils import read_csv


data = read_csv(r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day 12\data\orders.csv")
def required_feilds(row : dict[str, str], fields: list[str]) -> bool:
    for row in data:
        to_int(row.get("available_stock", ""))
        for field in fields:
            if field not in row or row[field] == '':
                return False
        
        return True

def to_int(value: str) -> str:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


    

    