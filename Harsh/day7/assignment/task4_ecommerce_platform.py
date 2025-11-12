class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}, Price: {self.price}")


class Electronics(Product):
    def __init__(self, name, price, product_id, brand, warranty_years):
        Product.__init__(self,name, price)
        self.product_id = product_id
        self.brand = brand
        self.warranty_years = warranty_years

    def display(self):
        super().display()
        print(f"Electronics ID: {self.product_id}, Brand: {self.brand}, Warranty: {self.warranty_years} years")


class Clothing(Product):
    def __init__(self, name, price, size, material):
        Product.__init__(self,name, price)
        self.size = size
        self.material = material

    def display(self):
        super().display()
        print(f"Clothing Size: {self.size}, Material: {self.material}")


class Groceries(Product):
    def __init__(self, name, price, expiry_date, is_organic):
        Product.__init__(self,name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def display(self):
        super().display()
        print(f"Groceries Expiry: {self.expiry_date}, Organic: {self.is_organic}")
        
class OnlineExclusiveProduct(Product):
    def __init__(self, name, price,discount_rate):
        Product.__init__(self,name, price)
        self.discount_rate=discount_rate
        
    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate)
        print(f"Discounted Price: {discounted_price}")

    def display(self):
        super().display()
        print(f"Discount Rate: {self.discount_rate * 100}%")

o1=OnlineExclusiveProduct("Laptop",60000,0.10)
o2=OnlineExclusiveProduct("Sneaker",10000,0.30)
o3=OnlineExclusiveProduct("Mobile",90000,0.40)
print("------------------------------------------")
o1.display()
o1.apply_discount()
print("------------------------------------------")
o2.display()
o2.apply_discount()
print("------------------------------------------")
o3.display()
o3.apply_discount()
print("------------------------------------------")


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