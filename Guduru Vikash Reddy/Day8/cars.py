# Step 1: Define the Car class with engine and fuel injection attributes
class Car:
    def __init__(self,engine,fuelinjection):
        self.engine=engine
        self.fuelinjection=fuelinjection

    # Step 2: Define accessories1 method to add AC, music system, and perfume
    def accessories1(self,ac,music,perfume):
        self.ac=ac
        self.musics=music
        self.perfume=perfume

    # Step 3: Define accessories2 method to add airbags, ABS, and fog lights
    def accessories2(self,airbags,abs,fog_lights):
        self.airbags=airbags
        self.abs=abs
        self.fog_lights=fog_lights

# Step 4: Create first car object and assign accessories1
c1=Car("kia","multi injection")
# c1.perfume()
c1.accessories1("Daikin","sony","ks")
print(c1.__dict__)

# Step 5: Create second and third car objects and assign accessories2 and accessories1
c2=Car("mg","single injection")
c2.accessories2("topnotch","null","premiun lights")
print(c2.__dict__)

c3=Car("toyota","multi injection")
c3.accessories2("lowlevel","NA","ledlights")
c3.accessories1("lg","philips","ns")
print(c3.__dict__)

# sample output
# {'engine': 'kia', 'fuelinjection': 'multi injection', 'ac': 'Daikin', 'musics': 'sony', 'perfume': 'ks'}
# {'engine': 'mg', 'fuelinjection': 'single injection', 'airbags': 'topnotch', 'abs': 'null', 'fog_lights': 'premiun lights'}
# {'engine': 'toyota', 'fuelinjection': 'multi injection', 'airbags': 'lowlevel', 'abs': 'NA', 'fog_lights': 'ledlights', 'ac': 'lg', 'musics': 'philips', 'perfume': 'ns'}
        
        