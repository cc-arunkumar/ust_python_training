# =====Task: UST Employee DailyWork Report Automation====
# Function without arguments and without return
def  Welcome():
    print("Welcome to UST Employee Work Report System")
    print("This program helps HR calculate employee performance easily")

# Function with arguments and with return
def efficiencystore(hours,tasks):
    return (tasks/ hours)* 10

# Function with arguments and without return
def report(Emp,Dept,Effy ):
    print(f"Employee Name:{Emp} | Department Name:{Dept} | Efficiency :{Effy}")
    if(Effy>25):
        print("Excellent performance.")
    elif(Effy>=15 and Effy<=25):
        print("Good performance.")
    else:
        print("Needs improvement.")



# Function without arguments but with return
def Info():
    active="Current Active Project: UST Cloud Migration"
    return active

# Function with variable arguments ( args )
def avgEffy(*scores):
    leng=len(scores)
    sum=0
    for i in scores:
        sum+=i
    avgres=sum/leng
    if(avgres>25):
        print("Team performed above expectations.")
    else:
        print("Team needs improvement.")
    




Welcome()
res=efficiencystore(25,10)
report("Asha","Finance",res)
ans=efficiencystore(37,78)
report("Rahul","IT",ans)
ans2=efficiencystore(34,56)
report("Sneha","HR",ans2)
Info()
avgEffy(res,ans,ans2)


# ////SAMPLE EXECUTION/////////
# Welcome to UST Employee Work Report System
# This program helps HR calculate employee performance easily
# Employee Name:Asha | Department Name:Finance | Efficiency :4.0
# Needs improvement.
# Employee Name:Rahul | Department Name:IT | Efficiency :21.08108108108108
# Good performance.
# Employee Name:Sneha | Department Name:HR | Efficiency :16.470588235294116
# Good performance.
# Team needs improvement.

