
def search():
    emp_id=input("Enter the id:")
    found = False
    with open("employees.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if fields[0].strip() == emp_id:
                print("\n Employee Found:")
                print(f"ID: {fields[0]}")
                print(f"Name: {fields[1]}")
                print(f"Department: {fields[2]}")
                print(f"Salary: {fields[3]}")
                print(f"Date of Joining: {fields[4]}")
                found = True
                break
    if not found:
        print(" Employee not found.")
        



