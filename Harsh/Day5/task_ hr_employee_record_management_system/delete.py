# Delete Employee Record
# Ask for Employee ID to delete.
# Read all lines, remove the matching record, and rewrite the file.
# Text File Task 4
# Confirm deletion to the user.
# Example:
# Enter Employee ID to delete: E105
# Employee deleted successfully!


def delete():
    # Ask the user to enter the Employee ID to delete
    emp_id = input("Enter Employee ID to delete: ").strip()
    
    # Flag to track whether the employee was found and deleted
    deleted = False
    
    # List to store updated employee records (after deletion)
    updated_lines = []

    # Open the employees.txt file in read mode
    with open("employees.txt", "r") as file:
        for line in file:
            # Split each line by comma to get individual fields
            fields = line.strip().split(",")
            
            # If the Employee ID does not match, keep the record
            if not fields[0].strip() == emp_id:
                updated_lines.append(line)
            else:
                # If Employee ID matches, mark as deleted
                deleted = True

    # If the employee was found and deleted
    if deleted:
        # Rewrite the file with updated records (excluding deleted employee)
        with open("employees.txt", "w") as file:
            file.writelines(updated_lines)
        print(f"Employee ID {emp_id} deleted successfully.")
    else:
        # If no matching Employee ID was found
        print(" Employee not found.")


