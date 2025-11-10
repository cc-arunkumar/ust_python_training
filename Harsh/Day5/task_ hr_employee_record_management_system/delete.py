def delete():
    emp_id = input("Enter Employee ID to delete: ").strip()
    deleted = False
    updated_lines = []

    with open("employees.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if not fields[0].strip() == emp_id:
                updated_lines.append(line)
            else:
                deleted = True

    if deleted:
        with open("employees.txt", "w") as file:
            file.writelines(updated_lines)
        print(f"Employee ID {emp_id} deleted successfully.")
    else:
        print(" Employee not found.")

