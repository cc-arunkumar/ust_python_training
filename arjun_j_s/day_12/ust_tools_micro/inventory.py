from .csv_utils import read_csv

class Inventory:

    def inventory(self,items):
        self.datas={}
        for data in items:
            self.datas[data["item_id"]]=data["available_stock"]
    
    def from_csv(self,path):
        inventory_data = read_csv(path)
        self.inventory(inventory_data)

    def allocate(self,item_id,qty):
        try:
            if(self.datas[item_id]):
                if(int(self.datas[item_id])-qty < 0):
                    return False
                else:
                    return True
        except Exception as e:
            return False
    
    def release(self,item_id,qty):
        if(self.datas[item_id]):
            self.datas[item_id]+=qty
