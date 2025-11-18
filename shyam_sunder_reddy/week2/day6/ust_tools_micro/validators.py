

class Order:
    def __init__(self,dict):
        # print(dict)
        for key,value in dict.items():
            setattr(self, key, value)


    def validate_order(self):
        try:
            if self.order_id.strip()=="" or self.item_id.strip()=="" or self.quantity.strip()=="":
                raise Exception
        except Exception:
            print("INVALID ORDER:",self)
            return False
            
        try:
            self.quantity=int(self.quantity)
        except:
            print("Invalid Quantity")
            return False
        return True