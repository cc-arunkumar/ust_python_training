# Task 4 — E-Commerce Platform (Inventory System)
#  Domain: Retail Tech
#  Business Requirement:
#  UST Digital Retail is developing an e-commerce backend system.
#   Base entity → 
# Product (with attributes:# product_id,#  name , 
# price )  
#  Subcategories:
#  Electronics → extra: 
 
# brand , 
# warranty_years
#  Clothing → extra: 
# size , 
# material
#  Groceries → extra: 
# expiry_date , 
# is_organic

#   A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
#  discount_rate
#  Method: 
# apply_discount()


# Define a base Product class
class Product:
    # Constructor to initialize product attributes
    def __init__(self, name, price):
        self.name = name      # Product name
        self.price = price    # Product price

    # Method to display product information
    def show_info(self):
        print(f"Name: {self.name}, Price: ₹{self.price}")


# Define Electronics class that inherits from Product
class Electronics(Product):
    # Constructor to initialize electronics-specific attributes
    def __init__(self, name, price, product_id, brand, warranty_years):
        # Call Product constructor
        super().__init__(name, price)
        self.product_id = product_id      # Unique product ID
        self.brand = brand                # Brand name
        self.warranty_years = warranty_years  # Warranty period in years

    # Method to display electronics information
    def show_electronics_info(self):
        print(f"ID: {self.product_id}, Brand: {self.brand}, Warranty: {self.warranty_years} years")


# Define Clothing class that inherits from Product
class Clothing(Product):
    # Constructor to initialize clothing-specific attributes
    def __init__(self, name, price, size, material):
        # Call Product constructor
        super().__init__(name, price)
        self.size = size          # Clothing size
        self.material = material  # Clothing material

    # Method to display clothing information
    def show_clothing_info(self):
        print(f"Size: {self.size}, Material: {self.material}")


# Define Groceries class that inherits from Product
class Groceries(Product):
    # Constructor to initialize grocery-specific attributes
    def __init__(self, name, price, expiry_date, is_organic):
        # Call Product constructor
        super().__init__(name, price)
        self.expiry_date = expiry_date   # Expiry date of grocery item
        self.is_organic = is_organic     # Boolean flag for organic status

    # Method to display grocery information
    def show_grocery_info(self):
        # Check if product is organic or not
        organic_status = "Organic" if self.is_organic else "Non-organic"
        print(f"Expiry: {self.expiry_date}, Type: {organic_status}")


# Define OnlineExclusiveProduct class (mixin for discount feature)
class OnlineExclusiveProduct:
    # Constructor to initialize discount rate
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate   # Discount percentage

    # Method to apply discount on price
    def apply_discount(self, price):
        discounted_price = price * (1 - self.discount_rate / 100)  # Calculate discounted price
        print(f"Discounted Price: ₹{discounted_price:.2f}")
        return discounted_price


# Define OnlineExclusiveElectronics class that inherits from Electronics and OnlineExclusiveProduct
class OnlineExclusiveElectronics(Electronics, OnlineExclusiveProduct):
    # Constructor to initialize both Electronics and OnlineExclusiveProduct
    def __init__(self, name, price, product_id, brand, warranty_years, discount_rate):
        Electronics.__init__(self, name, price, product_id, brand, warranty_years)
        OnlineExclusiveProduct.__init__(self, discount_rate)


# Define OnlineExclusiveClothing class that inherits from Clothing and OnlineExclusiveProduct
class OnlineExclusiveClothing(Clothing, OnlineExclusiveProduct):
    # Constructor to initialize both Clothing and OnlineExclusiveProduct
    def __init__(self, name, price, size, material, discount_rate):
        Clothing.__init__(self, name, price, size, material)
        OnlineExclusiveProduct.__init__(self, discount_rate)


# Define OnlineExclusiveGroceries class that inherits from Groceries and OnlineExclusiveProduct
class OnlineExclusiveGroceries(Groceries, OnlineExclusiveProduct):
    # Constructor to initialize both Groceries and OnlineExclusiveProduct
    def __init__(self, name, price, expiry_date, is_organic, discount_rate):
        Groceries.__init__(self, name, price, expiry_date, is_organic)
        OnlineExclusiveProduct.__init__(self, discount_rate)


# -------------------------------
# Object Creation and Method Calls
# -------------------------------

# Create an OnlineExclusiveElectronics object
item = OnlineExclusiveElectronics("Smartphone", 30000, "E22", "Samsung", 2, 10)

# Show basic product info
item.show_info()

# Show electronics-specific info
item.show_electronics_info()

# Apply discount and show discounted price
item.apply_discount(item.price)


# -------------------------------
# Expected Output
# -------------------------------
# Name: Smartphone, Price: ₹30000
# ID: E22, Brand: Samsung, Warranty: 2 years
# Discounted Price: ₹27000.00