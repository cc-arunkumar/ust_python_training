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
# Enterprise Tech Systems – Inheritance Design Challenge
# Ensure common attributes are reused and not redefined.

# main code:
# 1. Base entity → Product (with attributes: product_id , name , price )
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Category:{self.__class__.__name__}, Product ID:{self.product_id}, Name:{self.name}, Price:{self.price}")

# Subcategories
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def show_details(self):
        self.show_info()
        print(f"Brand:{self.brand}, Warranty:{self.warranty_years} years")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)
        self.size = size
        self.material = material

    def show_details(self):
        self.show_info()
        print(f"Size:{self.size}, Material:{self.material}")

class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def show_details(self):
        self.show_info()
        organic_status = "Organic" if self.is_organic else "Non-organic"
        print(f"Expiry Date:{self.expiry_date}, Organic:{organic_status}")

# Mixin for online exclusivity
class OnlineExclusive:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discount Applicable:{self.discount_rate}%, Original Price:{self.price}, Discounted Price:{discounted_price:.1f}")

# Hybrid classes
class OnlineExclusiveClothing(Clothing, OnlineExclusive):
    def __init__(self, product_id, name, price, size, material, brand, warranty_years, expiry_date, is_organic, discount_rate):
        Clothing.__init__(self, product_id, name, price, size, material)
        self.brand = brand
        self.warranty_years = warranty_years
        self.expiry_date = expiry_date
        self.is_organic = is_organic
        OnlineExclusive.__init__(self, discount_rate)

    def show_details(self):
        self.show_info()
        print(f"Brand:{self.brand}, Warranty:{self.warranty_years} years, Expiry Date:{self.expiry_date}, Organic:{self.is_organic}")
        print(f"Size:{self.size}, Material:{self.material}, Discount:{self.discount_rate}%")

# Sample objects
print("---Electronics---")
electronics = Electronics("E101", "Laptop", 75000, "Dell", 2)
electronics.show_details()

print("---Clothing---")
cloth = Clothing("C202", "T-Shirt", 999, "L", "Cotton")
cloth.show_details()

print("---Groceries---")
groceries = Groceries("G303", "Rice", 1200, "2026-01-01", True)
groceries.show_details()

print("---Online EXclusive Price---")
online= OnlineExclusiveClothing("O404", "Jacket", 3000, "M", "Leather", "Puma", 1, "NA", False, 10)
online.show_details()
online.apply_discount()

#sample output
# ---Electronics---
# Category:Electronics, Product ID:E101, Name:Laptop, Price:75000
# Brand:Dell, Warranty:2 years
# ---Clothing---
# Category:Clothing, Product ID:C202, Name:T-Shirt, Price:999    
# Size:L, Material:Cotton
# ---Groceries---
# Category:Groceries, Product ID:G303, Name:Rice, Price:1200
# Expiry Date:2026-01-01, Organic:Organic
# ---Online EXclusive Price---
# Category:OnlineExclusiveClothing, Product ID:O404, Name:Jacket, Price:3000
# Brand:Puma, Warranty:1 years, Expiry Date:NA, Organic:False
# Size:M, Material:Leather, Discount:10%
# Discount Applicable:10%, Original Price:3000, Discounted Price:2700.0