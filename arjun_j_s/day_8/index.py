class Car:

    def __init__(self,engine,fuel_inject):
        self.engine = engine
        self.fuel_inject = fuel_inject

    def access1(self):
        self.air_bag = True
        self.abs = True
        self.fog_light = True
    
    def access2(self):
        self.perfume = True
        self.a_c = True
        self.music = True
    
c1 = Car("BMW","Ferrari")
c2 = Car("Audi","Tata")
print(f"Base car : {c1.__dict__}")
c1.access1()
print(f"With access 1 : {c1.__dict__}")
c2.access2()
print(f"With access 2 : {c2.__dict__}")
c1.access2()
print(f"With access 1 and 2 : {c1.__dict__}")

class Employee:

    def __init__(self):
        self.name = "Arjun"
        self._desig = "SDE 1"
        self.__salary = "40000"
    
emp = Employee()

#Public Data
print("Name :",emp.name)

#Protected Data
print("Designation :",emp._desig)

#Private Data accessed through mangled name ie _ClassName__variable
print("Salary :",emp._Employee__salary)

#Output
# Base car : {'engine': 'BMW', 'fuel_inject': 'Ferrari'}
# With access 1 : {'engine': 'BMW', 'fuel_inject': 'Ferrari', 'air_bag': True, 'abs': True, 'fog_light': True}
# With access 2 : {'engine': 'Audi', 'fuel_inject': 'Tata', 'perfume': True, 'a_c': True, 'music': True}
# With access 1 and 2 : {'engine': 'BMW', 'fuel_inject': 'Ferrari', 'air_bag': True, 'abs': True, 'fog_light': True, 'perfume': True, 'a_c': True, 'music': True}
# Name : Arjun
# Designation : SDE 1
# Salary : 40000