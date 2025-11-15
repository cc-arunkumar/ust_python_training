class Car:
    def __init__(self, engine, fuel_injector):
        # Base attributes initialized when a Car object is created
        self.engine = engine
        self.fuel_injector = fuel_injector
        
        # Initialize accessory attributes with default values (None means not set yet)
        self.ac = None
        self.music = None
        self.perfume = None
        self.airbag = None
        self.abs = None
        self.foglight = None
        
    def accs1(self, ac, music, perfume):
        # Method to add first set of accessories
        self.ac = ac
        self.music = music
        self.perfume = perfume
        
    def accs2(self, airbag, abs, foglight):
        # Method to add second set of accessories
        self.airbag = airbag
        self.abs = abs
        self.foglight = foglight


# ------------------- Testing -------------------

# Car object with only base attributes
c1 = Car("Tata", "MPFI")
print("------------------------------------------------")
print(c1.__dict__)   # __dict__ shows all attributes of the object

# Car object with accs1 accessories added
print("------------------------------------------------")
c2 = Car("BMW", "MPFI")
c2.accs1("Hitachi", "Sony", "Dior")   # Add AC, music system, perfume
print(c2.__dict__)

# Car object with accs2 accessories added
print("------------------------------------------------")
c3 = Car("Porsche", "MPFI")
c3.accs2("Yes", "Yes", "No")   # Add safety features
print(c3.__dict__)

# Car object with both accs1 and accs2 accessories added
print("------------------------------------------------")
c4 = Car("Buggati", "MPFI")
c4.accs1("Hitachi", "Sony", "Dior")
c4.accs2("Yes", "Yes", "Yes")
print(c4.__dict__)
print("------------------------------------------------")




# ------------------------------------------------
# {'engine': 'Tata', 'fuel_injector': 'MPFI'}
# ------------------------------------------------
# {'engine': 'BMW', 'fuel_injector': 'MPFI', 'ac': 'Hitachi', 'music': 'Sony', 'perfume': 'Dior'}
# ------------------------------------------------
# {'engine': 'Porsche', 'fuel_injector': 'MPFI', 'airbag': 'Yes', 'abs': 'Yes', 'foglight': 'No'}
# ------------------------------------------------
# {'engine': 'Buggati', 'fuel_injector': 'MPIF', 'ac': 'Hitachi', 'music': 'Sony', 'perfume': 'Dior', 'airbag': 'Yes', 'abs': 'Yes', 'foglight': 'Yes'}
# ------------------------------------------------
