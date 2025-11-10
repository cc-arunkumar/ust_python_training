# TASK: UST Employee Daily Work Report Automation

# TASK 3: Function with arguments and without return

def report(Employee_name,dept_name,efficiency_score):

    if (efficiency_score > 25):
        Performance = "Excellent Performance"

    elif (15<efficiency_score<25):
        Performance = "Good Performance"

    else:
        Performance = "Needs Improvement"

    print(f"Employee : {Employee_name}")
    print(f"Department : {dept_name}")
    print(f"Efficiency : {Performance}")

Employee_name = "Sai Vamsi"
dept_name = "IT"
efficiency_score = 35
report(Employee_name,dept_name,efficiency_score)

# Sample Output
# Employee : Sai Vamsi
# Department : IT
# Efficiency : Excellent Performance
