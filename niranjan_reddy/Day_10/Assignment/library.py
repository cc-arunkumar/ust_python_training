from datetime import datetime, timedelta

from models import Book, User, Transaction

from storage import CSVStorage
 
from models import (

    InvalidBookError,

    InvalidUserError,

    BookNotAvailableError,

    UserNotAllowedError,

    TransactionError,

    ValidationError

)
 
def today():

    return datetime.today().strftime("%d-%m-%Y")
 
def add_days(date_str, days):

    base_date = datetime.strptime(date_str, "%d-%m-%Y")

    new_date = base_date + timedelta(days=days)

    return new_date.strftime("%d-%m-%Y")
 
class Library:
 
    def __init__(self, storage=None):

        self.books = []

        self.users = []

        self.transactions = []
 
        if storage:

            self.storage = storage

        else:

            self.storage = CSVStorage(

                books_path="books.csv",

                users_path="users.csv",

                transactions_path="transactions.csv"

            )
 
        self.books = self.storage.load_books()

        self.users = self.storage.load_users()

        self.transactions = self.storage.load_transactions()
 
    def add_book(self, book_id, title, authors, tags, isbn, total_copies):

        if self.get_book(book_id):

            raise InvalidBookError("Book ID already exists.")
 
        for b in self.books:

            if b.isbn == isbn:

                raise ValidationError("ISBN already exists.")
 
        book_object = Book(

            book_id=book_id,

            title=title,

            authors=authors,

            tags=tags,

            isbn=isbn,

            total_copies=total_copies,

            available_copies=total_copies

        )
 
        self.books.append(book_object)
 
    def update_book(self, book_id, **kwargs):

        book = self.get_book(book_id)

        if not book:

            raise InvalidBookError("Book not found.")

        book.update(**kwargs)
 
    def remove_book(self, book_id):

        book = self.get_book(book_id)

        if not book:

            raise InvalidBookError("Book not found.")

        for tx in self.transactions:

            if tx.book_id == book_id and tx.status == "borrowed":

                raise InvalidBookError("Book is currently borrowed.")

        self.books.remove(book)
 
    def get_book(self, book_id):

        for b in self.books:

            if b.book_id == book_id:

                return b

        return None
 
    def list_books(self):

        return self.books
 
    def search_books_by_title(self, title_substring):

        s = title_substring.lower()

        return [b for b in self.books if s in b.title.lower()]
 
    def search_books_by_author(self, author_name):

        s = author_name.lower()

        return [b for b in self.books if s in [a.lower() for a in b.authors]]
 
    def search_books_by_tag(self, tag_name):

        s = tag_name.lower()

        return [b for b in self.books if s in [t.lower() for t in b.tags]]
 
    def add_user(self, user_object):

        if self.get_user(user_object.user_id):

            raise InvalidUserError("User ID already exists.")

        self.users.append(user_object)
 
    def update_user(self, user_id, **kwargs):

        user = self.get_user(user_id)

        if not user:

            raise InvalidUserError("User not found.")

        user.update(**kwargs)
 
    def get_user(self, user_id):

        for u in self.users:

            if u.user_id == user_id:

                return u

        return None
 
    def list_users(self):

        return self.users
 
    def activate_user(self, user_id):

        user = self.get_user(user_id)

        if not user:

            raise InvalidUserError("User not found.")

        user.activate()
 
    def deactivate_user(self, user_id):

        user = self.get_user(user_id)

        if not user:

            raise InvalidUserError("User not found.")

        user.deactivate()
 
    def ban_user(self, user_id):

        user = self.get_user(user_id)

        if not user:

            raise InvalidUserError("User not found.")

        user.ban()
 
    def borrow_book(self, user_id, book_id):

        user = self.get_user(user_id)

        if not user:

            raise InvalidUserError("User does not exist.")
 
        book = self.get_book(book_id)

        if not book:

            raise InvalidBookError("Book does not exist.")
 
        if user.status != "active":

            raise UserNotAllowedError("User is not allowed to borrow.")
 
        if not book.is_available():

            raise BookNotAvailableError("Book is not available.")
 
        active_loans = [tx for tx in self.transactions if tx.user_id == user_id and tx.status == "borrowed"]

        if len(active_loans) >= user.max_loans:

            raise UserNotAllowedError("User reached maximum loan limit.")
 
        tx_id = f"T{len(self.transactions) + 1}"

        borrow_date = today()

        due_date = add_days(borrow_date, 14)
 
        transaction = Transaction(

            tx_id, book_id, user_id, borrow_date, due_date, None, "borrowed"

        )
 
        book.decrease_copies(1)

        self.transactions.append(transaction)

        return transaction
 
    def return_book(self, transaction_id):

        tx = next((t for t in self.transactions if t.tx_id == transaction_id), None)

        if not tx:

            raise TransactionError("Transaction not found.")
 
        if tx.status != "borrowed":

            raise TransactionError("Book already returned.")
 
        book = self.get_book(tx.book_id)

        book.increase_copies(1)
 
        tx.mark_returned(today())
 
    def get_active_loans(self):

        return [tx for tx in self.transactions if tx.status == "borrowed"]
 
    def get_overdue_loans(self, today_date):

        return [tx for tx in self.transactions if tx.is_overdue(today_date)]
 
    def get_user_loans(self, user_id):

        return [tx for tx in self.transactions if tx.user_id == user_id]
 
    def summary_report(self):

        total_books = len(self.books)

        total_users = len(self.users)

        active_loans = len(self.get_active_loans())

        overdue_loans = len(self.get_overdue_loans(today()))

        return total_books, total_users, active_loans, overdue_loans
 
    def save_all(self):

        self.storage.save_books(self.books)

        self.storage.save_users(self.users)

        self.storage.save_transactions(self.transactions)

        return "All data saved successfully."
 
    def help_menu(self):

        return """

Available Commands:

BOOK COMMANDS:

  book add

  book update <book_id>

  book remove <book_id>

  book get <book_id>

  book list

  book search title <text>

  book search author <text>

  book search tag <tag>

USER COMMANDS:

  user add

  user update <user_id>

  user get <user_id>

  user list

  user deactivate <user_id>

  user activate <user_id>

  user ban <user_id>

BORROW / RETURN:

  borrow <user_id> <book_id>

  return <transaction_id>

REPORTS:

  loans active

  loans overdue

  loans user <user_id>

  report summary

  report user <user_id>

UTILITY:

  save

  help

  exit

"""
 
    def exit_system(self):

        return "EXIT"

 