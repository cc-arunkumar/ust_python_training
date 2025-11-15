# Base class Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}, Price: {self.price}")


# Electronics inherits from Product
class Electronics(Product):
    def __init__(self, name, price, product_id, brand, warranty_years):
        # Call Product constructor
        Product.__init__(self, name, price)
        self.product_id = product_id
        self.brand = brand
        self.warranty_years = warranty_years

    def display(self):
        # Reuse Product's display method
        super().display()
        print(f"Electronics ID: {self.product_id}, Brand: {self.brand}, Warranty: {self.warranty_years} years")


# Clothing inherits from Product
class Clothing(Product):
    def __init__(self, name, price, size, material):
        Product.__init__(self, name, price)
        self.size = size
        self.material = material

    def display(self):
        super().display()
        print(f"Clothing Size: {self.size}, Material: {self.material}")


# Groceries inherits from Product
class Groceries(Product):
    def __init__(self, name, price, expiry_date, is_organic):
        Product.__init__(self, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def display(self):
        super().display()
        print(f"Groceries Expiry: {self.expiry_date}, Organic: {self.is_organic}")


# OnlineExclusiveProduct inherits from Product
class OnlineExclusiveProduct(Product):
    def __init__(self, name, price, discount_rate):
        Product.__init__(self, name, price)
        self.discount_rate = discount_rate
        
    def apply_discount(self):
        # Calculate discounted price
        discounted_price = self.price * (1 - self.discount_rate)
        print(f"Discounted Price: {discounted_price}")


# ------------------------------------------
# Product: Laptop, Price: 60000
# Discount Rate: 10.0%
# Discounted Price: 54000.0
# ------------------------------------------
# Product: Sneaker, Price: 10000
# Discount Rate: 30.0%
# Discounted Price: 7000.0
# ------------------------------------------
# Product: Mobile, Price: 90000
# Discount Rate: 40.0%
# Discounted Price: 54000.0
# ------------------------------------------