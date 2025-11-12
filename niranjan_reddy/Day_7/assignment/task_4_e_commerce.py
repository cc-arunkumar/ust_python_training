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


# 1. Base entity → Product (with attributes: product_id , name , price )
class Product:
    def __init__(self,product_id , name , price):
        self.product_id =product_id 
        self.name=name  
        self.price=price

# 2. Subcategories:
# Electronics → extra: brand , warranty_years
# Clothing → extra: size , material
# Groceries → extra: expiry_date , is_organic

class Electronics(Product):
    def __init__(self, product_id, name, price,brand , warranty_years):
        Product.__init__(self,product_id, name, price)
        self.brand=brand  
        self.warranty_years=warranty_years
    
class Clothing(Product):
    def __init__(self, product_id, name, price,size , material):
        Product.__init__(self,product_id, name, price)
        self.size=size 
        self.material=material

class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date , is_organic):
        Product.__init__(self,product_id, name, price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic

# 3. A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()

class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price,discount_rate):
        Product.__init__(self,product_id, name, price)
        self.discount_rate=discount_rate

    def apply_discount(self):
        discount_price=self.price-(self.discount_rate/100*self.price)
        print(f"Discounted Price:{int(discount_price)}")

product=OnlineExclusiveProduct(101,"Sport Shoe",5200,25)


product.apply_discount()


# Sample output
# Discounted Price:3900
