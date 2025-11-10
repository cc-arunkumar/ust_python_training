#Task : Combine two list employee and dept

#Code 
name = eval(input("Enter the name : "))
dept = eval(input("Enter the dept name : "))
combine = list(map(lambda n,d:f"{n} works in {d}",name,dept))
print(combine)

#Output
# Enter the name : ["Sohan","sanu"]
# Enter the dept name : ["IT","CSE"]
# ['Sohan works in IT', 'sanu works in CSE']