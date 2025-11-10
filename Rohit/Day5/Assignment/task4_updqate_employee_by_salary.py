import os

e_id = "E101"
e_salary = 65000
flag = False  # Initialize flag

if os.path.exists("employee.txt"):
    with open("employee.txt", "r") as file:
        lines = file.readlines()

    with open("employee.txt", "w") as file:
        for line in lines:
            tokens = line.strip().split(",")
            employee_id = tokens[0]
            if employee_id == e_id:
                tokens[4] = str(e_salary)  # Convert to string before joining
                rebuilt_string = ",".join(tokens)
                file.write(rebuilt_string + "\n")
                print("Updated:", rebuilt_string)
                flag = True
            else:
                file.write(line)

    if not flag:
        print("Employee not found")
else:
    print("File not found")
