dect={"key":"values"}
employee = {"E101":"arjun","E102":"neha","E103":"ravi"}
employee["E104"] = "priya"
employee["E105"] = "vikram"
print(employee)
employee["E103"]="ravi kumar"
print("after updating name:",employee)
del employee ["E102"]
print("after deleting E102:",employee)
print("total no. of employees",len(employee))

for employee_id,name in employee.items():
    print(f"employee id:{employee_id}-> Name:{name}")

print(employee.get("E10","employees not found"))


# output
# {'E101': 'arjun', 'E102': 'neha', 'E103': 'ravi', 'E104': 'priya', 'E105': 'vikram'}
# after updating name: {'E101': 'arjun', 'E102': 'neha', 'E103': 'ravi kumar', 'E104': 'priya', 'E105': 'vikram'}
# after deleting E102: {'E101': 'arjun', 'E103': 'ravi kumar', 'E104': 'priya', 'E105': 'vikram'}
# total no. of employees 4
# employee id:E101-> Name:arjun
# employee id:E103-> Name:ravi kumar
# employee id:E104-> Name:priya
# employee id:E105-> Name:vikram
# employees not found




