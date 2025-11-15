# ��Update Employee Salary
# Text File Task 3
# Ask for Employee ID and new salary.
# Read all lines, modify the correct line, and rewrite the file with the updated
# data.
# Example:
# Enter Employee ID: E104
# Enter New Salary: 65000
# Result:
# E104,Fatima Khan,HR,65000,2018-12-05

def update():
    # Ask user for Employee ID and new salary
    emp_id = input("Enter Employee ID to update salary: ").strip()
    sal = input("Enter New Salary: ").strip()

    updated_lines = []   # To store modified employee records
    updated = False      # Flag to check if update happened

    # Open the file in read mode
    with open("employees.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            
            # If Employee ID matches, update salary
            if fields[0].strip() == emp_id:
                fields[3] = sal   # Update salary field
                updated = True
                # Show updated details
                print("\n Employee Updated:")
                print(f"ID: {fields[0]}")
                print(f"Name: {fields[1]}")
                print(f"Department: {fields[2]}")
                print(f"Salary: {fields[3]}")
                print(f"Date of Joining: {fields[4]}")
            
            # Rebuild the line (updated or unchanged) and add to list
            updated_lines.append(",".join(fields) + "\n")

    # If update happened, rewrite the file with updated records
    if updated:
        with open("employees.txt", "w") as file:
            file.writelines(updated_lines)
        print(f"\n Salary updated successfully for Employee ID {emp_id}.")
    else:
        print("\n Employee not found.")

           
            
                
  