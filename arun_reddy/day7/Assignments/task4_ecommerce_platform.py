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
# ⚙️ Task: Design a flexible inheritance structure so new product categories can
# be added easily later.

class Product:
    def __init__(self,product_id , name , price):
        self.product_id=product_id
        self.name=name
        self.price=price
# Electronics extends Product 
class Electonics(Product):
    def __init__(self, product_id, name, price,brand , warranty_years):
        Product.__init__(self,product_id, name, price)
        self.brand=brand
        self.warranty_years=warranty_years
# Clothing extends Product
class Clothing(Product):
    def __init__(self, product_id, name, price,size , material):
        Product.__init__(self,product_id, name, price)
        self.size=size
        self.material=material

# Groceries extends Product
class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date , is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic
# OnlineExclusiveProduct extends Product
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate):
        Product.__init__(self,product_id, name, price)
        self.discount_rate=discount_rate
        self.price=price
    def apply_discount(self):
        print(f"the {self.discount_rate} percent discount valiue is {(self.discount_rate/100)*self.price}")
    
    
# creating the object and calling 
onexclpdt=OnlineExclusiveProduct(9876,"TV",78000,50)
onexclpdt.apply_discount()


# sample execution
# the 50 percent discount valiue is 39000.0