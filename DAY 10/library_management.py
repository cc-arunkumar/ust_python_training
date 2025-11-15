from models import Book, User, Transaction
from storage import CSVStorage

storage = CSVStorage()
books = storage.load_books()
users = storage.load_users()
transactions = storage.load_transactions()
