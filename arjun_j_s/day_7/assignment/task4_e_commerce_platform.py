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
# Task: Design a flexible inheritance structure so new product categories can
# be added easily later.

#Main class
class Product:

    def __init__(self,pro_id,name,price):
        self.pro_id = pro_id
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Product ID : {self.pro_id}")
        print(f"Name : {self.name}")
        print(f"Price : {self.price}")

#Sub-class
class Electronics(Product):

    def __init__(self, pro_id, name, price,brand,warranty_yr):
        Product.__init__(self,pro_id, name, price)
        self.brand = brand
        self.warranty_yr = warranty_yr

    def show_elec(self):
        self.show_info()
        print(f"Brand : {self.brand}")
        print(f"Warranty Year : {self.warranty_yr}")

#Sub-class
class Clothing(Product):

    def __init__(self, pro_id, name, price, size, material):
        Product.__init__(self,pro_id, name, price)
        self.size = size
        self.material = material
    
    def show_cloth(self):
        self.show_info()
        print(f"Size : {self.size}")
        print(f"Material : {self.material}")

#Sub-class
class Groceries(Product):

    def __init__(self, pro_id, name, price, exp_date, is_org):
        Product.__init__(self,pro_id, name, price)
        self.exp_date = exp_date
        self.is_org = is_org

    def show_gro(self):
        self.show_info()
        print(f"Expiry Date : {self.exp_date}")
        print(f"Is Organic : {self.is_org}")

#Sub-class
class OnlineExclusivePRoduct(Product):

    def __init__(self, pro_id, name, price):
        Product.__init__(self,pro_id, name, price)
        self.discount_rate = 0

    def apply_discount(self):
        self.show_info()
        self.discount_rate =self.price - self.price * 0.1
        print(f"Price after Discount  : {self.discount_rate}")

#Creating the object
exclu_prod = OnlineExclusivePRoduct(101,"Headset",1500)
exclu_prod.apply_discount()

#Output
# Product ID : 101
# Name : Headset
# Price : 1500
# Price after Discount  : 1350.0