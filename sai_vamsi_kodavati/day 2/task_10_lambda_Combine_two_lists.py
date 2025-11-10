# TASK 5 - Combine Two Lists

names = ["Rahul","Sai Vamsi","Arjun"]
dept = ["HR","IT","Finance"]

merge = list(map(lambda a,b : a + " works in " + b,names,dept))
print(merge)

# Sample Output
# ['Rahul works in HR', 'Sai Vamsi works in IT', 'Arjun works in Finance']