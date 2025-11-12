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
# Enterprise Tech Systems – Inheritance Design Challenge 3
# Ensure common attributes are reused and not redefined.


# Step 1: Define a base Product class with common attributes
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price

# Step 2: Create Electronics subclass with brand and warranty details
class Electronics(Product):
    def __init__(self, product_id, name, price,brand,warranty_years):
        Product.__init__(self,product_id,name,price)
        self.brand=brand
        self.warranty_years=warranty_years

# Step 3: Create Clothing subclass with size and material attributes
class Clothing(Product):
    def __init__(self, product_id, name, price,size,material):
        Product.__init__(self,product_id, name, price)
        self.size=size
        self.material=material

# Step 4: Create Groceries subclass with expiry and organic status
class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date,is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic

# Step 5: Create OnlineExclusiveProduct subclass with discount functionality
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id,name,price,discount_rate):
        Product.__init__(self,product_id,name,price)
        self.discount_rate=discount_rate
    def apply_discount(self):
        discount=self.price-((self.discount_rate/100)*self.price)
        print(f"product id:",self.product_id)
        print(f"Name:",self.name)
        print(f"price:",self.price)
        print(f"Discount rate is:",discount)

# Step 6: Instantiate an online-exclusive product and apply discount
product=OnlineExclusiveProduct(1,"Ranga",200,5)
product.apply_discount()
# sample output
# product id: 1
# Name: Ranga
# price: 200
# Discount rate is: 190.0


        
        