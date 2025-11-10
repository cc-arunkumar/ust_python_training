import os

print("Enter employee details: ID, NAME, DESIGNATION, SALARY, STARTING DATE")


# employee_id = input("Enter the ID: ")
# employee_name = input("Enter the Name: ")
# employee_designation = input("Enter the Designation: ")
# employee_salary = input("Enter the Salary: ")
# employee_date = input("Enter the Starting Date (YYYY-MM-DD): ")


# field = f"{employee_id},{employee_name},{employee_designation},{employee_salary},{employee_date}\n"

with open("employee.txt", "a") as file:
    file.write("E105,Vikram Singh,Operations,58000,2022-01-11\n")


validate = set()
if os.path.exists("employee.txt"):
    with open("employee.txt", "r") as file:
        for line in file:
            tokens = line.strip().split(",")
            if len(tokens) < 1:
                continue
            employee_id = tokens[0].strip()
            if employee_id not in validate:
                validate.add(employee_id)
            else:
                print(f"Duplicate found: {line.strip()} (ID: {employee_id})")
else:
    print("file not found")

print("\nValidation complete.")



# ==============sample output================
# Enter employee details: ID, NAME, DESIGNATION, SALARY, STARTING DATE
# Duplicate found: E105,Vikram Singh,Operations,58000,2022-01-11 (ID: E105)

# Validation complete.