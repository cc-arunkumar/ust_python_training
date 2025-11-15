# storage.py
import csv
from models import Book, User, Transaction
from os import path

DATA_PATH = "data/"

class CSVStorage:

    def load_books(self):
        books = []
        try:
            with open(f"{DATA_PATH}books.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Create Book object
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
            with open(f"{DATA_PATH}books.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
                writer.writeheader()
        return books

    def save_books(self, books):
        with open(f"{DATA_PATH}books.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["book_id", "title", "authors", "isbn", "tags", "total_copies", "available_copies"])
            writer.writeheader()
            for book in books:
                # Write each book as a row in the CSV
                writer.writerow({
                    "book_id": book.book_id,
                    "title": book.title,
                    "authors": "|".join(book.authors),  # Convert authors list to a string
                    "isbn": book.isbn,
                    "tags": "|".join(book.tags),  # Convert tags list to a string
                    "total_copies": book.total_copies,
                    "available_copies": book.available_copies
                })

    def load_users(self):
        users = []
        try:
            with open(f"{DATA_PATH}users.csv", mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        row["user_id"],
                        row["name"],
                        row["email"],
                        row["status"],
                        int(row["max_loans"])  # Convert max_loans to integer
                    )
                    users.append(user)
        except FileNotFoundError:
            # If file does not exist, create it with headers
            with open(f"{DATA_PATH}users.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["user_id", "name", "email", "status", "max_loans"])
                writer.writeheader()
        return users

    def save_users(self, users):
        with open(f"{DATA_PATH}users.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["user_id", "name", "email", "status", "max_loans"])
            writer.writeheader()
            for user in users:
                writer.writerow({
                    "user_id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "status": user.status,
                    "max_loans": user.max_loans
                })

    def load_transactions(self):
        transactions = []
        try:
            with open(f"{DATA_PATH}transactions.csv", mode="r") as file:
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
            with open(f"{DATA_PATH}transactions.csv", mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["tx_id", "book_id", "user_id", "borrow_date", "due_date", "return_date", "status"])
                writer.writeheader()
        return transactions

    def save_transactions(self, transactions):
        with open(f"{DATA_PATH}transactions.csv", mode="w", newline="") as file:
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
