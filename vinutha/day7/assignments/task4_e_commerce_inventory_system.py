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

# 1. Base entity → Product
# Every product has: product_id, name, price
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    # Method to display basic product info
    def show_info(self):
        print(f"Category:{self.__class__.__name__}, Product ID:{self.product_id}, Name:{self.name}, Price:{self.price}")


# 2. Electronics subclass (inherits from Product)
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        # Initialize base Product attributes
        Product.__init__(self, product_id, name, price)
        # Add electronics-specific attributes
        self.brand = brand
        self.warranty_years = warranty_years

    def show_details(self):
        # Show base info + electronics details
        self.show_info()
        print(f"Brand:{self.brand}, Warranty:{self.warranty_years} years")


# 3. Clothing subclass (inherits from Product)
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        # Initialize base Product attributes
        Product.__init__(self, product_id, name, price)
        # Add clothing-specific attributes
        self.size = size
        self.material = material

    def show_details(self):
        # Show base info + clothing details
        self.show_info()
        print(f"Size:{self.size}, Material:{self.material}")


# 4. Groceries subclass (inherits from Product)
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        # Initialize base Product attributes
        Product.__init__(self, product_id, name, price)
        # Add grocery-specific attributes
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def show_details(self):
        # Show base info + grocery details
        self.show_info()
        organic_status = "Organic" if self.is_organic else "Non-organic"
        print(f"Expiry Date:{self.expiry_date}, Organic:{organic_status}")


# 5. Mixin class for Online Exclusive products
class OnlineExclusive:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    # Method to apply discount on price
    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discount Applicable:{self.discount_rate}%, Original Price:{self.price}, Discounted Price:{discounted_price:.1f}")


# 6. Hybrid class → OnlineExclusiveClothing
# Combines Clothing + OnlineExclusive features
class OnlineExclusiveClothing(Clothing, OnlineExclusive):
    def __init__(self, product_id, name, price, size, material, brand, warranty_years, expiry_date, is_organic, discount_rate):
        # Initialize Clothing attributes
        Clothing.__init__(self, product_id, name, price, size, material)
        # Add extra attributes (brand, warranty, expiry, organic status)
        self.brand = brand
        self.warranty_years = warranty_years
        self.expiry_date = expiry_date
        self.is_organic = is_organic
        # Initialize OnlineExclusive attributes
        OnlineExclusive.__init__(self, discount_rate)

    def show_details(self):
        # Show combined details from Clothing + OnlineExclusive
        self.show_info()
        print(f"Brand:{self.brand}, Warranty:{self.warranty_years} years, Expiry Date:{self.expiry_date}, Organic:{self.is_organic}")
        print(f"Size:{self.size}, Material:{self.material}, Discount:{self.discount_rate}%")


# ---------------- Sample Objects ----------------
print("---Electronics---")
electronics = Electronics("E101", "Laptop", 75000, "Dell", 2)
electronics.show_details()

print("---Clothing---")
cloth = Clothing("C202", "T-Shirt", 999, "L", "Cotton")
cloth.show_details()

print("---Groceries---")
groceries = Groceries("G303", "Rice", 1200, "2026-01-01", True)
groceries.show_details()

print("---Online Exclusive Price---")
online = OnlineExclusiveClothing("O404", "Jacket", 3000, "M", "Leather", "Puma", 1, "NA", False, 10)
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