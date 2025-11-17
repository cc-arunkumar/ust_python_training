import csv
from models import Book, User, Transaction
from os import path

DATA_PATH = "data/"

class CSVStorage:

    def __init__(self, data_folder="data/"):
        self.data_folder = data_folder

    # Load Books from CSV
    def load_books(self):
        books = []
        try:
            with open(f"{self.data_folder}books.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        row["book_id"],
                        row["title"],
                        row["authors"].split("|"),  # Convert authors back to list
                        row["isbn"],
                        row["tags"].split("|"),  # Convert tags back to list
                        int(row["total_copies"])  # Convert total_copies to integer
                    )
                    # Set available_copies separately
                    book.available_copies = int(row["available_copies"])
                    books.append(book)
        except FileNotFoundError:
            # If file does not exist, create it with headers
            with open(f"{self.data_folder}books.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
                writer.writeheader()
        return books

    # Save Books to CSV
    def save_books(self, books):
        with open(f"{self.data_folder}books.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
            writer.writeheader()
            for book in books:
                writer.writerow({
                    "book_id": book.book_id,
                    "title": book.title,
                    "authors": "|".join(book.authors),  # Convert authors list to a string
                    "isbn": book.isbn,
                    "tags": "|".join(book.tags),  # Convert tags list to a string
                    "total_copies": book.total_copies,
                    "available_copies": book.available_copies
                })

    # Load Users from CSV
    def load_users(self):
        users = []
        try:
            with open(f"{self.data_folder}users.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        user_id=row["user_id"],
                        name=row["name"],
                        email=row["email"],
                        status=row["status"],
                        max_loans=row["max_loans"],
                        password=row["password"]  # Load the password
                    )
                    users.append(user)
        except FileNotFoundError:
            # If file does not exist, return an empty list
            pass
        return users

    # Save Users to CSV
    def save_users(self, users):
        with open(f"{self.data_folder}users.csv", mode="w", newline="") as file:
            fieldnames = ["user_id", "name", "email", "status", "max_loans", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow(user.to_dict())

    # Load Transactions from CSV
    def load_transactions(self):
        transactions = []
        try:
            with open(f"{self.data_folder}transactions.csv", mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transaction = Transaction(
                        row["tx_id"],
                        row["book_id"],
                        row["user_id"],
                        row["borrow_date"],
                        row["due_date"],
                        row["return_date"] if row["return_date"] else None,
                        row["status"]
                    )
                    transactions.append(transaction)
        except FileNotFoundError:
            # If file does not exist, create it with headers
            with open(f"{self.data_folder}transactions.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])
                writer.writeheader()
        return transactions

    # Save Transactions to CSV
    def save_transactions(self, transactions):
        with open(f"{self.data_folder}transactions.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])
            writer.writeheader()
            for transaction in transactions:
                writer.writerow({
                    "tx_id": transaction.tx_id,
                    "book_id": transaction.book_id,
                    "user_id": transaction.user_id,
                    "borrow_date": transaction.borrow_date,
                    "due_date": transaction.due_date,
                    "return_date": transaction.return_date if transaction.return_date else '',
                    "status": transaction.status
                })
