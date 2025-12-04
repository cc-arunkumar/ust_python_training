
from storage import CSVStorage
from models import Book, Transaction, User
from utils import today_str, add_days, parse_comma_list, make_tx_id

storage = CSVStorage()

def add_book():
    try:
        book_id = input("Book ID: ").strip()
        title = input("Title: ").strip()
        authors = parse_comma_list(input("Authors (comma separated): "))
        isbn = input("ISBN: ").strip()
        tags = parse_comma_list(input("Tags (comma separated): "))
        total_copies = int(input("Total Copies: ").strip())

        books = storage.load_books()
        if any(b.book_id == book_id for b in books):
            print("Book ID already exists.")
            return

        book = Book(book_id, title, authors, isbn, tags, total_copies)
        books.append(book)
        storage.save_books(books)
        print(f"Book '{book.title}' added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def soft_delete_book():
    book_id = input("Book ID to delete (soft): ").strip()
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    if not book:
        print("Book not found.")
        return
    if book.is_deleted:
        print("Book already soft-deleted.")
        return
    book.is_deleted = True
    storage.save_books(books)
    print(f"Book '{book.title}' soft-deleted.")

def restore_book():
    book_id = input("Book ID to restore: ").strip()
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    if not book:
        print("Book not found.")
        return
    if not book.is_deleted:
        print("Book is not deleted.")
        return
    book.is_deleted = False
    storage.save_books(books)
    print(f"Book '{book.title}' restored.")

def update_book():
    book_id = input("Book ID to update: ").strip()
    books = storage.load_books()
    book = next((b for b in books if b.book_id == book_id), None)
    if not book:
        print("Book not found.")
        return

    print("Current details:")
    print(f"- Title: {book.title}")
    print(f"- Authors: {', '.join(book.authors)}")
    print(f"- ISBN: {book.isbn}")
    print(f"- Tags: {', '.join(book.tags)}")
    print(f"- Total Copies: {book.total_copies}")
    print(f"- Available Copies: {book.available_copies}")
    print(f"- Deleted: {book.is_deleted}")

    title = input("New Title (leave blank to keep): ").strip()
    authors_input = input("New Authors (comma separated, leave blank to keep): ").strip()
    isbn = input("New ISBN (leave blank to keep): ").strip()
    tags_input = input("New Tags (comma separated, leave blank to keep): ").strip()
    total_copies_input = input("New Total Copies (leave blank to keep): ").strip()

    if title:
        book.title = title
    if authors_input:
        book.authors = parse_comma_list(authors_input)
    if isbn:
        book.isbn = isbn
    if tags_input:
        book.tags = parse_comma_list(tags_input)
    if total_copies_input:
        try:
            new_total = int(total_copies_input)
            borrowed_count = book.total_copies - book.available_copies
            if new_total < borrowed_count:
                print("Total copies cannot be less than currently borrowed copies.")
                return
            book.total_copies = new_total
            book.available_copies = max(0, new_total - borrowed_count)
        except ValueError:
            print("Invalid total copies input.")
            return

    storage.save_books(books)
    print("Book updated successfully.")

def borrow_book(current_user: User):
    try:
        if not current_user:
            print("Please login first.")
            return

        book_id = input("Book ID: ").strip()
        users = storage.load_users()
        books = storage.load_books()
        transactions = storage.load_transactions()

        user = next((u for u in users if u.user_id == current_user.user_id), None)
        book = next((b for b in books if b.book_id == book_id), None)

        if not user:
            print("User not found!")
            return
        if not book:
            print("Book not found!")
            return
        if book.is_deleted:
            print("Book is deleted and cannot be borrowed.")
            return
        if not user.can_borrow():
            print(f"User {user.name} cannot borrow more books.")
            return
        if not book.is_available():
            print(f"Book {book.title} is not available.")
            return

        # Prevent borrowing same book twice until returned
        active_same_book = any(
            tx.book_id == book_id and tx.user_id == user.user_id and tx.status == "borrowed"
            for tx in transactions
        )
        if active_same_book:
            print("You have already borrowed this book and not returned it yet.")
            return

        borrow_date = today_str()
        due_date = add_days(borrow_date, 14)
        tx_id = make_tx_id(len(transactions) + 1)

        transaction = Transaction(tx_id, book_id, user.user_id, borrow_date, due_date)

        book.decrease_copies(1)
        user.increase_active_loans()

        storage.save_books(books)
        storage.save_users(users)

        transactions.append(transaction)
        storage.save_transactions(transactions)

        print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")
    except Exception as e:
        print(f"Error in borrow: {e}")

def return_book(current_user: User):
    try:
        if not current_user:
            print("Please login first.")
            return

        transaction_id = input("Transaction ID: ").strip()
        transactions = storage.load_transactions()
        transaction = next((t for t in transactions if t.tx_id == transaction_id), None)

        if not transaction:
            print("Transaction not found!")
            return
        if transaction.user_id != current_user.user_id:
            print("You can only return your own transactions.")
            return
        if transaction.status == "returned":
            print("This book has already been returned.")
            return

        transaction.mark_returned(today_str())

        books = storage.load_books()
        users = storage.load_users()

        book = next((b for b in books if b.book_id == transaction.book_id), None)
        user = next((u for u in users if u.user_id == transaction.user_id), None)

        if book:
            book.increase_copies(1)
            storage.save_books(books)
        if user:
            user.decrease_active_loans()
            storage.save_users(users)

        storage.save_transactions(transactions)

        print("Return successful.")
    except Exception as e:
        print(f"Error in return: {e}")
