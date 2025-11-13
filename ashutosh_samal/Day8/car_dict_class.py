#Cars class creation
class Cars:
    def __init__(self,engine,fuelinjecter):
        self.engine = engine
        self.fuelinjecter = fuelinjecter
    
    # function to add accessories
    def accessories1(self,ac,music,perfume):
        self.ac = ac
        self.music = music
        self.perfume = perfume
        
    def accessories2(self,airbag,abs,foglight):
        self.airbag = airbag
        self.abs = abs
        self.foglight = foglight


#object creation and Calling the functions
c1 = Cars("TATA","Delphi")
c1.accessories1("GE","JBL","Yes")
print(c1.__dict__)
print("============================================================================")

c2 = Cars("BMW","Bosch")
c2.accessories1("Bergstorm","Bowers & Wilkins","Not needed")
c2.accessories2("Valeo","Bosch","Osram")
print(c2.__dict__)
print("============================================================================")

c3 = Cars("Honda","Denso")
c3.accessories2("Honda Global","Honda","Osram")
print(c3.__dict__)
print("============================================================================")


#Sample Output
# {'engine': 'TATA', 'fuelinjecter': 'Delphi', 'ac': 'GE', 'music': 'JBL', 'perfume': 'Yes'}
# ============================================================================
# {'engine': 'BMW', 'fuelinjecter': 'Bosch', 'ac': 'Bergstorm', 'music': 'Bowers & Wilkins', 'perfume': 'Not needed', 'airbag': 'Valeo', 'abs': 'Bosch', 'foglight': 'Osram'}
# ============================================================================
# {'engine': 'Honda', 'fuelinjecter': 'Denso', 'airbag': 'Honda Global', 'abs': 'Honda', 'foglight': 'Osram'}
# ============================================================================