class Cars:
    def __init__(self,engine,fuel_injection):
        self.engine=engine
        self.fuel_injection=fuel_injection
    
    def accessories(self,Ac,music,perfume):
        self.Ac=Ac
        self.music=music
        self.perfume=perfume
    
    def Accessories(self,airbag,abs,fog):
        self.airbag=airbag
        self.abs=abs
        self.fog=fog


c1=Cars("Tata","UST")
c1.accessories("Yes","Sony","Nivea")
print(c1.__dict__)

c2=Cars("BMW","Own Engine")
c2.Accessories(6,"Dual ABS","Hella")
print(c2.__dict__)
c1.Accessories(2,"NO ABS","Default")
print(c1.__dict__)
"""
OUTPUT FOR ABOVE

{'engine': 'Tata', 'fuel_injection': 'UST', 'Ac': 'Yes', 'music': 'Sony', 'perfume': 'Nivea'}
{'engine': 'BMW', 'fuel_injection': 'Own Engine', 'airbag': 6, 'abs': 'Dual ABS', 'fog': 'Hella'}
{'engine': 'Tata', 'fuel_injection': 'UST', 'Ac': 'Yes', 'music': 'Sony', 'perfume': 'Nivea', 'airbag': 2, 'abs': 'NO ABS', 'fog': 'Default'}
"""

# C2 object is not using the method that has perfume
print(c2.perfume)

""""
AttributeError: 'Cars' object has no attribute 'perfume'
"""