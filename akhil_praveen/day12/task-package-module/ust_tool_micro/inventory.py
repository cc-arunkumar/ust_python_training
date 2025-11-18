from csv_utils import read_csv

class Inventory:
        
        
    def inventory(self,data,header):
        self.dict = {}
        for row in data:
            dict[row[header[0]]] = row[header[1]]
    
    def from_csv(self,path):
        data,header = read_csv(path)
        self.inventory(data,header)
        
    def allocate(self,item_id,quantity):
        if self.dict[item_id] and self.dict[item_id]>0:
            self.dict[item_id] -=quantity
            return True
        else:
            return False
        
    def release(self,item_id,quantity):
        if self.dict[item_id]:
            self.dict[item_id] +=quantity
            return True
        else:
            return False