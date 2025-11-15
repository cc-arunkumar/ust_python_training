# Constructor Chainig

class Employee:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def show_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Dept: {self.dept}")


class Developer(Employee):
    def __init__(self, id, name, dept, platform):
        super().__init__(id, name, dept)
        self.platform = platform

    def platform_info(self):
        print(f"Platform: {self.platform}")


class FrontEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, react):
        super().__init__(id, name, dept, platform)
        self.react = react

    def tech_info(self):
        print(f"Tech: {self.react}")


class BackEndDeveloper(Developer):
    def __init__(self, id, name, dept, platform, python):
        super().__init__(id, name, dept, platform)
        self.python = python

    def lang_info(self):
        print(f"Lang: {self.python}")



emp1 = FrontEndDeveloper(1, "Vinnu", "IT", "Android", "React")
emp2 = BackEndDeveloper(2, "hima", "IT", "Android", "Python")

print("**Frontend**")
emp1.show_info()
emp1.platform_info()
emp1.tech_info()
print("**Backend**")
emp2.show_info()
emp2.platform_info()
emp2.lang_info()

#output:
# ID: 1, Name: Vinnu, Dept: IT
# Platform: Android
# Tech: React
# **Backend**
# ID: 2, Name: hima, Dept: IT
# Platform: Android
# Lang: Python