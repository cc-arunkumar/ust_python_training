import csv
class Inventory:
    def __init__(self,items):
        self.items = items
        
    def from_csv(self,path):
        with open(path,"r") as file:
            reader = csv.DictReader(file)
            for item in reader:
                if item["item_id"] == self.items["item_id"]:
                    return  Inventory(item)
            
    def allocate(self,item_id,qty):
        if int(self.items["available_stock"]) >= int(qty):
            self.items["available_stock"] = int(self.items["available_stock"]) + int(qty)
            return True
        else:
            return False
        
    # def release(self,qty):
    #     self.items["available_stock"] = int(self.items["available_stock"]) + int(qty)
     