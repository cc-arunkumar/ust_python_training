import csv
from .csv_utils import read_csv
class Inventory:
    def __init__(self,items):
        self.item=items
        
    
    def from_csv(self,path):
        with open(path,'r') as file:
            content=csv.DictReader(file)
            inventory=Inventory(content)
            return inventory
                
    
    def allocate(self,item_id:str,qty:int):
        for it in self.item:
            if item_id==it["item_id"] and int(it["available_stock"])>=qty:
                it["available_stock"]=(int(it["available_stock"])-qty)
                return True
        return False
    def release(self,item_id:str,qty:int):
        if item_id in self.item:
            self.item["available_stock"]=qty


        
        