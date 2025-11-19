from typing import Dict,List

def require_fields(row:Dict[str,str], fields:list[str])->bool:
    for field in fields:
        if field in row and row.strip()!="":
            return True
            
def to_int(value:str)->int:
    try:
        value=int(value)
        return value
    except ValueError:
        raise ValueError("Invalid integer")
    
        
    
