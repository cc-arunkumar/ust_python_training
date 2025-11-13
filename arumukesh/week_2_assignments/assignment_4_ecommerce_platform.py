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
# ⚙️ Task: Design a flexible inheritance structure so new product categories can
# be added easily later

class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self,product_id,name,price,brand,warranty_years):
        Product.__init__(self,product_id,name,price)
        self.brand=brand
        self.warranty_years=warranty_years

class Groceries(Product):
    def __init__(self,product_id,name,price,expiry_date,is_organic):
        Product.__init__(self,product_id,name,price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic
class OnlineExclusiveProduct(Electronics,Groceries):
    def __init__(self,product_id,name,price,discount_rate,product_type,brand=None,expiry_date=None,warranty_years=None,is_organic=None):
        self.product_type=product_type
        self.discount_rate=discount_rate
        if product_type == "electronics":
            self.product = Electronics(product_id, name, price, brand, warranty_years)
        elif product_type == "grocery":
            self.product = Groceries(product_id, name, price, expiry_date, is_organic)
    def apply_discount(self):
        discounted_price = self.product.price - (self.product.price * self.discount_rate / 100)
        print(f"Discount applied ({self.discount_rate}%): New price = ₹{discounted_price:.2f}")

# Electronics example
item1 = OnlineExclusiveProduct(
    product_type="electronics",
    discount_rate=15,
    product_id="E101",
    name="Smart TV",
    price=55000,
    brand="LG",
    warranty_years=2
)

# Grocery example
item2 = OnlineExclusiveProduct(
    product_type="grocery",
    discount_rate=10,
    product_id="G501",
    name="Organic Honey",
    price=400,
    expiry_date="2026-03-01",
    is_organic=True
)

# item1.show_product_info()
item1.apply_discount()

# item2.show_product_info()
item2.apply_discount()

        

# Discount applied (15%): New price = ₹46750.00
# Discount applied (10%): New price = ₹360.00