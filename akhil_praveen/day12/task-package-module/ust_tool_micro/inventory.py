from .csv_utils import read_csv

class Inventory:
        
        
    def inventory(self,data,header):
        self.dict = {}
        for row in data:
            self.dict[row[header[0]]] = int(row[header[1]])
    
    def from_csv(self,path):
        data,header = read_csv(path)
        self.inventory(data,header)
        
    def allocate(self,item_id,quantity):
        if self.dict[item_id]:
            self.dict[item_id] -=quantity
            if self.dict[item_id]>=0:
                print(f"ALLOCATED: {item_id} -> {item_id} ({quantity})")
            else:
                print(f"FAILED: {item_id} -> {item_id} ({quantity})")
                self.dict[item_id] +=quantity
        else:
            print(f"{item_id} doesn't exists")
        
    def release(self,item_id,quantity):
        if self.dict[item_id]:
            self.dict[item_id] +=quantity
            print(f"{item_id} released successfully")