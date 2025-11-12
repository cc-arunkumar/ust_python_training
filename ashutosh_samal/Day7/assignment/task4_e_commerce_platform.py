#Task 4 — E-Commerce Platform

#Creation pf product class
class Product:
    def __init__(self,product_id , name , price):
        self.product_id = product_id
        self.name = name
        self.price = price

#creation of electronics product class
class Electronics(Product):
    def __init__(self, product_id, name, price, brand , warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

#creation of clothing class
class Clothing(Product):
    def __init__(self, product_id, name, price, size , material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

#creation of groceries class        
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date , is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

#creation of online exclusive clas
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate =discount_rate
    
    #function to apply discount    
    def apply_discount(self):
        print(f"Product Name: {self.name}")
        print(f"Product ID: {self.product_id}")
        print(f"Original Price: {self.price}")
        self.price -= ((self.price*self.discount_rate)//100)
        print(f"Discounted Price after {self.discount_rate}% discount: {self.price}")

exclprod1 = OnlineExclusiveProduct("P101","Oneplus",50000,10)
exclprod1.apply_discount() 


#Sample Execution
# Product Name: Oneplus
# Product ID: P101
# Original Price: 50000
# Discounted Price after 10% discount: 45000