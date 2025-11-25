# Define Car class
class Car:
    def __init__(self, company_name, model):
        # Initialize car with company name and model
        self.company_name = company_name
        self.model = model
        
    def print_values(self):
        # Print basic car details (company and model)
        print(self.company_name, " ", self.model)
    
    def add_acesorries1(self):
        # Add first set of accessories
        self.perfume = "yes"
        self.air_bag = "yes"
        self.ac = "yes"
        
    def add_acesorries2(self):
        # Add second set of accessories
        self.fog_light = "yes"
        self.alloy_wheels_custom = "yes"
        self.extra_storage = "yes"
        
    def print_with_accesories1(self):
        # Print car details along with accessories from set 1
        print(self.company_name, " ", self.model, " ", self.perfume, " ", self.air_bag, " ", self.ac)
    
    def print_with_accesories2(self):
        # Print car details along with accessories from set 2
        print(self.company_name, " ", self.model, " ", self.fog_light, " ", self.alloy_wheels_custom, " ", self.extra_storage)
    
    def print_with_accesories_1_2(self):
        # Print car details along with accessories from both sets
        print(self.company_name, " ", self.model, " ", 
              self.fog_light, " ", self.alloy_wheels_custom, " ", self.extra_storage, " ", 
              self.perfume, " ", self.air_bag, " ", self.ac)


# Create car1 object (BMW X5) and print only basic details
car1 = Car("BMW", "X5")
car1.print_values()

# Create car2 object (Audi A8), add accessories set 1, and print with accessories
car2 = Car("Audi", "A8")
car2.add_acesorries1()
car2.print_with_accesories1()

# Create car3 object (Mercedes S-class), add accessories set 2, and print with accessories
car3 = Car("Mercedes", "S-class")
car3.add_acesorries2()
car3.print_with_accesories2()

# Create car4 object (Range Rover Velarr), add both sets of accessories, and print with all
car4 = Car("Range_rover", "velarr")
car4.add_acesorries1()
car4.add_acesorries2()
car4.print_with_accesories_1_2()


# ==============sample output=======================
# BMW   X5
# Audi   A8   yes   yes   yes
# Mercedes   S-class   yes   yes   yes
# Range_rover   velarr   yes   yes   yes   yes   yes   yes
