names=["Arun","Neha","Vikram"]
depts=["HR","IT","Finance"]
result = list(map(lambda n,d : f"{n} works in {d}",names,depts))
print(result)