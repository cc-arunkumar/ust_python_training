#Constructor Chaining

class Emp:

    def __init__(self,id,name,dep):
        self.id = id
        self.name = name
        self.dep = dep

class Dev(Emp):

    def __init__(self, id, name, dep, platform):
        super().__init__(id, name, dep)
        self.platform = platform

class Frontend(Dev):

    def __init__(self, id, name, dep, platform, tech):
        super().__init__(id, name, dep, platform)
        self.tech = tech

class Backend(Dev):

    def __init__(self, id, name, dep, platform, language):
        super().__init__(id, name, dep, platform)
        self.language = language

f1 = Frontend(101,"Arjun","IT","Web","React")
b1 = Backend(101,"Arjun","IT","Web","Python")
print("Framework :",f1.tech)
print("Language :",b1.language)

#Output
# Framework : React
# Language : Python