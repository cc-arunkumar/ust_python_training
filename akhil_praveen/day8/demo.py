class Car:
    def __init__(self,engine ,fuel_injector):
        self._engine = engine
        self.__fuel_injector = fuel_injector
    def accessories1(self):
        self.ac =True
        self.music = True
        self.perfume = True
    def accessories2(self):
        self.airbag = True
        self.abs =True
        self.fog_light =True
        
        
c1 = Car("Tata","jaguar")
c1.accessories1()
print(c1.__dict__)
c2 = Car("Audi","Porsche")
c2.accessories2()
print(c2.__dict__)
c3 = Car("Supra","BMW")
c3.accessories1()
c3.accessories2()
print(c3.__dict__)