#Assignment 4: E-commerce Platform(Inventory System)

# Base class
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def show_info(self):
        print(f"Product ID: {self.product_id} | Product: {self.name} | Price: ₹{self.price}")


class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def show_details(self):
        self.show_info()
        print(f"Brand: {self.brand} | Warranty: {self.warranty_years} years")


class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def show_details(self):
        self.show_info()
        print(f"Size: {self.size} | Material: {self.material}")


class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def show_details(self):
        self.show_info()
        print(f"Expiry: {self.expiry_date} | Organic: {'Yes' if self.is_organic else 'No'}")


class OnlineExclusiveProduct:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        print(f"Discounted Price: ₹{discounted_price:.2f}")


class OnlineElectronics(Electronics, OnlineExclusiveProduct):
    def __init__(self, product_id, name, price, brand, warranty_years, discount_rate):
        Electronics.__init__(self, product_id, name, price, brand, warranty_years)
        OnlineExclusiveProduct.__init__(self, discount_rate)


class OnlineClothing(Clothing, OnlineExclusiveProduct):
    def __init__(self, product_id, name, price, size, material, discount_rate):
        Clothing.__init__(self, product_id, name, price, size, material)
        OnlineExclusiveProduct.__init__(self, discount_rate)


p1 = Product("P1", "Water Bottle", 150)
p2 = Product("P2", "Notebook", 80)
p3 = Product("P3", "Bluetooth Speaker", 1200)
p1.show_info()
p2.show_info()
p3.show_info()
print("----------------------------------")

e1 = Electronics("E101", "Smartphone", 30000, "Samsung", 2)
e2 = Electronics("E202", "Laptop", 75000, "Dell", 3)
e3 = Electronics("E303", "Smartwatch", 15000, "Garmin", 1)
e1.show_details()
e2.show_details()
print("----------------------------------")

g1 = Groceries("G101", "Organic Apples", 250, "2025-12-01", True)
g2 = Groceries("G102", "Milk", 60, "2025-11-15", False)
g3 = Groceries("G103", "Brown Rice", 120, "2026-01-10", True)
g1.show_details()
g3.show_details()
print("----------------------------------")


item1 = OnlineElectronics("E401", "Smartphone", 100000, "Samsung", 2, 10)
item1.show_details()
item1.apply_discount()
print("----------------------------------")


item2 = OnlineClothing("C101", "T-Shirt", 999, "L", "Cotton", 20)
item2.show_details()
item2.apply_discount()
print("----------------------------------")

'''output:
Product ID: P1 | Product: Water Bottle | Price: ₹150
Product ID: P2 | Product: Notebook | Price: ₹80
Product ID: P3 | Product: Bluetooth Speaker | Price: ₹1200
----------------------------------
Product ID: E101 | Product: Smartphone | Price: ₹30000    
Brand: Samsung | Warranty: 2 years
Product ID: E202 | Product: Laptop | Price: ₹75000        
Brand: Dell | Warranty: 3 years
----------------------------------
Product ID: G101 | Product: Organic Apples | Price: ₹250  
Expiry: 2025-12-01 | Organic: Yes
Product ID: G103 | Product: Brown Rice | Price: ₹120      
Expiry: 2026-01-10 | Organic: Yes
----------------------------------
Product ID: E401 | Product: Smartphone | Price: ₹100000   
Brand: Samsung | Warranty: 2 years
Discounted Price: ₹90000.00
----------------------------------
Product ID: C101 | Product: T-Shirt | Price: ₹999
Size: L | Material: Cotton
Discounted Price: ₹799.20
----------------------------------
'''