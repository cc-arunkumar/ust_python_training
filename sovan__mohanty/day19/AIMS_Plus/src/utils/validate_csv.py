import csv
from fastapi import HTTPException
from typing import List

def validate_csv(file_path: str, required_columns: List[str]) -> List[dict]:
    """
    Validate that a CSV file contains the required columns and return its rows.

    Args:
        file_path (str): Path to the CSV file.
        required_columns (List[str]): List of required column names.

    Returns:
        List[dict]: List of rows as dictionaries.

    Raises:
        HTTPException: If required columns are missing.
    """
    try:
        with open(file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            # Check required columns
            if not set(required_columns).issubset(reader.fieldnames):
                raise HTTPException(
                    status_code=422,
                    detail=f"CSV missing required columns. Expected {required_columns}, found {reader.fieldnames}"
                )
            # Return rows as list of dicts
            return [row for row in reader]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"CSV file not found: {file_path}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading CSV: {str(e)}")
