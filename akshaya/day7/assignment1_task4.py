# Task 4 — E-Commerce Platform (Inventory System)

# 1. Base entity → Product (with attributes: product_id , name , price )
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self):
        print(f"Product ID: {self.product_id} | Name: {self.name} | Price: ₹{self.price}")
# Subcategories:
# Electronics → extra: brand , warranty_years
# Clothing → extra: size , material
# Groceries → extra: expiry_date , is_organic

class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def get_details(self):
        super().get_details()
        print(f"Brand: {self.brand} | Warranty: {self.warranty_years} years")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def get_details(self):
        super().get_details()
        print(f"Size: {self.size} | Material: {self.material}")

class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def get_details(self):
        super().get_details()
        print(f"Expiry Date: {self.expiry_date} | Organic: {'Yes' if self.is_organic else 'No'}")
# A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discounted Price for {self.name}: ₹{discounted_price:.2f}")

    def get_details(self):
        super().get_details()
        print(f"Discount Rate: {self.discount_rate}%")
        self.apply_discount()


p1 = Electronics("E101", "Smartphone", 15000, "Samsung", 2)
p1.get_details()
print("------------------")

p2 = Clothing("C202", "T-shirt", 799, "L", "Cotton")
p2.get_details()
print("------------------")

p3 = Groceries("G303", "Organic Apple", 120, "2025-12-31", True)
p3.get_details()
print("------------------")

p4 = OnlineExclusiveProduct("OE404", "Smartwatch", 5000, 10)
p4.get_details()
print("------------------")


# sample output
# Product ID: E101 | Name: Smartphone | Price: ₹15000
# Brand: Samsung | Warranty: 2 years
# ------------------
# Product ID: C202 | Name: T-shirt | Price: ₹799      
# Size: L | Material: Cotton
# ------------------
# Product ID: G303 | Name: Organic Apple | Price: ₹120
# Expiry Date: 2025-12-31 | Organic: Yes
# ------------------
# Product ID: OE404 | Name: Smartwatch | Price: ₹5000
# Discount Rate: 10%
# Discounted Price for Smartwatch: ₹4500.00
# ------------------