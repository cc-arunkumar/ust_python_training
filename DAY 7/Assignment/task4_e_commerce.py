"""
A new department wants to build an OnlineExclusiveProduct that applies to only some product categories and adds:

"""

# Base Product class
class Product:
    def __init__(self, category, product_id, name, price):
        self.category = category          # Category of product
        self.product_id = product_id      # Unique product ID
        self.name = name                  # Product name
        self.price = price                # Product price



# Electronics inherits from Product
class Electronics(Product):
    def __init__(self, category, product_id, name, price, brand, warranty_years):
        Product.__init__(self, category, product_id, name, price)   # Initialize base product fields
        self.brand = brand                                           # Electronics brand
        self.warranty_years = warranty_years                         # Warranty period
    
    # Display electronics info
    def display(self):
        print(f"Category:{self.category}, Product ID:{self.product_id}, Name:{self.name}, "
              f"Price:{self.price}, Brand:{self.brand}, Warranty:{self.warranty_years} years")



# Clothing inherits from Product
class Clothing(Product):
    def __init__(self, category, product_id, name, price, size, material):
        Product.__init__(self, category, product_id, name, price)   # Initialize base product
        self.size = size                                             # Clothing size
        self.material = material                                     # Material type
    
    # Display clothing info
    def display(self):
        print(f"Category:{self.category}, Product ID:{self.product_id}, Name:{self.name}, "
              f"Price:{self.price}, Size:{self.size}, Material:{self.material}")



# Groceries inherits from Product
class Groceries(Product):
    def __init__(self, category, product_id, name, price, expiry_date, is_organic):
        Product.__init__(self, category, product_id, name, price)   # Initialize base product
        self.expiry_date = expiry_date                               # Expiry date
        self.is_organic = is_organic                                 # Whether product is organic
    
    # Display groceries info
    def display(self):
        print(f"Category:{self.category}, Product ID:{self.product_id}, Name:{self.name}, "
              f"Price:{self.price}, Expiry Date:{self.expiry_date}, Organic:{self.is_organic}")



# OnlineExclusiveProduct inherits from Electronics, Clothing, and Groceries
class OnlineExclusiveProduct(Electronics, Clothing, Groceries):
    def __init__(self, category, product_id, name, price,
                 brand, warranty_years, expiry_date, is_organic,
                 size, material, discount_rate):

        # Initialize all parent classes manually (multiple inheritance)
        Electronics.__init__(self, category, product_id, name, price, brand, warranty_years)
        Clothing.__init__(self, category, product_id, name, price, size, material)
        Groceries.__init__(self, category, product_id, name, price, expiry_date, is_organic)

        self.discount_rate = discount_rate   # Extra feature: discount rate
    
    # Method to apply discount if product category is clothing
    def apply_discount(self):
        if self.category == "Clothing":
            discount_amount = (self.price * self.discount_rate) / 100
            final_price = self.price - discount_amount
            print(f"Discount Applicable:{self.discount_rate}%, Original Price:{self.price}, "
                  f"Discounted Price:{final_price}")
        else:
            print(f"No discount applicable for Category:{self.category}")
    
    # Display all combined features
    def display(self):
        print(f"Category:{self.category}, Product ID:{self.product_id}, Name:{self.name}, "
              f"Price:{self.price}, Brand:{self.brand}, Warranty:{self.warranty_years} years, "
              f"Expiry Date:{self.expiry_date}, Organic:{self.is_organic}, Size:{self.size}, "
              f"Material:{self.material}, Discount:{self.discount_rate}%")


# -------------------------------------------------------
# Creating objects and testing the classes
# -------------------------------------------------------

print("---Electronics---")
e1 = Electronics("Electronics", "E101", "Laptop", 75000, "Dell", 2)
e1.display()

print("---Clothing---")
c1 = Clothing("Clothing", "C202", "T-Shirt", 999, "L", "Cotton")
c1.display()

print("---Groceries---")
g1 = Groceries("Groceries", "G303", "Rice", 1200, "2026-01-01", True)
g1.display()

print("---Online EXclusive Price---")
ocp1 = OnlineExclusiveProduct("Clothing", "O404", "Jacket", 3000,
                              "Puma", 1, "NA", False,
                              "M", "Leather", 10)
ocp1.display()
ocp1.apply_discount()


"""
SAMPLE OUTPUT

---Electronics---
Category:Electronics, Product ID:E101, Name:Laptop, Price:75000, Brand:Dell, Warranty:2 years
---Clothing---
Category:Clothing, Product ID:C202, Name:T-Shirt, Price:999, Size:L, Material:Cotton
---Groceries---
Category:Groceries, Product ID:G303, Name:Rice, Price:1200, Expiry Date:2026-01-01, Organic:True
---Online EXclusive Price---
Category:Clothing, Product ID:O404, Name:Jacket, Price:3000, Brand:Puma, Warranty:1 years, Expiry Date:NA, Organic:False, Size:M, Material:Leather, Discount:10%
Discount Applicable:10%, Original Price:3000, Discounted Price:2700.0

"""