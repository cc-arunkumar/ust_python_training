
import csv 
from src.model.model_asset_inventory import AssetInventory
from src.model.model_employees import Employee
from src.model.model_maintenance_log import MaintenanceLog
from src.model.model_vendor_master import VendorMaster
import os

# ---------------- CSV PROCESSING ----------------
valid_rows = []
error_rows = []

input_file = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\asset_inventory.csv"
clean_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\cleaned_asset_inventory.csv"
error_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\error_data.csv"


if not os.path.exists(input_file):
    print(f" File not found: {input_file}")
else:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                model = AssetInventory(**row)
                valid_rows.append(model.model_dump())
            except Exception as e:
                print("\n ERROR:", row)
                print("   Reason:", e)
                error_rows.append(row)


# ---------------- SAVE RESULTS ----------------
if valid_rows:
    with open(clean_output, "w", newline='') as file:
        csv.DictWriter(file, fieldnames=valid_rows[0].keys()).writeheader()
        csv.DictWriter(file, fieldnames=valid_rows[0].keys()).writerows(valid_rows)
    print(f"\n Cleaned data saved to: {clean_output}")

if error_rows:
    with open(error_output, "w", newline='') as file:
        csv.DictWriter(file, fieldnames=error_rows[0].keys()).writeheader()
        csv.DictWriter(file, fieldnames=error_rows[0].keys()).writerows(error_rows)
    print(f" Errors saved to: {error_output}")

print(f"\nSummary → Processed: {len(valid_rows)+len(error_rows)}, Valid: {len(valid_rows)}, Errors: {len(error_rows)}")


input_file = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\maintenance_log.csv"
clean_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\cleaned_maintenance_log.csv"
error_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\maintenance_log_error_data.csv"

valid_rows = []
error_rows = []


# ---------------------------------------------------------
# CSV Processing Logic
# ---------------------------------------------------------

if not os.path.exists(input_file):
    print(f" ERROR: Input file not found: {input_file}")
else:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                model = MaintenanceLog(**row)
                valid_rows.append(model.model_dump())
            except Exception as e:
                print("\nERROR PROCESSING ROW:", row)
                print("Reason:", e)
                error_rows.append(row)


# ---------------------------------------------------------
# WRITE CLEANED DATA
# ---------------------------------------------------------

if valid_rows:
    with open(clean_output, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(valid_rows)
    print(f"\n✔ Cleaned data saved at: {clean_output}")


# ---------------------------------------------------------
# WRITE ERROR DATA
# ---------------------------------------------------------

if error_rows:
    with open(error_output, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=error_rows[0].keys())
        writer.writeheader()
        writer.writerows(error_rows)
    print(f"Error data saved at: {error_output}")


# # ---------------------------------------------------------
# # SUMMARY OUTPUT
# # ---------------------------------------------------------

# print("\n-------------------------------------------------")
# print(f" Total rows processed: {len(valid_rows) + len(error_rows)}")
# print(f" Valid rows: {len(valid_rows)}")
# print(f" Invalid rows: {len(error_rows)}")
# print("-------------------------------------------------\n")


# ---------------------------------------------------------
# File Paths
# ---------------------------------------------------------
input_file = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\vendor_master.csv"
clean_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\cleaned_vendor_master.csv"
error_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\vendor_master_error_data.csv"

valid_rows = []
error_rows = []


# ---------------------------------------------------------
# Validate CSV Records
# ---------------------------------------------------------

if not os.path.exists(input_file):
    print(f" ERROR: Input file not found: {input_file}")
else:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                model = VendorMaster(**row)
                valid_rows.append(model.model_dump())
            except Exception as e:
                print("\n ERROR PROCESSING ROW:", row)
                print("   Reason:", e)
                error_rows.append(row)


# ---------------------------------------------------------
# Write Cleaned Data to File
# ---------------------------------------------------------

if valid_rows:
    with open(clean_output, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(valid_rows)
    print(f"\nCLEAN DATA SAVED → {clean_output}")


# ---------------------------------------------------------
# Write Error Data to File
# ---------------------------------------------------------

if error_rows:
    with open(error_output, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=error_rows[0].keys())
        writer.writeheader()
        writer.writerows(error_rows)
    print(f" ERROR DATA SAVED → {error_output}")


# ---------------------------------------------------------
# Summary Output
# ---------------------------------------------------------
print("\n----------------------------------------------")
print(f" Total rows processed : {len(valid_rows) + len(error_rows)}")
print(f" Valid rows         : {len(valid_rows)}")
print(f" Invalid rows       : {len(error_rows)}")
print("----------------------------------------------\n")
