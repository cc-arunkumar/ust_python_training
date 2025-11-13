# UST Digital Retail is developing an e-commerce backend system.
# 1. Base entity → Product (with attributes: product_id , name , price )

class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
    def show_info(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}")
# 2. Subcategories:
# Electronics → extra: brand , warranty_years
# Clothing → extra: size , material
# Groceries → extra: expiry_date , is_organic

class Electronics(Product):
    def __init__(self,product_id,name,price,brand,warranty_years):
        Product.__init__(self,product_id,name,price)
        self.brand=brand
        self.warranty_years=warranty_years
class Clothing(Product):
    def __init__(self,product_id,name,price,size,material):
        Product.__init__(self,product_id,name,price)
        self.size=size
        self.material=material
class Groceries(Product):
    def __init__(self,product_id,name,price,expiry_date,is_organic):
        Product.__init__(self,product_id,name,price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic

# A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()
        
class OnlineExclusiveMixin:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discount applied: {self.discount_rate}% → Final Price: {discounted_price}")
        return discounted_price

# Online Exclusive Clothing
class OnlineExclusiveClothing(Clothing, OnlineExclusiveMixin):
    def __init__(self, product_id, name, price, size, material, discount_rate):
        Clothing.__init__(self, product_id, name, price, size, material)
        OnlineExclusiveMixin.__init__(self, discount_rate)


# Online Exclusive Electronics
class OnlineExclusiveElectronics(Electronics, OnlineExclusiveMixin):
    def __init__(self, product_id, name, price, brand, warranty_years, discount_rate):
        Electronics.__init__(self, product_id, name, price, brand, warranty_years)
        OnlineExclusiveMixin.__init__(self, discount_rate)
        
# Online Exclusive Electronics
phone = OnlineExclusiveElectronics(201, "Smartphone", 50000, "Samsung", 2, 10)
phone.show_info()
phone.apply_discount()

print("___________________________________________________")

# Online Exclusive Clothing
shirt = OnlineExclusiveClothing(301, "T-Shirt", 1500, "L", "Cotton", 20)
shirt.show_info()
shirt.apply_discount()


#output

# Product ID: 201, Name: Smartphone, Price: 50000
# Discount applied: 10% → Final Price: 45000.0
# ___________________________________________________
# Product ID: 301, Name: T-Shirt, Price: 1500
# Discount applied: 20% → Final Price: 1200.0