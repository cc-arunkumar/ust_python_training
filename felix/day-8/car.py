class Car:
    def __init__(self,engine,fuelinjector):
        self.engine = engine
        self.fuelinjector = fuelinjector
        
    def accessories1(self,ac,music,perfume):
        self.ac = ac
        self.music = music
        self.perfume =perfume
    
    def accessories2(self,airbags,abs,foglight):
        self.airbags = airbags
        self.abs = abs
        self.foglight = foglight
        
c1 = Car("Tata","UST")
print(c1.__dict__)
c1.accessories1("Ac","Kenwood","Perfume")
print(c1.__dict__)
c1.accessories2("AirBags","ABS","Foglight")
print(c1.__dict__)

c2 = Car("BMW","Ferrari")
print(c2.__dict__)
c2.accessories1("Ac","BOSE","Perfume")
print(c2.__dict__)
c2.accessories2("AirBags","ABS","Foglight")
print(c2.__dict__)

c3 = Car("Honda","Yemaha")
print(c3.__dict__)
c3.accessories1("Ac","BOAT","Perfume")
print(c3.__dict__)
c3.accessories2("AirBags","ABS","Foglight")
print(c3.__dict__)

c4 = Car("Benz","Petronas")
print(c4.__dict__)
c4.accessories1("Ac","BOSE","Perfume")
print(c4.__dict__)
c4.accessories2("AirBags","ABS","Foglight")
print(c4.__dict__)

# output

# {'engine': 'Tata', 'fuelinjector': 'UST'}
# {'engine': 'Tata', 'fuelinjector': 'UST', 'ac': 'Ac', 'music': 'Kenwood', 'perfume': 'Perfume'}   
# {'engine': 'Tata', 'fuelinjector': 'UST', 'ac': 'Ac', 'music': 'Kenwood', 'perfume': 'Perfume', 'airbags': 'AirBags', 'abs': 'ABS', 'foglight': 'Foglight'}
# {'engine': 'BMW', 'fuelinjector': 'Ferrari'}
# {'engine': 'BMW', 'fuelinjector': 'Ferrari', 'ac': 'Ac', 'music': 'BOSE', 'perfume': 'Perfume'}   
# {'engine': 'BMW', 'fuelinjector': 'Ferrari', 'ac': 'Ac', 'music': 'BOSE', 'perfume': 'Perfume', 'airbags': 'AirBags', 'abs': 'ABS', 'foglight': 'Foglight'}
# {'engine': 'Honda', 'fuelinjector': 'Yemaha'}
# {'engine': 'Honda', 'fuelinjector': 'Yemaha', 'ac': 'Ac', 'music': 'BOAT', 'perfume': 'Perfume'}  
# {'engine': 'Honda', 'fuelinjector': 'Yemaha', 'ac': 'Ac', 'music': 'BOAT', 'perfume': 'Perfume', 'airbags': 'AirBags', 'abs': 'ABS', 'foglight': 'Foglight'}
# {'engine': 'Benz', 'fuelinjector': 'Petronas'}
# {'engine': 'Benz', 'fuelinjector': 'Petronas', 'ac': 'Ac', 'music': 'BOSE', 'perfume': 'Perfume'} 
# {'engine': 'Benz', 'fuelinjector': 'Petronas', 'ac': 'Ac', 'music': 'BOSE', 'perfume': 'Perfume', 
# 'airbags': 'AirBags', 'abs': 'ABS', 'foglight': 'Foglight'}