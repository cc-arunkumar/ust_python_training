class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
    def accessories1(self,AC,music,perfume):
        self.AC=AC
        self.music=music
        self.perfume=perfume
    def accessories2(self,airbag,abs,fog,light):
        self.airbag=airbag
        self.abs=abs
        self.fog=fog
        self.light=light
        
c1 = Car("Tata","UST")
print("***********************************")
print(c1.__dict__)
c2 = Car("BMW","XYZ")
c2.accessories1("Samsung","Sony","Wonders")
print("***********************************")
print(c2.__dict__)
c1.accessories2("abc","xyz","xbc","sd")
print("***********************************")
print(c1.__dict__)
c1.accessories1("sams","boat","wg")
c1.accessories2("xvc","df","jksj","hvel")
print("***********************************")
print(c1.__dict__)


        