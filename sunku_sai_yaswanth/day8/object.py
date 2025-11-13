class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
    def accessories1(self,AC,music,perfume):
        self.AC=AC
        self.music=music
        self.perfume=perfume
    def accessories2(self,airbag,abs,fog_lights):
        self.airbag=airbag
        self.abs=abs
        self.fog_lights=fog_lights

c1=Car("Tata","UST")
# c1.perfume()
c1.accessories1("hp","ubl","foog")
print(c1.__dict__)
c2=Car("Honda","UST")
c2.accessories2("new","ydf","brand new")
print(c2.__dict__)
c3=Car("maruthi","suzuki")
c3.accessories2("old","gyh","brandnew")
c3.accessories1("samsung","rick","godrej")
print(c3.__dict__)


# output
# {'engine': 'Tata', 'fuel_injector': 'UST', 'AC': 'hp', 'music': 'ubl', 'perfume': 'foog'}
# {'engine': 'Honda', 'fuel_injector': 'UST', 'airbag': 'new', 'abs': 'ydf', 'fog_lights': 'brand new'}
# {'engine': 'maruthi', 'fuel_injector': 'suzuki', 'airbag': 'old', 'abs': 'gyh', 'fog_lights': 'new', 'AC': 'samsung', 'music': 'rick', 'perfume': 'godrej'}  