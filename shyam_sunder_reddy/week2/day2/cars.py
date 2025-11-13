class Car:    
    #creating the base car
    def __init__(self,engine,fuel_injectors):
        self.engine=engine
        self.fuel_injectors=fuel_injectors
    
    #Adding the accessories on top of base car
    def accessories1(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
    
    #Adding the accessories on top of base car
    def accessories2(self,airbags,abs,foglight):
        self.airbags=airbags
        self.abs=abs
        self.foglight=foglight

#creating the base car
c1=Car("tata","Ust")
print(c1.__dict__)
#this call  will give error as in the state of object the perfume doesnt exists yet
#print(c1.perfume)

#creating car with first accessories
c2=Car("maruthi","suzuki")
c2.accessories1("Voltos","boat","yarley")
print(c2.__dict__)

#creating car with second accessories
c3=Car("Mahindra","unicorn")
c3.accessories2("volvo","tata","lg")
print(c3.__dict__)

#creating car with two accessories
c4=Car("bmw","benz")
c4.accessories1("lg","jbl","wild stone")
c4.accessories2("Volvo","mg","lg")
print(c4.__dict__)

# #Sample output
# {'engine': 'tata', 'fuel_injectors': 'Ust'}
# {'engine': 'maruthi', 'fuel_injectors': 'suzuki', 'ac': 'Voltos', 'music': 'boat', 'perfume': 'yarley'}
# {'engine': 'Mahindra', 'fuel_injectors': 'unicorn', 'airbags': 'volvo', 'abs': 'tata', 'foglight': 'lg'}
# {'engine': 'bmw', 'fuel_injectors': 'benz', 'ac': 'lg', 'music': 'jbl', 'perfume': 'wild stone', 'airbags': 'Volvo', 'abs': 'mg', 'foglight': 'lg'}