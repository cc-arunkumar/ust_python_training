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
import datetime
# Define the Product class
class Product:
    def __init__(self,product_id,name,price):
        self.product_id = product_id
        self.name = name 
        self.price = price 
        
    # Method to display product details
    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: Rs.{self.price}\n")

# Define the Electronics class

class Electronics(Product):
    def __init__(self,product_id,name,price,brand,warranty_years):
        Product.__init__(self,product_id,name,price)
        self.brand = brand 
        self.warranty_years = warranty_years

# Define the Clothing class
class Clothing(Product):
    def __init__(self,product_id,name,price,size , material):
        Product.__init__(self,product_id,name,price)
        self.size = size 
        self.material = material

# Define the Groceries class     
class Groceries(Product):
    def __init__(self,product_id,name,price,expiry_date , is_organic):
        Product.__init__(self,product_id,name,price)
        self.expiry_date = expiry_date 
        self.is_organic = is_organic
        
# Define the OnlineExclusiveProduct class     
class OnlineExclusiveProduct(Product):
    def __init__(self,product_id,name,price,discount_rate):
        Product.__init__(self,product_id,name,price)
        self.discount_rate = discount_rate
        
# Method: apply_discount()
    def apply_discount(self):
        self.price -= self.price * (self.discount_rate/100) 
        print(f"Discounted Price for {self.name}: {self.price}")      
    
product1 = Product("P01","Laptop", 1200)
tshirt = Clothing(102, "Graphic T-Shirt", 250, "L", "Cotton")
apple = Groceries(103, "Red Apple", 50, datetime.date(2025, 12, 25), True)
exclusive_watch = OnlineExclusiveProduct(104, "Smart Watch", 299,50)

product1.display_info()
tshirt.display_info()
apple.display_info()
exclusive_watch.display_info()
exclusive_watch.apply_discount()

#Sample Output 
# Product Name: Laptop
# Price: Rs.1200

# Product Name: Graphic T-Shirt
# Price: Rs.250

# Product Name: Red Apple
# Price: Rs.50

# Product Name: Smart Watch
# Price: Rs.299

# Discounted Price for Smart Watch: 149.5