class Inventory:
    def __init__(self,item):
        for key,value in item.items():
            setattr(self,key,value)
        self.available_stock=int(self.available_stock)
# class Method:
    # def from_csv(self,path):
    #     with open(path,"r") as file:
    #         reader=csv.DictReader(file)
    #         for row in reader:
    #             self.i=Inventory(row)
    
    def allocate(self,item_id,qty):
        if self.available_stock>=qty:
            self.available_stock-=qty
            return True
        else : return False 
    
    def release(self,item_id,qty):
        item_id.available_stock+=qty
        