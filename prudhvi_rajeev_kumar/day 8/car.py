class Car:
    def __init__(self, engine, fuelEngine):
        self.engine = engine
        self.fuelEngine = fuelEngine
        
    def accessories1(self, AC, music, perfume):
        self.AC = AC
        self.music = music
        self.perfume = perfume
        
    def accessories2(self, airbag, abs, foglight):
        self.airbag = airbag
        self.abs = abs
        self.foglight = foglight
        
c1 = Car("Tata", "BharatBenz")
c1.accessories1("AC", "Sony Speaker", "Perfume Added in it.")
print(c1.__dict__)

