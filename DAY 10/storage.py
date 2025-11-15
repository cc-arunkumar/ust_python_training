import csv
import os
from models import Book, User, Transaction


class CSVStorage:
    def __init__(self, data_folder='data'):
        self.data_folder = data_folder
        os.makedirs(data_folder, exist_ok=True)



    # -------------------- BOOKS --------------------
    def load_books(self):
        books = []
        path = os.path.join(self.data_folder, 'books.csv')
        if not os.path.exists(path):
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['book_id','title','authors','isbn','tags','total_copies','available_copies'])
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:  # skip empty rows
                    authors = row['authors'].split('|') if row['authors'] else []
                    tags = row['tags'].split('|') if row['tags'] else []
                    book = Book(
                        book_id=row['book_id'],
                        title=row['title'],
                        authors=authors,
                        isbn=row['isbn'],
                        tags=tags,
                        total_copies=int(row['total_copies']),
                        available_copies=int(row['available_copies'])
                    )
                    books.append(book)
        return books

    def save_books(self, books):
        path = os.path.join(self.data_folder, 'books.csv')
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['book_id','title','authors','isbn','tags','total_copies','available_copies'])
            for b in books:
                writer.writerow([
                    b.book_id,
                    b.title,
                    '|'.join(b.authors),
                    b.isbn,
                    '|'.join(b.tags),
                    b.total_copies,
                    b.available_copies
                ])


    # -------------------- USERS --------------------
    def load_users(self):
        # same as load_books but for User
        pass

    def save_users(self, users):
        # same as save_books but for User
        pass


    # -------------------- TRANSACTIONS --------------------
    def load_transactions(self):
        # same as load_books but for Transaction
        pass

    def save_transactions(self, transactions):
        # same as save_books but for Transaction
        pass
