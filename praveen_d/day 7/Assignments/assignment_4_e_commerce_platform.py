# Task 4 — E-Commerce Platform (Inventory System)
# Domain: Retail Tech
# Business Requirement:
# UST Digital Retail is developing an e-commerce backend system.


# Task: Design a flexible inheritance structure so new product categories can
# be added easily later.
# Enterprise Tech Systems – Inheritance Design Challenge 3
# Ensure common attributes are reused and not redefined.

# 1. Base entity → Product (with attributes: product_id , name , price )
class Product:
    def __init__(self,product_id , name , price ):
        self.product_id=product_id
        self.name=name
        self.price=price

    def get_product_info(self):
        print(f"Product ID:{self.product_id}")
        print(f"Product name:{self.name}")
        print(f"product price:{self.price}")

# 2. Subcategories:
# Electronics → extra: brand , warranty_years
class Electronics(Product):
    def __init__(self, product_id, name, price, brand , warranty_years):
        super().__init__(product_id, name, price)
        self.brand=brand
        self.warranty_years=warranty_years
    
    def electronics_info(self):
         print(f"Product ID:{self.product_id}")
         print(f"Product name:{self.name}")
         print(f"product price:{self.price}")
         print(f"Product Brand:{self.brand}")
         print(f"Product Warrenty:{self.warranty_years}")
    
# Clothing → extra: size , material
class Clothing(Product):
    def __init__(self, product_id, name,price,size,material):
        super().__init__(product_id, name, price)
        self.size=size
        self.material=material

    def clothing_info(self):
         print(f"Product ID:{self.product_id}")
         print(f"Product name:{self.name}")
         print(f"product price:{self.price}")
         print(f"Product Size:{self.size}")
         print(f"Product Material:{self.material}")

# Groceries → extra: expiry_date , is_organic
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date , is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic

    def groceries_info(self):
             print(f"Product ID:{self.product_id}")
             print(f"Product name:{self.name}")
             print(f"product price:{self.price}")
             print(f"Product Expiry_date:{self.expiry_date}")
             print(f"Product is_organic:{self.is_organic}")

# 3. A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()

class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate ):
        super().__init__(product_id, name, price)
        self.discount_rate=discount_rate
    
    def apply_discount(self):
        discount=self.price*self.discount_rate
        print(f"The total discount for the product{self.product_id} is {discount}")


# Electronics
electronic_item = Electronics("E101", "Smartphone", 25000, "Samsung", 2)
print("---------Electronics Product-------")
electronic_item.electronics_info()

# Clothing
clothing_item = Clothing("C201", "Tracks", 799, "L", "Cotton")
print("\n--- Clothing Product ---")
clothing_item.clothing_info()

# Groceries
grocery_item = Groceries("G301", "Rice", 399, "2026-01-01", True)
print("\n--- Grocery Product ---")
grocery_item.groceries_info()

# Online Exclusive Product
online_item = OnlineExclusiveProduct("O401", "Wireless Earbuds", 2999, 0.10)
print("\n--- Online Exclusive Product ---")
online_item.get_product_info()
online_item.apply_discount()


# Sample Output
# ---------Electronics Product-------
# Product ID:E101
# Product name:Smartphone
# product price:25000
# Product Brand:Samsung
# Product Warrenty:2

# --- Clothing Product ---
# Product ID:C201
# Product name:Tracks
# product price:799
# Product Size:L
# Product Material:Cotton

# --- Grocery Product ---
# Product ID:G301
# Product name:Rice
# product price:399
# Product Expiry_date:2026-01-01
# Product is_organic:True

# --- Online Exclusive Product ---
# Product ID:O401
# Product name:Wireless Earbuds
# product price:2999
# The total discount for the productO401 is 299.90000000000003
