from crud.csv_to_db import load_assets, load_vendors, load_maintenance

if __name__ == "__main__":
    load_assets()
    load_vendors()
    load_maintenance()
    print("CSV data loaded into MySQL successfully!")
