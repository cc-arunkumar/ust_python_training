# Task 4 — E-Commerce Platform (Inventory System)
# Domain: Retail Tech
# Business Requirement:
# UST Digital Retail is developing an e-commerce backend system.
# 1. Base entity → Product (with attributes: product_id , name , price )
class Product:
    def __init__(self,product_id,name,price):
        self.product_id=product_id
        self.name=name
        self.price=price
        
# 2. Subcategories:
# Electronics → extra: brand , warranty_years
class Electronics(Product):
    def __init__(self,product_id,name,price,brand,warranty_years):
        super().__init__(product_id,name,price)
        self.brand=brand
        self.warrenty_years=warranty_years
        
# Clothing → extra: size , material
class Clothing(Product):
    def __init__(self,product_id,name,price,size,material):
        super().__init__(product_id,name,price)
        self.size=size
        self.material=material
    
# Groceries → extra: expiry_date , is_organic
class Groceries(Product):
    def __init__(self,product_id,name,price,expiry_date,is_organic):
        super().__init__(product_id,name,price)
        self.expiry_date=expiry_date
        self.is_organic=is_organic
        
# 3. A new department wants to build an OnlineExclusiveProduct that applies to 
# only some product categories and adds:
# discount_rate
# Method: apply_discount()
class OnlineExclusiceProduct(Product):
    def __init__(self,product_id,name,price,discount_rate):
        super().__init__(product_id,name,price)
        self.discount_rate=discount_rate
    
    def apply_discount(self):
        self.price=self.price-(self.price*(self.discount_rate/100))
        print("Discounted Price: ",self.price )

prod1=Product(101,"boost",5)

prod2=Electronics(102,"headphones",4000,"Boat",3)

prod3=Clothing(103,"shirt",3000,"M","Cotton")

prod4=Groceries(104,"apple",40,"2025-11-14","Yes")

prod=OnlineExclusiceProduct(202,"lotion",9000,10)
prod.apply_discount()    
    
#sample output
# Discounted Price:  8100.0