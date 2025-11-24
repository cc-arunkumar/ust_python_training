import csv

# Function to read a CSV file and return its contents as a list of dictionaries.
# Each dictionary represents a row in the CSV file, with column headers as keys.
# Arguments:
# path: The file path to the CSV file that needs to be read.
# Returns:
# A list of dictionaries where each dictionary represents a row in the CSV file.
def read_csv(path: str) -> list[dict[str, str]]:
    # Open the CSV file in read mode
    with open(path, mode='r', newline='') as f:
        # Initialize a CSV DictReader which will parse the CSV and convert each row into a dictionary
        reader = csv.DictReader(f)
        
        # Return a list of all rows as dictionaries
        return [row for row in reader]

# Function to write data to a CSV file from a list of dictionaries.
# Arguments:
# path: The file path to the CSV file where data needs to be written.
# rows: A list of dictionaries where each dictionary represents a row to write to the CSV.
# headers: A list of column headers for the CSV file.
# Returns:
# None. The function directly writes the rows to the specified file.
def write_csv(path: str, rows: list[dict[str, str]], headers: list[str]) -> None:
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        if not rows:
            return
        
        # Initialize a CSV DictWriter which will write dictionaries to the CSV file
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the header row to the CSV
        writer.writeheader()
        
        # Write the actual data rows to the CSV
        writer.writerows(rows)
