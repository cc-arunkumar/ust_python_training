# code shows how different car objects can hold varying attributes, illustrating object state 
# differences.

class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
    def accessories(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
    def accessories1(self,air_bags,abs,fog_lights):
        self.air_bags=air_bags
        self.abs=abs
        self.fog_lights=fog_lights
c1=Car("Tata","UST")
c1.accessories("Ac","Playlist","Rose")
print("Car 1:")
print(c1.__dict__)

c2=Car("BMW","Ferrori")
c2.accessories("6","Yes","Yes")
print("Car 2:")
print(c2.__dict__)

c3=Car("swift","Honda")
c3.accessories("Ac","melody","Lavendor")
c3.accessories1("6","Yes","Yes")
print("Car 3:")
print(c3.__dict__)

#output:

# Car 1:
# {'engine': 'Tata', 'fuel_injector': 'UST', 'ac': 'Ac', 'music': 'Playlist', 'perfume': 'Rose'}
# Car 2:
# {'engine': 'BMW', 'fuel_injector': 'Ferrori', 'ac': '6', 'music': 'Yes', 'perfume': 'Yes'}    
# Car 3:
# {'engine': 'swift', 'fuel_injector': 'Honda', 'ac': 'Ac', 'music': 'melody', 'perfume': 'Lavendor', 'air_bags': 
# '6', 'abs': 'Yes', 'fog_lights': 'Yes'}