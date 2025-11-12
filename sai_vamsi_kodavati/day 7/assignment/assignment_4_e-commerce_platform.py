# assignment_4_e-commerce_platform

# Base entity → Product (with attributes: product_id , name , price )


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
 
# # Subcategories:
# Electronics → extra: brand , warranty_years
# Clothing → extra: size , material
# Groceries → extra: expiry_date , is_organic

# Electronics class inherits from Product
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years
 
 # Clothing class inherits from Product
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)
        self.size = size
        self.material = material
 
 
# Groceries class inherits from Product
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic
 
#  new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()

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
 
# Creating instances of various product categories
laptop = Electronics("101", "TV", 60000, "Samsung", 2)
shirt = Clothing("102", "Jeans", 550, "M", "Cotton")
apple = Groceries("103", "Shirt", 1750, "2025-11-12", True)
 
online_phone = OnlineExclusiveProduct("104", "Smartphone", 50000, 10)
online_jeans = OnlineExclusiveProduct("105", "Denim Jeans", 1500, 15)
 
print("\n--- Online Exclusive Discounts ---")
online_phone.apply_discount()
online_jeans.apply_discount()  

# -----------------------------------------------------------------------------------------------

# Sample Output

# --- Online Exclusive Discounts ---
# Product: Smartphone
# Original Price: ₹50000
# Discount: 10%
# Discounted Price: ₹45000.0
# Product: Denim Jeans
# Original Price: ₹1500
# Discount: 15%
# Discounted Price: ₹1275.0