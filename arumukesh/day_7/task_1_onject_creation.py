class Employee:
    def __init__(self,emp_id,name,dept,salary):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary
# definition to print the details of employee
    def show_info(self):
        print(f"employee_id:{self.emp_id}|name:{self.name}|department:{self.dept}|salary:{self.salary}")
# to find the yearly salary details
    def calculate_yearly_salary(self):
        return self.salary*12
# to modify slary details
    def  apply_bonus(self):
        if self.dept=="IT":
            self.salary+=0.1*self.salary
        if self.dept=="HR":
            self.salary+=0.08*self.salary
        if self.dept=="Finance":
            self.salary+=0.12*self.salary
        else:
            self.salary+=0.05*self.salary
        print("bonus applied")


emp1=Employee("E101","swathi","IT",50000)
emp1.show_info()
emp1.apply_bonus()
emp1.show_info()
yearly_sal=emp1.calculate_yearly_salary()
print(emp1.name," yearly salary:",yearly_sal)
            

# employee_id:E101|name:swathi|department:IT|salary:50000
# bonus applied
# employee_id:E101|name:swathi|department:IT|salary:57750.0
# swathi  yearly salary: 693000.0 