# Importing the necessary CRUD functions from the asset_crud module
from crud.asset_crud import create_asset, read_all_assets, read_asset_by_id, update_asset, delete_asset

# Demo script to call CRUD functions and display log messages
def main():
    try:
        # Create a new asset
        print("Creating a new asset...")
        result = create_asset(
            asset_tag="UST-LTP-1001",  # Unique asset tag
            asset_type="Laptop",  # Type of the asset (Laptop)
            serial_number="SN-ABC12345",  # Unique serial number
            manufacturer="HP",  # Manufacturer of the asset
            model="HP EliteBook 850",  # Model name
            purchase_date="2023-06-15",  # Purchase date
            warranty_years=3,  # Warranty duration in years
            assigned_to=None,  # Initially, no user assigned
            asset_status="Available"  # Initial status of the asset (Available)
        )
        # Display the result of creating the asset
        print(f"Create Asset Result: {result}")

        # Read all assets from the database
        print("\nReading all assets...")
        read_all_assets()  # Function to read and display all assets

        # Read a single asset by ID (example with asset_id = 1)
        print("\nReading asset with ID 1...")
        read_asset_by_id(1)  # Function to fetch asset details by ID

        # Update an asset (example with asset_id = 1)
        print("\nUpdating asset with ID 1...")
        result = update_asset(
            asset_id=1,  # Asset ID to update
            asset_type="Laptop",  # Updated asset type
            manufacturer="Dell",  # Updated manufacturer
            model="Dell XPS 15",  # Updated model
            warranty_years=4,  # Updated warranty years
            asset_status="Assigned",  # Updated asset status (Assigned)
            assigned_to="John Doe (UST Bangalore)"  # Updated user assignment
        )
        # Display the result of the update operation
        print(f"Update Asset Result: {result}")

        # Delete an asset (example with asset_id = 2)
        print("\nDeleting asset with ID 2...")
        result = delete_asset(2)  # Function to delete an asset by ID
        # Display the result of the delete operation
        print(f"Delete Asset Result: {result}")

    except Exception as e:
        # Handling any exceptions that occur during the operations
        print(f"An error occurred: {e}")

# Entry point for the script when executed
if __name__ == "__main__":
    main()
    
    
    
# Sample Output:
#     Attempting to connect to the database...
# Connection established successfully.
# Creating a new asset...
# Attempting to connect to the database...
# Connection established successfully.
# Create Asset Result: ❌ Error: Asset tag or serial number already exists.

# Reading all assets...
# Attempting to connect to the database...
# Connection established successfully.
# 📑 Asset ID: 1, Tag: UST-LTP-1001, Type: Laptop, Serial: SN-ABC12345, Manufacturer: Dell, Model: Dell XPS 15, Status: John Doe (UST Bangalore)  
# 📑 Asset ID: 3, Tag: UST-MNT-0002, Type: Monitor, Serial: SN-LG-7719231, Manufacturer: LG, Model: UltraWide 29WL500, Status: None
# 📑 Asset ID: 4, Tag: UST-KEY-0003, Type: Keyboard, Serial: SN-HP-6612321, Manufacturer: HP, Model: HP Wired 160, Status: None
# 📑 Asset ID: 5, Tag: UST-LTP-0004, Type: Laptop, Serial: SN-LN-1234987, Manufacturer: Lenovo, Model: ThinkPad E15, Status: Rohit Sharma (UST Bangalore)
# 📑 Asset ID: 6, Tag: UST-DCK-0005, Type: Docking Station, Serial: SN-DL-5543123, Manufacturer: Dell, Model: Dell D6000, Status: Anjali Nair (UST Trivandrum)
# 📑 Asset ID: 7, Tag: UST-MNT-0006, Type: Monitor, Serial: SN-SAM-9834567, Manufacturer: Samsung, Model: Samsung S24R350, Status: Vivek Reddy (UST Hyderabad)
# 📑 Asset ID: 8, Tag: UST-LTP-0007, Type: Laptop, Serial: SN-HP-8834129, Manufacturer: HP, Model: HP ProBook 440 G8, Status: None
# 📑 Asset ID: 9, Tag: UST-MNT-0008, Type: Monitor, Serial: SN-LG-9925511, Manufacturer: LG, Model: LG 24MK600, Status: None

# Reading asset with ID 1...
# Attempting to connect to the database...
# Connection established successfully.
# 📑 Asset ID: 1, Tag: UST-LTP-1001, Type: Laptop, Serial: SN-ABC12345, Manufacturer: Dell, Model: Dell XPS 15, Status: John Doe (UST Bangalore)

# Updating asset with ID 1...
# Attempting to connect to the database...
# Connection established successfully.
# Update Asset Result: 🎉 Asset updated successfully.

# Deleting asset with ID 2...
# Attempting to connect to the database...
# Connection established successfully.
# Delete Asset Result: ❗ Asset not found.    
    