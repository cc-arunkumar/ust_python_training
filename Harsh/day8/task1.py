class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
        
    def accs1(self,ac,music,perfume):
        self.ac=ac
        self.music=music
        self.perfume=perfume
        
    def accs2(self,airbag,abs,foglight):
        self.airbag=airbag
        self.abs=abs
        self.foglight=foglight


c1=Car("Tata","MPFI")
print("------------------------------------------------")
print(c1.__dict__)
print("------------------------------------------------")
c2=Car("BMW","MPFI")
c2.accs1("Hitachi","Sony","Dior")
print(c2.__dict__)
print("------------------------------------------------")
c3=Car("Porsche","MPFI")
c3.accs2("Yes","Yes","No")
print(c3.__dict__)   
print("------------------------------------------------")     
c4=Car("Buggati","MPIF")
c4.accs1("Hitachi","Sony","Dior")
c4.accs2("Yes","Yes","Yes")
print(c4.__dict__) 
print("------------------------------------------------") 



# ------------------------------------------------
# {'engine': 'Tata', 'fuel_injector': 'MPFI'}
# ------------------------------------------------
# {'engine': 'BMW', 'fuel_injector': 'MPFI', 'ac': 'Hitachi', 'music': 'Sony', 'perfume': 'Dior'}
# ------------------------------------------------
# {'engine': 'Porsche', 'fuel_injector': 'MPFI', 'airbag': 'Yes', 'abs': 'Yes', 'foglight': 'No'}
# ------------------------------------------------
# {'engine': 'Buggati', 'fuel_injector': 'MPIF', 'ac': 'Hitachi', 'music': 'Sony', 'perfume': 'Dior', 'airbag': 'Yes', 'abs': 'Yes', 'foglight': 'Yes'}
# ------------------------------------------------
