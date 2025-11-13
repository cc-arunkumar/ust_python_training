#Base class
class Car:
    def __init__(self , engine,fuelinjector):
        self.engine = engine
        self.fuelinjector = fuelinjector
    
    #methods to add more attributes    
    def accessories1(self , ac,music,perfume):
        self.ac = ac
        self.music = music
        self.perfume = perfume
        
    def accessories2(self ,airbag,abs,foglight):
        self.airbag = airbag
        self.abs = abs
        self.foglight = foglight
        
c1 = Car("tata","USA")
print("Car1:")
c1.accessories1("cool","plesent","good")
print(c1. __dict__ )

c2 = Car("BMW","India")
print("car1:")
c1.accessories1("yes","yes","used")
c2.accessories2("present","used","present")
print(c1. __dict__ )
print("car2:")
print(c2.__dict__)

#output
# Car1:
# {'engine': 'tata', 'fuelinjector': 'USA', 'ac': 'cool', 'music': 'plesent', 'perfume': 'good'}
# car1:
# {'engine': 'tata', 'fuelinjector': 'USA', 'ac': 'yes', 'music': 'yes', 'perfume': 'used'}
# car2:
# {'engine': 'BMW', 'fuelinjector': 'India', 'airbag': 'present', 'abs': 'used', 'foglight': 'present'}