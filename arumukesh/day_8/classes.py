class Car:
    def __init__(self,engine,fuel_inj):
        self.engine=engine
        self.fuelinjector=fuel_inj
    def accessories_1(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
    def accessories_2(self,airbag=None,abs=None):
        self.airbag=airbag
        self.abs=abs
c1=Car("BMW","Honda")
c1.accessories_1("flow","JBL","perf")
print(c1.__dict__)

c1.accessories_2(None,"SS-airbags")
print(c1.__dict__)
c2=Car("Hyundai","fiat")
c2.accessories_1("airr",None,"dior")
print(f"C2 AC:{c2.ac}")
print(c2.__dict__)
# print(c2.abs)
c3=Car("TATA","TATA")
c3.accessories_2("honda-abs","ss airbags")
print(c3.__dict__)


    