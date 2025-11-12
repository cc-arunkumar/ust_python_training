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


# This class to store general product details
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # Product ID
        self.name = name  # Product name
        self.price = price  # Product price
    
    def show(self):
        # Display product details
        print(f"The product id is {self.product_id}")
        print(f"The product name is {self.name}")
        print(f"The product price is {self.price}")

# This class inherits from Product, adds brand and warranty info
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        Product.__init__(self, product_id, name, price)  # Inherit from Product
        self.brand = brand  # Electronics brand
        self.warranty_years = warranty_years  # Warranty in years
        
    def ele_show(self):
        # Display electronic-specific details
        print(f"The brand is {self.brand}")
        print(f"The warranty is {self.warranty_years}")

# This class inherits from Product, adds size and material info
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        Product.__init__(self, product_id, name, price)  # Inherit from Product
        self.size = size  # Clothing size
        self.material = material  # Clothing material
        
    def cle_show(self):
        # Display clothing-specific details
        print(f"The size is {self.size}")
        print(f"The material is {self.material}")

# This class inherits from Product, adds expiry and organic info
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, product_id, name, price)  # Inherit from Product
        self.expiry_date = expiry_date  # Expiry date of product
        self.is_organic = is_organic  # Whether product is organic
        
    def gle_show(self):
        # Display grocery specific details
        print(f"The expiry date is {self.expiry_date}")
        print(f"The material is {self.is_organic}")

# This class inherits from Product, adds discount feature
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        Product.__init__(self, product_id, name, price)  # Inherit from Product
        self.discount_rate = discount_rate  # Discount rate in percentage
    
    def apply_discount(self):
        # Apply discount and show new price
        self.price -= (self.price * self.discount_rate) // 100
        print(f"The discounted price is {self.price}")

# Object creation and method calls
e1 = Electronics(100, "Fan", 10000, "Orient", 20)  # Create Electronics object
e1.show()  # Show product details
e1.ele_show()  # Show electronics info
print("---------------------------------------")

c1 = Clothing(200, "T-shit", 800, "Large", "Cotton")  # Create Clothing object
c1.show()  # Show product details
c1.cle_show()  # Show clothing info
print("---------------------------------------")

g1 = Groceries(300, "Milk", 20, "2025-11-04", "Organic")  # Create Groceries object
g1.show()  # Show product details
g1.gle_show()  # Show grocery info
print("---------------------------------------")

p1 = OnlineExclusiveProduct(101, "Minimalist", 1000, 10)  # Create OnlineExclusiveProduct object
p1.show()  # Show product details
p1.apply_discount()  # Apply discount to price


#Sample output
# The product id is 100
# The product name is Fan
# The product price is 10000
# The brand is Orient
# The warranty is 20
# ---------------------------------------
# The product id is 200
# The product name is T-shit
# The product price is 800
# The size is Large
# The material is Cotton
# ---------------------------------------
# The product id is 300
# The product name is Milk
# The product price is 20
# The expiry date is 2025-11-04
# The material is Organic
# ---------------------------------------
# The product id is 101
# The product name is Minimalist
# The product price is 1000
# The discounted price is 900