class Car:
    def __init__(self,engine,fuelinjector):
        self.engine=engine
        self .fuelinjector=fuelinjector
    
    def accessories1(self,ac,musicsystem,perfume):
        self.ac=ac
        self.musicsystem=musicsystem
        self.perfume=perfume
    def accessories2(self,carburetor,radiator):
        self.carburetor=carburetor
        self.radiator=radiator 
        


c1=Car("Tata","injector")
print(c1.__dict__)
# print(c1.perfume) AttributeError: 'Car' object has no attribute 'perfume'
c1.accessories1("AC","newmusic","lily")
print(c1.__dict__)
c1.accessories2("carburateofixed","radiatorfixed")
print(c1.__dict__)


c2=Car("BMW","bmwfuelinjector")
print(c2.__dict__)
c2.accessories1("AC","newmusic","lily")
print(c2.__dict__)
c2.accessories2("carburateofixed","radiatorfixed")
print(c2.__dict__)



# sample execution 
# {'engine': 'Tata', 'fuelinjector': 'injector'}
# {'engine': 'Tata', 'fuelinjector': 'injector', 'ac': 'AC', 'musicsystem': 'newmusic', 'perfume': 'lily'}
# {'engine': 'Tata', 'fuelinjector': 'injector', 'ac': 'AC', 'musicsystem': 'newmusic', 'perfume': 'lily', 'carburetor': 'carburateofixed', 'radiator': 'radiatorfixed'}
# {'engine': 'BMW', 'fuelinjector': 'bmwfuelinjector'}
# {'engine': 'BMW', 'fuelinjector': 'bmwfuelinjector', 'ac': 'AC', 'musicsystem': 'newmusic', 'perfume': 'lily'}
# {'engine': 'BMW', 'fuelinjector': 'bmwfuelinjector', 'ac': 'AC', 'musicsystem': 'newmusic', 'perfume': 'lily', 'carburetor': 'carburateofixed', 'radiator': 'radiatorfixed'}