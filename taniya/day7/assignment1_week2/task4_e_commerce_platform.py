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


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Name: {self.name}, Price: ₹{self.price}")


class Electronics(Product):
    def __init__(self, name, price, product_id, brand, warranty_years):
        super().__init__(name, price)
        self.product_id = product_id
        self.brand = brand
        self.warranty_years = warranty_years

    def show_electronics_info(self):
        print(f"ID: {self.product_id}, Brand: {self.brand}, Warranty: {self.warranty_years} years")

class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def show_clothing_info(self):
        print(f"Size: {self.size}, Material: {self.material}")

class Groceries(Product):
    def __init__(self, name, price, expiry_date, is_organic):
        super().__init__(name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def show_grocery_info(self):
        organic_status = "Organic" if self.is_organic else "Non-organic"
        print(f"Expiry: {self.expiry_date}, Type: {organic_status}")


class OnlineExclusiveProduct:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self, price):
        discounted_price = price * (1 - self.discount_rate / 100)
        print(f"Discounted Price: ₹{discounted_price:.2f}")
        return discounted_price


class OnlineExclusiveElectronics(Electronics, OnlineExclusiveProduct):
    def __init__(self, name, price, product_id, brand, warranty_years, discount_rate):
        Electronics.__init__(self, name, price, product_id, brand, warranty_years)
        OnlineExclusiveProduct.__init__(self, discount_rate)

class OnlineExclusiveClothing(Clothing, OnlineExclusiveProduct):
    def __init__(self, name, price, size, material, discount_rate):
        Clothing.__init__(self, name, price, size, material)
        OnlineExclusiveProduct.__init__(self, discount_rate)

class OnlineExclusiveGroceries(Groceries, OnlineExclusiveProduct):
    def __init__(self, name, price, expiry_date, is_organic, discount_rate):
        Groceries.__init__(self, name, price, expiry_date, is_organic)
        OnlineExclusiveProduct.__init__(self, discount_rate)

item = OnlineExclusiveElectronics("Smartphone", 30000, "E22", "Samsung", 2, 10)
item.show_info()
item.show_electronics_info()
item.apply_discount(item.price)


# Output
# Name: Smartphone, Price: ₹30000
# ID: E22, Brand: Samsung, Warranty: 2 years  
# Discounted Price: ₹27000.00
