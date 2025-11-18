from .csv_utils import read_csv
#defining class
class Inventory:
    #constructor 
    def __init__(self,items):
        self.items=items 
    #class method so no object creation needed
    @classmethod
    def from_csv(cls,path):
        rows=read_csv(path)
        items={}
        
        for row in rows:
            item_id=row["item_id"]
            stock=int(row["available_stock"])
            items[item_id]=stock
        return cls(items)

    def allocate(self,item_id,qty):
        if item_id not in self.items:
            return False
        if self.items[item_id]<qty:
            return False

        self.items[item_id]-=qty
        return True

    def release(self,item_id,qty):
        if item_id in self.items:
            self.items[item_id]+=qty
        
