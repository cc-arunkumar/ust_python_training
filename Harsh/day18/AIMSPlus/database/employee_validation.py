import csv
import datetime
import re

# -----------------------------
# VALIDATION RULES / MASTER DATA
# -----------------------------
valid_departments = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
valid_locations = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
valid_statuses = {"Active", "Inactive", "Resigned"}

valid_rows = []  # Store only rows that pass validation

# -----------------------------
# READ AND VALIDATE EMPLOYEE DIRECTORY
# -----------------------------
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\employee_directory.csv", 
          newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        errors = []  # Collect validation errors for each row
        try:
            # emp_code must start with USTEMP- followed by digits
            if not re.match(r"^USTEMP-\d+$", row["emp_code"]):
                errors.append("Invalid emp_code")

            # email must follow proper format
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", row["email"]):
                errors.append("Invalid email")

            # phone must be exactly 10 digits
            if not re.match(r"^\d{10}$", row["phone"]):
                errors.append("Invalid phone")

            # department must be one of the valid departments
            if row["department"] not in valid_departments:
                errors.append("Invalid department")

            # location must be one of the valid locations
            if row["location"] not in valid_locations:
                errors.append("Invalid location")

            # join_date must be in YYYY-MM-DD format and not in the future
            try:
                join_date_obj = datetime.datetime.strptime(row["join_date"], "%Y-%m-%d").date()
                if join_date_obj > datetime.date.today():
                    errors.append("Join date cannot be in the future")
            except ValueError:
                errors.append("Invalid join_date format")

            # status must be one of the valid statuses
            if row["status"] not in valid_statuses:
                errors.append("Invalid status")

        except Exception as e:
            # Catch any unexpected errors
            errors.append(str(e))

        # If no errors, add row to valid_rows
        if not errors:
            valid_rows.append(row)

# -----------------------------
# WRITE VALIDATED DATA TO NEW CSV
# -----------------------------
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\validated_employee_directory.csv", 
          "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Validation complete. {len(valid_rows)} valid rows written.")
