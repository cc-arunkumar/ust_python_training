class Car:
    def __init__(self,company_name,model):
        self.company_name=company_name
        self.model = model
        
    def print_values(self):
        print(self.company_name, " ", self.model)
    
    def add_acesorries1(self):
        self.perfume = "yes"
        self.air_bag = "yes"
        self.ac = "yes"
        
    def add_acesorries2(self):
        self.fog_light = "yes"
        self.alloy_wheels_custom = "yes"
        self.extra_storage = "yes"
        
    def print_with_accesories1(self):
        print(self.company_name," ", self.model, " ", self.perfume, " ", self.air_bag, " ", self.ac)
    def print_with_accesories2(self):
        print(self.company_name," ", self.model, " ", self.fog_light, " ", self.alloy_wheels_custom, " ", self.extra_storage)
    def print_with_accesories_1_2(self):
        print(self.company_name," ", self.model, " ", self.fog_light, " ", self.alloy_wheels_custom, " ", self.extra_storage," ", self.perfume, " ", self.air_bag, " ",self.ac)


car1= Car("BMW", "X5")
car1.print_values()

car2 = Car("Audi", "A8")
car2.add_acesorries1()
car2.print_with_accesories1()

car3 = Car("Mercedes","S-class")
car3.add_acesorries2()
car3.print_with_accesories2()


car4 = Car("Range_rover","velarr")
car4.add_acesorries1()
car4.add_acesorries2()
car4.print_with_accesories_1_2()
    