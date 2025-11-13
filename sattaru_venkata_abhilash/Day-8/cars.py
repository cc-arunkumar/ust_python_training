# -------------------------------------
# Class Definition for Cars
# -------------------------------------
class Cars:
    def __init__(self, engine, fuelinjector):
        # Engine and Fuel Injector (Basic Information)
        self.engine = engine
        self.fuelinjector = fuelinjector

    # -------------------------------------
    # Accessories Set 1: AC, Music System, Perfume
    # -------------------------------------
    def accessories1(self, ac, music, perfume):
        self.ac = ac
        self.music = music
        self.perfume = perfume

    # -------------------------------------
    # Accessories Set 2: Airbags, ABS
    # -------------------------------------
    def accessories2(self, airbags, abs):
        self.airbags = airbags
        self.abs = abs


# -------------------------------------
# Object Creation + OWN ACCESSORIES
# -------------------------------------

# Car 1 — Only Accessories1
c1 = Cars("Tata", "UST")
c1.accessories1("Automatic AC", "Sony Music System", "Jasmine Perfume")
print("\nCar 1 Details:", c1.__dict__)

# Car 2 — Only Accessories2
c2 = Cars("BMW", "Ferrari")
c2.accessories2("6 Airbags", "ABS Enabled")
print("\nCar 2 Details:", c2.__dict__)

# Car 3 — Both Accessories1 + Accessories2
c3 = Cars("Audi", "Apex")
c3.accessories1("Dual Zone AC", "Bose Music System", "Lavender Perfume")
c3.accessories2("8 Airbags", "Premium ABS")
print("\nCar 3 Details:", c3.__dict__)



# sample output:
# Car 1 Details: {
#  'engine': 'Tata',
#  'fuelinjector': 'UST',
#  'ac': 'Automatic AC',
#  'music': 'Sony Music System',
#  'perfume': 'Jasmine Perfume'
# }

# Car 2 Details: {
#  'engine': 'BMW',
#  'fuelinjector': 'Ferrari',
#  'airbags': '6 Airbags',
#  'abs': 'ABS Enabled'
# }

# Car 3 Details: {
#  'engine': 'Audi',
#  'fuelinjector': 'Apex',
#  'ac': 'Dual Zone AC',
#  'music': 'Bose Music System',
#  'perfume': 'Lavender Perfume',
#  'airbags': '8 Airbags',
#  'abs': 'Premium ABS'
# }
