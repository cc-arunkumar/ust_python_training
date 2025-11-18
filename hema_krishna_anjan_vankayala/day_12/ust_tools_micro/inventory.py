from .csv_utils import read_csv,write_csv
from .validators import to_int
class Inventory:
    def __init__(self,items):
        for key,value in items.items():
            setattr(self,key,value) 
    
    def from_csv(path,item_id):
        li = read_csv(path)
        for i in li:
            if item_id in i.values():
                i['available_stock'] = to_int(i['available_stock'])
                invent = Inventory(i)
                return [True,invent] 
        return [False,'']
                
            
    def allocate(self,item_id,qty):
        if item_id == self.item_id and qty<= self.available_stock:
            self.available_stock -= qty
            return True 
        return False 

    def release(self,item_id,qty):
        if item_id == self.item_id:
            self.available_stock += qty 
            return True
        else:
            return False
            