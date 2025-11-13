class Car:
    def __init__(self,engine,fuleinject):
        self.engine=engine
        self.fuelinject=fuleinject
    def accessories1(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
    def accessories2(self,airbag,abs,foglight):
        self.airbag=airbag
        self.abs=abs
        self.foglight=foglight
c1=Car("Tata","UST")
c1.accessories1("dual","Sony","godridge")
print(c1.__dict__)

c2=Car("BMW","Ferrari")
c2.accessories2(6,"dual channel","yes")
print(c2.__dict__)

c3=Car("Honda","Audi")
c3.accessories1("dual","Sony","godridge")
c3.accessories2(6,"dual channel","yes")
print(c3.__dict__)

c4=Car("Suzuki","BMW")
c4.accessories1("Sony","godridge",6)
print(c4.__dict__)


#Sample Execution
# {'engine': 'Tata', 'fuelinject': 'UST', 'ac': 'dual', 'music': 'Sony', 'perfume': 'godridge'}
# {'engine': 'Honda', 'fuelinject': 'Audi', 'ac': 'dual', 'music': 'Sony', 'perfume': 'godridge', 'air': 'dual channel', 'foglight': 'yes'}
# {'engine': 'Suzuki', 'fuelinject': 'BMW', 'ac': 'Sony', 'music': 'godridge', 'perfume': 6}

        