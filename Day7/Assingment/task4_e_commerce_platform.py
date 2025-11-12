# Task 4 — E-Commerce Platform (Inventory System)
# Domain: Retail Tech

# Base class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_details(self):
        print(f"ID: {self.product_id}, Name: {self.name}, Price: ₹{self.price}")


# Subclass 1 — Electronics
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def display_details(self):
        super().display_details()
        print(f"Brand: {self.brand}, Warranty: {self.warranty_years} years")


# Subclass 2 — Clothing
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def display_details(self):
        super().display_details()
        print(f"Size: {self.size}, Material: {self.material}")


# Subclass 3 — Groceries
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def display_details(self):
        super().display_details()
        print(f"Expiry Date: {self.expiry_date}, Organic: {self.is_organic}")


# Online Exclusive Product
class OnlineExclusiveProduct:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, price):
        discount_amount = price * (self.discount_rate / 100)
        return price - discount_amount


# Hybrid Inheritance Example
class OnlineElectronics(Electronics, OnlineExclusiveProduct):
    def __init__(self, product_id, name, price, brand, warranty_years, discount_rate):
        Electronics.__init__(self, product_id, name, price, brand, warranty_years)
        OnlineExclusiveProduct.__init__(self, discount_rate)

    def display_details(self):
        super().display_details()
        discounted_price = self.apply_discount(self.price)
        print(f"Discount Rate: {self.discount_rate}%")
        print(f"Discounted Price: ₹{discounted_price}")
#Testing
e1 = OnlineElectronics(101, "Smartphone", 30000, "Samsung", 2, 10)
print("---- Online Exclusive Product ----")
e1.display_details()

print("\n---- Normal Product ----")
c1 = Clothing(201, "T-Shirt", 800, "L", "Cotton")
c1.display_details()

# sample output:

# ---- Online Exclusive Product ----
# ID: 101, Name: Smartphone, Price: ₹30000
# Brand: Samsung, Warranty: 2 years
# Discount Rate: 10%
# Discounted Price: ₹27000.0

# ---- Normal Product ----
# ID: 201, Name: T-Shirt, Price: ₹800
# Size: L, Material: Cotton