class Cars:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector
    
    def accessories(self,AC,Purifier,TPMS):
        self.AC=AC
        self.Purifier=Purifier
        self.TPMS=TPMS
    
    def imp_accessories(self,airbag,ADAS,foglight):
        self.airbag=airbag
        self.ADAS=ADAS
        self.foglight=foglight
    

c1=Cars("Nissan","npme")
c1.accessories("Blue star","Xioami","4 tyre Nissan TPMS")
print(c1.__dict__)
print("----------------------------------------------------------------------")


c2=Cars("Volkswagen","vpme")
c2.imp_accessories("Level-5","Level-2","White Foglights")
print(c2.__dict__)
print("----------------------------------------------------------------------")


c3=Cars("Benz","bpme")
print(c3.__dict__)