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
# Enterprise Tech Systems – Inheritance Design Challenge 3
# Ensure common attributes are reused and not redefined.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def product_info(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Price: ₹{self.price}")

#  online-exclusive products
class OnlineExclusiveProduct:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discounted Price: ₹{discounted_price:.2f}")

# Electronics category
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def electronics_info(self):
        self.product_info()
        print(f"Brand: {self.brand}, Warranty: {self.warranty_years} years")

# Clothing category
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)
        self.size = size
        self.material = material

    def clothing_info(self):
        self.product_info()
        print(f"Size: {self.size}, Material: {self.material}")

# Groceries category
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def grocery_info(self):
        self.product_info()
        print(f"Expiry Date: {self.expiry_date}, Organic: {'Yes' if self.is_organic else 'No'}")

# Online-exclusive electronics
class OnlineElectronics(Electronics, OnlineExclusiveProduct):
    def __init__(self, product_id, name, price, brand, warranty_years, discount_rate):
        Electronics.__init__(self, product_id, name, price, brand, warranty_years)
        OnlineExclusiveProduct.__init__(self, discount_rate)

# Create an online-exclusive electronics product
# Test Product
print("Testing Product:")
p = Product(1, "Generic Item", 100)
p.product_info()

print("\nTesting Electronics:")
e = Electronics(101, "iphone", 30000, "oppo", 2)
e.electronics_info()

print("\nTesting Clothing:")
c = Clothing(102, "saree", 499, "L", "tissue")
c.clothing_info()

print("\nTesting Groceries:")
g = Groceries(103, "papaya", 250, "2020-12-10", True)
g.grocery_info()

print("\nTesting OnlineExclusiveProduct (via OnlineElectronics):")
oe = OnlineElectronics(103, "Laptop", 850000, "hp", 3, 45)
oe.electronics_info()
oe.apply_discount()


# ID: 101, Name: Smartphone, Price: ₹30000
# Brand: Samsung, Warranty: 2 years
# Discounted Price: ₹27000.00