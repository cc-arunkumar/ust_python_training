from csv_utils import read_csv, write_csv

def to_int(value:str)->int|None:
    try:
        return int(value)
    except (TypeError,ValueError):
        return None
    
    

# data = read_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\order.csv")
def required_fileds(data: list[dict[str,str]], required_fields: list[str]) -> bool:
    for row in data:
        to_int(row.get("available_stock",""))
        for field in required_fields:
            if field not in row or row[field] == '':
                return False
    return True


# ans = required_fileds(data=data, required_fields=['item_id','available_stock'])
# print(ans)
