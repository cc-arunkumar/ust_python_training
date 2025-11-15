
class Car:
    # Constructor method to initialize
    def __init__(self,engine,fuel_injector):
        self.engine = engine
        self.fuel_injector = fuel_injector
        
    # Method to add first set of accessories (comfort-related)
    def accessories1(self,ac,music,perfume):
        self.ac  = ac 
        self.music = music 
        self.perfume = perfume
        
    # Method to add second set of accessories (safety-related)
    def accessories2(self,airbag,foglight,abs):
        self.airbag = airbag 
        self.foglight = foglight 
        self.abs = abs 

# Create a Car object
c1 = Car('Tata','suzuki')
c1.accessories2('Sleepwell','Fogg','Ceat')
print(c1.airbag)
print(c1.abs)
print(c1.foglight)
print(c1.__dict__)

# output:
# Sleepwell
# Ceat
# Fogg
# { 'engine': 'Tata', 'fuel_injector': 'suzuki', 'airbag': 'Sleepwell', 'foglight': 'Fogg', 'abs': 'Ceat'
# }
   
   
   

# class Test:
#     def __init__(self):
#         self.a=10
#         #self.b=20
#     def show(self):
#         self.c = 40
    
# n1 = Test()
# n1.show()

# print(n1.__dict__)      
