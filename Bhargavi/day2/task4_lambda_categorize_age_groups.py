#Categorize Age Groups

age = 60
category = (lambda x: "Junior" if x < 30 else "Mid-level" if x < 45 else "Senior")(age)
print(category)

# Senior
