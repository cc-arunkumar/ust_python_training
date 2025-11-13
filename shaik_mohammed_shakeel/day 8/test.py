class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
    
    def accessories_1(self,AC,perfume):
        self.AC=AC
        self.perfume=perfume

    def accessories_2(self,airbag,abs,fog_light):
        self.airbag=airbag
        self.abs=abs
        self.fog_light=fog_light

#calling Car

c1=Car("FORTUNER","Single-point")
print(c1.__dict__)
print("**********************")

#Calling the accessories without giving inputs to understand how it works
# c1.perfume
print(c1.__dict__)
print("**********************")

#Calling with inputs
c2=Car("ENDEAVOUR","Multi-point")
c2.accessories_1("LG","TMC")
print(c2.__dict__)
print("**********************")

c1.accessories_2(8,"YES","YES")
print(c1.__dict__)
