#Task 4 : Ecommerce Platform 

#Code 
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name = name
        self.price =price
        
class Electronics(Product):
    def __init__(self, product_id, name, price,brand,warranty_years):
        Product.__init__(self,product_id, name, price)
        self.brand=brand
        self.warranty_years=warranty_years
        
class Clothing(Product):
    def __init__(self, product_id, name, price,size,material):
        Clothing.__init__(self,product_id, name, price)
        self.size=size
        self.material=material
        
class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date,is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_date =expiry_date
        self.is_organic= is_organic
        
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate=discount_rate
        
    def apply_discount(self):
        print(f"Product_id : {self.product_id}")
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")
        print(f"Price after discount of {self.discount_rate} is : {self.price - (self.price * self.discount_rate)}:")
ecom1=OnlineExclusiveProduct(102,"sohan",4000,0.05)
ecom1.apply_discount()

#Output
# Product_id : 102
# Product Name : sohan
# Product Price : 4000
# Price after discount of 0.05 is : 3800.0:
        