class Car:
    def __init__(self,engine,fuel_injector):
        self.engine = engine
        self.fuel_injector = fuel_injector

    def accessories1(self,ac,music,perfume):
        self.ac = ac
        self.music = music
        self.perfume = perfume

    def accessories2(self,airbag,abs,fog_light):
        self.airbag = airbag
        self.abs = abs
        self.fog_light = fog_light

c1 = Car("TATA","UST")
print(c1.__dict__)
print("------------------------------------------------------------")

c1.accessories1("Baleno","JBL","freshair")
print(c1.__dict__)
print("-------------------------------------------------------------")

c2 = Car("Fortuner","Infosys")
c2.accessories1("LG","Sony","Airfresh")
print(c2.__dict__)
print("================================================================")

c2.accessories2("Honda","Ferrari","BMW")
print(c2.__dict__)


# -----------------------------------------------------------------------------------------------

# Sample Output

# {'engine': 'TATA', 'fuel_injector': 'UST'}
# ------------------------------------------------------------
# {'engine': 'TATA', 'fuel_injector': 'UST', 'ac': 'Baleno', 'music': 'JBL', 'perfume': 'freshair'}
# -------------------------------------------------------------
# {'engine': 'Fortuner', 'fuel_injector': 'Infosys', 'ac': 'LG', 'music': 'Sony', 'perfume': 'Airfresh'} 
# ================================================================
# {'engine': 'Fortuner', 'fuel_injector': 'Infosys', 'ac': 'LG', 'music': 'Sony', 'perfume': 'Airfresh', 'airbag': 'Honda', 'abs': 'Ferrari', 'fog_light': 'BMW'}

