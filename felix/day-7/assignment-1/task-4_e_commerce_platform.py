# Task 4 — E-Commerce Platform (Inventory System)
# Domain: Retail Tech
# Business Requirement:
# UST Digital Retail is developing an e-commerce backend system.
# 1. Base entity → Product (with attributes: product_id , name , price )
# 2. Subcategories:
# Electronics → extra: brand , warranty_years
# Clothing → extra: size , material
# Groceries → extra: expiry_date , is_organic
# 3. A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()

class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name
        self.price = price
        
# Electronics extends Product
class Electronics(Product):
    def __init__(self, product_id, name, price,brand,warrenty_year):
        Product.__init__(self,product_id, name, price)
        self.brand = brand
        self.warrenty_year = warrenty_year
   

# Clothing extends Product    
class Clothing(Product):
    def __init__(self, product_id, name, price,size,material):
        Product.__init__(self,product_id, name, price)
        self.size = size
        self.material = material
        
# Groceries extends Product     
class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date,is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic
    
# OnlineExclusiveProduct extends Product   
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate):
        Product.__init__(self,product_id, name, price)
        self.discount_rate = discount_rate
        self.price = price
        
    def apply_discount(self):
        print(f"{self.discount_rate}% discount is applied")
        print(f"New price : {self.price - self.price*self.discount_rate/100}")
        
# Creating objects for all class
p = Product(101,"Biscut",200)
e = Electronics(101,"Biscut",200,"Sunfiest",3)
c = Clothing(101,"Biscut",200,20,"Cotton")
g = Groceries(101,"Biscut",200,"25-12-26","yes")
        
product = OnlineExclusiveProduct(101,"Biscut",200,5)
product.apply_discount()
    
    
# output

# 5% discount is applied
# New price : 190.0