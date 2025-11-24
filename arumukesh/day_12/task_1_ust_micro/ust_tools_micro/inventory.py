from csv import DictReader

class Inventory:
    def __init__(self, items: dict[str, int]):
        """
        Initialize the Inventory object with a dictionary of items.
        
        :param items: A dictionary where keys are item_ids (str) and values are the available stock (int).
        """
        self.items = items

    @classmethod
    def from_csv(cls, path: str):
        """
        Class method to load inventory data from a CSV file.

        The CSV file is expected to have two columns: 'item_id' and 'available_stock'.

        :param path: The file path to the CSV file.
        :return: An instance of the Inventory class initialized with the data from the CSV file.
        """
        items = {}

        with open(path, "r") as file:
            reader = DictReader(file)  # Read the CSV as a dictionary (header row is automatically used as keys)
            for row in reader:
                # For each row in the CSV, store item_id as the key and available_stock as the value.
                items[row["item_id"]] = int(row["available_stock"])

        return cls(items)  # Return an instance of Inventory with the loaded items

    def allocate(self, item_id: str, qty: int) -> bool:
        """
        Allocate a certain quantity of an item from the inventory, if there is enough stock.

        :param item_id: The ID of the item to allocate.
        :param qty: The quantity of the item to allocate.
        :return: True if allocation was successful (enough stock available), False otherwise.
        """
        if item_id in self.items and self.items[item_id] >= qty:
            self.items[item_id] -= qty  # Subtract the allocated quantity from available stock
            return True
        return False  # Return False if item_id doesn't exist or there isn't enough stock

    def release(self, item_id: str, qty: int) -> None:
        """
        Release (return) a certain quantity of an item back to the inventory.

        :param item_id: The ID of the item to release.
        :param qty: The quantity of the item to release.
        """
        if item_id in self.items:
            self.items[item_id] += qty  # Add the released quantity back to the available stock

