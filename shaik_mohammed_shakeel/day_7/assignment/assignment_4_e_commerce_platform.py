# Task 4 — E-Commerce Platform (Inventory System)

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


# Base class representing a general product

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

 # Subclass for electronic products
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

# Subclass for clothing products
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)
        self.size = size
        self.material = material
 
 # Subclass for grocery items
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic


# Subclass for products sold exclusively online 
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        Product.__init__(self, product_id, name, price)
        self.discount_rate = discount_rate

     # Method to calculate and display discounted price  
    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate / 100)
        print(f"Product: {self.name}")
        print(f"Original Price: ₹{self.price}")
        print(f"Discount: {self.discount_rate}%")
        print(f"Discounted Price: ₹{discounted_price}")
 
# Creating objects for different categories
Mobile = Electronics("101", "Mobile", 70000, "samsung", 1)
shirt = Clothing("A9051", "UCB", 1200, "M", "Cotton")
fruits = Groceries("F101", "Apple", 150, "22-12-2025", "YES")

# Creating online-exclusive products
online_phone = OnlineExclusiveProduct("707", "16 Pro", 130000, 10)
online_jeans = OnlineExclusiveProduct("808", "S24 Ultra", 72000, 15)

# Displaying discounted prices for online products 
print("\n--- Online Exclusive Discounts ---")
online_phone.apply_discount()
online_jeans.apply_discount()   


#Sample Output
# --- Online Exclusive Discounts ---
# Product: 16 Pro
# Original Price: ₹130000
# Discount: 10%
# Discounted Price: ₹117000.0
# Product: S24 Ultra
# Original Price: ₹72000
# Discount: 15%
# Discounted Price: ₹61200.0