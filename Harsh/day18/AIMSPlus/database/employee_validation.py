import csv
import datetime
import re

valid_departments = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
valid_locations = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
valid_statuses = {"Active", "Inactive", "Resigned"}

valid_rows = []

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\employee_directory.csv", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        errors = []
        try:
            # emp_code must start with USTEMP-
            if not re.match(r"^USTEMP-\d+$", row["emp_code"]):
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

            # join_date must be valid and not future
            try:
                join_date_obj = datetime.datetime.strptime(row["join_date"], "%Y-%m-%d").date()
                if join_date_obj > datetime.date.today():
                    errors.append("Join date cannot be in the future")
            except ValueError:
                errors.append("Invalid join_date format")

            # status check
            if row["status"] not in valid_statuses:
                errors.append("Invalid status")

        except Exception as e:
            errors.append(str(e))

        if not errors:
            valid_rows.append(row)

# Write valid rows to a new CSV
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_employee_directory.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Validation complete. {len(valid_rows)} valid rows written.")
