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

# Parent class
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
    def show_prod(self):
        print(f"Id: {self.product_id}")
        print(f"name: {self.name}")
        print(f"price: {self.price}")
        
# Child class
class Electronics(Product):
    def __init__(self, product_id, name, price,brand,warranty_years):
        super().__init__(product_id, name, price)
        self.brand=brand
        self.warranty_years=warranty_years
    def show_elec(self):
        self.show_prod()
        print(f"brand: {self.brand}")
        print(f"warranty_years: {self.warranty_years}")

# child class
class Clothing(Product):
    def __init__(self, product_id, name, price,size,material):
        super().__init__(product_id, name, price)
        self.size=size
        self.material=material
    def show_cloth(self):
        self.show_prod()
        print(f"size: {self.size}")
        print(f"material: {self.material}")

# child class
class Groceries(Product):
    def __init__(self, product_id, name, price,expiry_date,is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic
    def show_groce(self):
        self.show_prod()
        print(f"expiry_date: {self.expiry_date}")
        print(f"is_organic: {self.is_organic}")
        
# child class
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price):
        super().__init__(product_id, name, price)
        self.discount_rate=0
    def apply_discount(self):
        self.show_prod()
        self.discount_rate=self.price-(self.price*0.10)
        print(f"New discount_rate: {self.discount_rate}")

# Object creation and getting info
onlineprod1= OnlineExclusiveProduct("p001","Mouse",1000)
onlineprod1.apply_discount()
    
# Output
# Id: P001
# name: Mouse
# price: 1000
# New discount_rate: 900.0