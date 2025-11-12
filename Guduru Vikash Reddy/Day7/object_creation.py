# Step 1: Define the Emp class with attributes for ID, name, and salary
class Emp:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    # Step 2: Define a method to simulate promotion (though increment logic is missing)
    def promote(self,increment):
        self.increment
        print(f"{self.name} has promoted new salary is{self.salary}")

# Step 3: Create the first employee instance
emp1=Emp(1,"arjun reddy",40000)

# Step 4: Create the second employee instance
emp2=Emp(2,"Roy",50000)

# Step 5: Display details of both employees
print(f"Employee id:{emp1.id}")
print(f"Employee name:{emp1.name}")
print(f"Employee salary:{emp1.salary}")
print(f"Employee id:{emp2.id}")
print(f"Employee name:{emp2.name}")
print(f"Employee salary:{emp2.salary}")

# sample output
# Employee id:1
# Employee name:arjun reddy
# Employee salary:40000
# Employee id:2
# Employee name:Roy
# Employee salary:50000