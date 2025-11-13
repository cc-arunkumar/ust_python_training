#Task : Car acessories 

#Code
class Car:
    def __init__(self,engine,fuelInjector):
        
        self.engine=engine
        self.fuelInjector= fuelInjector
    def show(self):
        self.engine
        self.fuelInjector
        
    def accessories1(self,AC,music,perfume):
        
        self.AC=AC
        self.music=music
        self.perfume=perfume
    def accessories2(self,airbag,abs,foglight):
        
        self.airbag=airbag
        self.abs=abs
        self.foglight=foglight
c1=Car("Tata","UST")
c1.show()
print(c1.__dict__)
c1.accessories1("Voltas","Harman Music","Air")
print(c1.__dict__)
c1.accessories2("Tata-Airbag","Tata-Airbag","Tata-foglight")
print(c1.__dict__)

# #Output
# {'engine': 'Tata', 'fuelInjector': 'UST'}
# {'engine': 'Tata', 'fuelInjector': 'UST', 'AC': 'Voltas', 'music': 'Harman Music', 'perfume': 'Air'}
# {'engine': 'Tata', 'fuelInjector': 'UST', 'AC': 'Voltas', 'music': 'Harman Music', 'perfume': 'Air', 'airbag': 'Tata-Airbag', 'abs': 'Tata-Airbag', 'foglight': 'Tata-foglight'}

