#Part 1: Function without arguments and without return
def noargsnoreturn():
    print("Welcome to UST Employee Work Report System")
    print("This program helps HR calculate employee performance easily.")

#Part 2: Function with arguments and with return
def argsandreturn(hours,completed):
    efficiency=(completed/hours)*10
    return efficiency

# Part3: Function with arguments and without return
def argsandnoreturn(name,department,efficiency):
    print("Employee: ",name,end="|")
    print("Department: ",department,end="|")
    print("Efficiency: ",efficiency)
    if(efficiency>25):
        print("Excellent performance.")
    elif(efficiency>=15):
        print("Good performance.")
    else:
        print("Needs improvement.")

#Part 4: Function without arguments but with return
def noargsandreturn():
    return "UST Cloud Migration"

#Part 5: Function with variable arguments ( args )
def variableargs(*efficiency):
    length=len(efficiency)
    sum=0
    for e in efficiency:
        sum=sum+e
    sum=sum/length
    print("Average Team Efficiency: ",sum)
    if(sum>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")



noargsnoreturn()
print()
print(noargsandreturn())
print()
eff1=argsandreturn(90,190)
argsandnoreturn("shyam","Finance",eff1)
print()
eff2=argsandreturn(80,100)
argsandnoreturn("Rahul","IT",eff2)
print()
eff3=argsandreturn(60,120)
argsandnoreturn("Sneha","HR",eff3)
print()
variableargs(eff1,eff2,eff3)


#Sample output
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily.

# UST Cloud Migration

# Employee:  shyam|Department:  Finance|Efficiency:  21.11111111111111
# Good performance.

# Employee:  Rahul|Department:  IT|Efficiency:  12.5
# Needs improvement.

# Employee:  Sneha|Department:  HR|Efficiency:  20.0
# Good performance.

# Average Team Efficiency:  17.87037037037037
# Team needs improvement.