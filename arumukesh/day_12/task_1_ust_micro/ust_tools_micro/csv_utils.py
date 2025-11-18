import csv

def read_csv(path: str) -> list[dict[str, str]]:
    """
    Read a CSV file and return a list of dictionary rows.
    """
    with open(path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(path: str, rows: list[dict[str, str]], headers: list[str]) -> None:
    """
    Overwrite CSV file with given headers and rows.
    """
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
