class Car:
    def __init__(self,engine,fuel_injector):
        self.engine=engine
        self.fuel_injector=fuel_injector

    def accessories1(self,music_system,neon_lights,ventilated_seats):
        self.music_system=music_system
        self.neon_lights=neon_lights
        self.ventilated_seats=ventilated_seats

    def accessories2(self,air_bag,abs,additional_silencer):
        self.air_bag=air_bag
        self.abs=abs
        self.additional_silencer=additional_silencer

ambasidior=Car("TATA","Mahindrea")
print(ambasidior.__dict__)

# Car with only 1st accessories
jaguar=Car("jaguar","jaguar")
jaguar.accessories1("JBL","End-to-end","Yes")
print(jaguar.__dict__)
print("---------------------------------------------------------------------")

# Car with only 2nd accessories
lambogeni=Car("VOLKSVAGEN","audi")
lambogeni.accessories2("Installed","4-wheels","Throttle sound_with fire")
print(lambogeni.__dict__)
print("---------------------------------------------------------------------")

# Car with both accessories
BMW=Car("Ferrari","ferrari")
BMW.accessories1("Marshell","End-to-end","Yes")
BMW.accessories2("Installed","4-wheels","Throttle sound_Boosted")
print(BMW.__dict__)



