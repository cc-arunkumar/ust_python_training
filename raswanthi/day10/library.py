import storage
from models import Book, User, Transaction
from datetime import datetime, timedelta

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors = input("Authors (comma separated): ")
    isbn = input("ISBN: ")
    tags = input("Tags (comma separated): ")
    total_copies = int(input("Total Copies: "))
    
    book = Book(book_id, title, authors, isbn, tags, total_copies, total_copies)
    books = storage.load_books()
    books.append(book)
    storage.save_books(books)
    print(f"Book {book.title} added successfully.")
    #book is added successfully

def borrow_book():
    user_id = input("User ID: ") #input user ID
    book_id = input("Book ID: ") #input book ID
    
    users = storage.load_users()
    books = storage.load_books()
    
    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)

    if not user: #print if user not found
        print("User not found!") 
        return
    if not book: #print if book not found
        print("Book not found!")
        return
    if not user.can_borrow():
        print(f"User {user.name} cannot borrow more books.") #checks for the borrowing limit
        return
    if not book.is_available():
        print(f"Book {book.title} is not available.") #print if book not available
        return
    
    borrow_date = datetime.today().strftime('%d-%m-%Y')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
    tx_id = f"T{len(storage.load_transactions()) + 1}"
    
    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    
    book.decrease_copies(1)
    books = storage.load_books()
    storage.save_books(books)
    
    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)

    print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")
