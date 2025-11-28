import csv
import datetime
import re

valid_departments = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
valid_locations = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
valid_statuses = {"Active", "Inactive", "Resigned"}

valid_rows = []

input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\employee_directory(in).csv"
output_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\valid_employee.csv"

with open(input_file, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    for row in reader:
        errors = []

        # emp_code must start with USTEMP- and 4 digits
        if not re.match(r"^USTEMP-\d{4}$", row["emp_code"]):
            errors.append("Invalid emp_code")

        # email format
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", row["email"]):
            errors.append("Invalid email")

        # phone must be 10 digits
        if not re.match(r"^\d{10}$", row["phone"]):
            errors.append("Invalid phone")

        # department check
        if row["department"] not in valid_departments:
            errors.append("Invalid department")

        # location check
        if row["location"] not in valid_locations:
            errors.append("Invalid location")

        if not row["join_date"]:
            errors.append("Missing join_date")
        # status check
        if row["status"] not in valid_statuses:
            errors.append("Invalid status")

        if errors:
            print(f"Row {row.get('emp_code','?')} errors: {errors}")
        else:
            valid_rows.append(row)

# Write valid rows to new CSV
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Validation complete. {len(valid_rows)} valid rows written.")