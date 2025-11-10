# Task: UST Employee DailyWork Report
# Automation

# Part 1: Function without arguments and without return

# def greet():
#     print("Welcome to UST Employee Work Report System.\n")
#     print("This program helps HR calculate employee performance easily.")
# greet()

# Part 2: Function with arguments and with return

def efficiency_score(hours,task):
    efficiency = (task/hours)*10
    return efficiency

tot_hours = int(input("Enter tot hours:"))
tot_task = int(input("Enter tot task:"))
res = efficiency_score(tot_hours,tot_task)
print(res)

# Part 3: Function with arguments and without return

emp_name = input("Enter Employee Name:")
dep_name = input("Enter dep name:")
score = res 
def calculate_effi(name,dep,scoree):
    if(scoree>25):
        print("employee name:{name},employee dep:{dep},employee status:excellent")
calculate_effi(emp_name,dep_name,score)