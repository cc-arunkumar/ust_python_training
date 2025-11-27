import csv
import pymysql
import datetime

# --- Simple validators ---
def validate_date(date_str):
    """Check if date is in YYYY-MM-DD format and valid."""
    try:
        datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_email(email_str):
    """Check if email contains '@' and ends with ust.com."""
    return email_str and "@" in email_str and email_str.strip().endswith("ust.com")

# --- DB connection ---
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_asset_db"
)

cursor = conn.cursor()

# --- SQL insert ---
query = """
INSERT INTO employee_master (
    emp_code, full_name, email, phone, department, location, join_date, status
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
)
"""

path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\employee_directory.csv"
# --- Load CSV ---
with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    success, fail = 0, 0

    for row in reader:
        # Validate join_date
        if not validate_date(row["join_date"]):
            print(f"Skipping invalid date: {row['join_date']} for row {row}")
            fail += 1
            continue

        # Validate email
        if not validate_email(row["email"]):
            print(f"Skipping invalid email: {row['email']} for row {row}")
            fail += 1
            continue

        # Prepare values
        data = (
            row["emp_code"],
            row["full_name"],
            row["email"],
            row["phone"],
            row["department"],
            row["location"],
            row["join_date"],
            row["status"]
        )

        try:
            cursor.execute(query, data)
            success += 1
        except Exception as e:
            print(f"Skipping row due to DB error: {row}\nError: {e}")
            fail += 1

# --- Commit & close ---
conn.commit()
cursor.close()
conn.close()

print(f"Inserted {success} rows, skipped {fail} rows.")
