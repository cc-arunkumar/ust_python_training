#base class
class Car:
    def __init__(self,engine,fuel_injector):
        self.engine = engine
        self.fuel_injector = fuel_injector

    def accessories1(self,AC,music,perfume):
        self.AC = AC
        self.music = music
        self.perfume = perfume

    def accessories2(self,airbag,abs,fog_light):
        self.airbag = airbag
        self.abs = abs
        self.fog_light = fog_light
        
#testing

# c1 = Car("TATA","Volkswagen")
# print(c1.__dict__)

# c2 = Car("Ferrari","BMW")
# c2.accessories1("avail","avail","not-avail")
# print(c2.__dict__)

# c3 = Car("Benz","Audi")
# c3.accessories2("avail","avail","not-avail")
# print(c3.__dict__)

c4 = Car("Mahendra","suzuki")
c4.accessories1("on","playing","fog")
c4.accessories2("enabled","not-avail","avail")
print(c4.__dict__)

# sample output:

# {'engine': 'Mahendra', 'fuel_injector': 'suzuki', 'AC': 'on', 'music': 'playing', 'perfume': 'fog', 'airbag': 'enabled', 'abs': 'not-avail', 'fog_light': 'avail'}



