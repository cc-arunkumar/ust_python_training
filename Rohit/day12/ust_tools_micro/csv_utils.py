import csv   # Import CSV module for reading/writing CSV files

# Function to write data into a CSV file
def write_csv(path: str, data: list[dict[str, str]], headers: list[str]) -> None:
    # Open file in write mode
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        if not data:   # If data is empty, exit early
            return 

        # Create a DictWriter with specified headers
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write all rows (expects list of dictionaries)
        writer.writerows(data)

# Function to read a CSV file and return list of dictionaries
def read_csv(path: str) -> list[dict[str, str]]:
    # """Reads a CSV file and returns a list of dictionaries representing each row.
    # Args:
    #     path (str): The file path to the CSV file.
    with open(path, mode='r', encoding='utf-8') as file:
        # DictReader reads rows into dictionaries using header names as keys
        reader = csv.DictReader(file)

        # Convert reader object into a list of dictionaries
        data = [row for row in reader]

        # Write the data into another CSV file (inventory.csv) with specific headers
        write_csv(
            r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\inventory.csv",
            data,
            headers=['item_id', 'available_stock']
        )

        # Return the data read from the original file
        return data

# Call read_csv on order.csv (this will also trigger writing to inventory.csv)
read_csv(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\data\order.csv")
