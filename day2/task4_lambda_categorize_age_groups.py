#Categorize Age Groups
age = 35
category = (lambda x: "Junior" if x < 30 else "Mid-level" if x < 45 else "Senior")(age)
print(category)

#sample execution
#Mid-level
