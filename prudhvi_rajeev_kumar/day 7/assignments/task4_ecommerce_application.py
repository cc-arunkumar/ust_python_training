#Creating a class Product and adding the required attributes to it.
class Product:
    def __init__(self, product_id , name , price):
        self.product_id = product_id
        self.name = name
        self.price = price

#Creating a class Electronics inheriting the properties of Product class.
class Electronics(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

#Creating a class Clothing inheriting the properties of Product class.
class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

#Creating a class Groceries inheriting the properties of Product class.
class Groceries(Product):
    def __init__(self, product_id, name, price, expiry_date, is_organic):
        super().__init__(product_id, name, price)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

#Creating a class OnlineExclusiveProduct inheriting the properties of Product class.
class OnlineExclusiveProduct(Product):
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate = discount_rate

    def apply_discount(self):
        discounted_price = self.price * (1 - self.discount_rate / 100)
        return discounted_price
    
# Example usage
print("----------------------------------------------------------------------------------------------")
laptop = Electronics(101, "Laptop", 80000, "Dell", 2)
print(f"Product: {laptop.name}, Brand: {laptop.brand}, Price: {laptop.price}, Warranty: {laptop.warranty_years} years")
laptop_price_after_discount = OnlineExclusiveProduct(101, "Laptop", 80000, 10).apply_discount()
print(f"Price after discount: {laptop_price_after_discount}")
print("----------------------------------------------------------------------------------------------")
tshirt = Clothing(201, "T-Shirt", 500, "L", "Cotton")
print(f"Product: {tshirt.name}, Size: {tshirt.size}, Material: {tshirt.material}, Price: {tshirt.price}")
tshirt_price_after_discount = OnlineExclusiveProduct(201, "T-Shirt", 500, 15).apply_discount()
print(f"Price after discount: {tshirt_price_after_discount}")


#Console Output:
# ----------------------------------------------------------------------------------------------
# Product: Laptop, Brand: Dell, Price: 80000, Warranty: 2 years
# Price after discount: 72000.0
# ----------------------------------------------------------------------------------------------
# Product: T-Shirt, Size: L, Material: Cotton, Price: 500
# Price after discount: 425.0