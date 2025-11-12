# Task 4 — E-Commerce Platform (Inventory System)
# Domain: Retail Tech

# Base class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

# Derived class - Electronics
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

# Derived class - Clothing
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)
        self.size = size
        self.material = material

# Derived class - Groceries
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

# Derived class - Online Exclusive Product
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        Product.__init__(self, product_id, name, price)
        self.discount_rate = discount_rate
        
    # Method to apply discount
    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate / 100)
        print(f"Product: {self.name}")
        print(f"Original Price: ₹{self.price}")
        print(f"Discount: {self.discount_rate}%")
        print(f"Discounted Price: ₹{discounted_price}")

# Object creation
laptop = Electronics("E101", "Laptop", 60000, "Dell", 2)
shirt = Clothing("C202", "T-Shirt", 800, "L", "Cotton")
apple = Groceries("G303", "Apple", 150, "2025-12-10", True)
online_phone = OnlineExclusiveProduct("O404", "Smartphone", 30000, 10)
online_jeans = OnlineExclusiveProduct("O405", "Denim Jeans", 2000, 15)

# Display online exclusive product discounts
print("\n--- Online Exclusive Discounts ---")
online_phone.apply_discount()
online_jeans.apply_discount()


# Sample Output:
# --- Online Exclusive Discounts ---
# Product: Smartphone
# Original Price: ₹30000
# Discount: 10%
# Discounted Price: ₹27000.0
# Product: Denim Jeans
# Original Price: ₹2000
# Discount: 15%
# Discounted Price: ₹1700.0
