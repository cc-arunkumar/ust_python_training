#Task 4: E-Commerce Platform (Inventory System)
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self,product_id,name,price,brand,warranty):
        Product.__init__(self,product_id,name,price)
        self.brand=brand
        self.warranty=warranty
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
class OnlineExclusiveProduct(Product):
    def __init__(self,product_id,name,price,discount_rate):
        Product.__init__(self,product_id,name,price)
        self.discount_rate=discount_rate
    def apply_discount(self):
        return(self.price-(self.price*self.discount_rate))
#Object Creation of Online Exclusive Product
product_id=int(input("Enter product ID: "))
name=input("Enter the product name: ")
price=float(input("Enter price: Rs"))
discount_rate=float(input("Enter the discount rate: "))
oep=OnlineExclusiveProduct(product_id,name,price,discount_rate)
print("Discount price: Rs",oep.apply_discount())

#================Sample output=================
# Enter product ID: 101
# Enter the product name: water bottle
# Enter price: Rs78
# Enter the discount rate: 0.10
# Discount price: Rs 70.2