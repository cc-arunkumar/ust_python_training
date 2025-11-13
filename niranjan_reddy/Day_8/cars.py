class Cars:
    def __init__(self,engine,fuelinjector):
        self.engine=engine
        self.fuelinjector=fuelinjector

    def accessories1(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
    
    def accessories2(self,airbag,abs):
        self.airbag=airbag
        self.abs=abs

c=Cars("hundai","tata")
# c.perfume
print(c.__dict__)


c1=Cars("Tata","UST")
c1.accessories1("haier","tseries","fog")
print(c1.__dict__)

c2=Cars("BMW","Ferari")
c2.accessories2("indigo","ceat")
print(c2.__dict__)

c3=Cars("Suzuki","Skoda")
c3.accessories1("voltas","sony","h2")
c3.accessories2("punch","abs")
print(c3.__dict__)


# Sample output

# {'engine': 'hundai', 'fuelinjector': 'tata'}
# {'engine': 'Tata', 'fuelinjector': 'UST', 'ac': 'haier', 'music': 'tseries', 'perfume': 'fog'}
# {'engine': 'BMW', 'fuelinjector': 'Ferari', 'airbag': 'indigo', 'abs': 'ceat'}
# {'engine': 'Suzuki', 'fuelinjector': 'Skoda', 'ac': 'voltas', 'music': 'sony', 'perfume': 'h2', 'airbag': 'punch', 'abs': 'abs'}