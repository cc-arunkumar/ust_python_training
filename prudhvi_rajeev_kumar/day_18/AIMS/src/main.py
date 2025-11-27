from crud.csv_to_db import load_csv_to_db, load_vendors, load_maintenance,load_employees

if __name__ == "__main__":
    load_csv_to_db()
    load_vendors()
    load_maintenance()
    print("CSV data loaded into MySQL successfully!")
