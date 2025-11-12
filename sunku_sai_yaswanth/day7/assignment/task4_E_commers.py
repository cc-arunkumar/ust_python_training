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
# be added easily late
class Product:
    def __init__(self,product_id , name , price):
        self.prodect_id=product_id
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self, product_id, name, price,brand , warranty_years):
        Product.__init__(self,product_id, name, price)
        self.brand=brand
        self.warraty_years=warranty_years
class Clothing(Product):
    def __init__(self, product_id, name, price,size , material):
        Product.__init__(self,product_id, name, price)
        self.size=size
        self.material=material
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date , is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_data=expiry_date
        self.is_organic=is_organic
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate):
        Product.__init__(self,product_id, name, price)
        self.discount_rate=discount_rate

    def apply_discount(self):
        dicount_rate=self.price-(self.discount_rate/100 )*self.price
        print(f"discount rate on product: {dicount_rate}")

discount=OnlineExclusiveProduct(101,"shirt",5000,0.2)
discount.apply_discount()

# output
# discount rate on product: 4990.0
        