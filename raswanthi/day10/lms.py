import sys
from storage import CSVStorage
from models import Book, User, Transaction
from datetime import datetime, timedelta

# Initialize the storage
storage = CSVStorage()

#add_book details 
def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    authors = input("Authors (comma separated): ")
    isbn = input("ISBN: ")
    tags = input("Tags (comma separated): ")
    total_copies = input("Total Copies: ")

    book = Book(book_id, title, authors, isbn, tags, total_copies)
    books = storage.load_books()
    books.append(book)
    storage.save_books(books)
    print("Book added successfully.")

#add user details
def add_user():
    user_id = input("User ID: ")
    name = input("Name: ")
    email = input("Email: ")
    status = input("Status (active/inactive/banned): ")
    max_loans = input("Max Loans: ")

    user = User(user_id, name, email, status, max_loans)
    users = storage.load_users()
    users.append(user)
    storage.save_users(users)
    print("User added successfully.")

#borrow book details
def borrow_book():
    user_id = input("User ID: ")
    book_id = input("Book ID: ")

    users = storage.load_users()
    books = storage.load_books()

    user = next((u for u in users if u.user_id == user_id), None)
    book = next((b for b in books if b.book_id == book_id), None)

    if not user:
        print("User not found!")
        return
    if not book:
        print("Book not found!")
        return
    if not user.can_borrow():
        print(f"User {user.name} cannot borrow more books.")
        return
    if not book.is_available():
        print(f"Book {book.title} is not available.")
        return
    
    # Create the transaction
    borrow_date = datetime.today().strftime('%d-%m-%Y')
    due_date = (datetime.today() + timedelta(days=14)).strftime('%d-%m-%Y')
    tx_id = f"T{len(storage.load_transactions()) + 1}"
    transaction = Transaction(tx_id, book_id, user_id, borrow_date, due_date)
    
    # Update the available copies
    book.decrease_copies(1)
    books = storage.load_books()
    storage.save_books(books)
    
    # Add transaction
    transactions = storage.load_transactions()
    transactions.append(transaction)
    storage.save_transactions(transactions)

    print(f"Borrow successful. Transaction ID: {tx_id}. Due Date: {due_date}.")

#return book details
def return_book():
    transaction_id = input("Transaction ID: ")

    transactions = storage.load_transactions()
    transaction = next((t for t in transactions if t.tx_id == transaction_id), None)

    if not transaction:
        print("Transaction not found!")
        return
    if transaction.status == "returned":
        print("This book has already been returned.")
        return
    
    # Mark the transaction as returned
    transaction.mark_returned(datetime.today().strftime('%d-%m-%Y'))
    books = storage.load_books()
    book = next((b for b in books if b.book_id == transaction.book_id), None)
    
    if book:
        book.increase_copies(1)
        storage.save_books(books)
    
    transactions = storage.load_transactions()
    storage.save_transactions(transactions)
    
    print("Return successful.")

#showing active loans
def show_active_loans():
    transactions = storage.load_transactions()
    active_transactions = [t for t in transactions if t.status == 'borrowed']
    
    if not active_transactions:
        print("No active loans.")
    else:
        for tx in active_transactions:
            print(f"Transaction ID: {tx.tx_id}, User ID: {tx.user_id}, Book ID: {tx.book_id}, Due Date: {tx.due_date}")

def save_data():
    storage.save_books(storage.load_books())
    storage.save_users(storage.load_users())
    storage.save_transactions(storage.load_transactions())
    print("All data saved to CSV successfully.")

def exit_program():
    save_data()
    print("Exiting the program.")
    sys.exit()

def main():
    while True:
        command = input("lms> ").strip()
        #calling the functions
        if command == "book add":
            add_book()
        elif command == "user add":
            add_user()
        elif command.startswith("borrow"):
            borrow_book()
        elif command.startswith("return"):
            return_book()
        elif command == "loans active":
            show_active_loans()
        elif command == "save":
            save_data()
        elif command == "exit":
            exit_program()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()



# output:
# lms> book add
# Book ID: B1042
# Title: The International CTO
# Authors (comma separated): David Ivell
# ISBN: 6725349870
# Tags (comma separated): technology|strategy
# Total Copies: 3
# Book added successfully.
# lms> user add
# User ID: U2026
# Name: Ragavi
# Book added successfully.
# lms> user add
# User ID: U2026
# Name: Ragavi
# Email: ragavi@ust.com
# Status (active/inactive/banned): active
# Status (active/inactive/banned): active
# Max Loans: 3
# User added successfully.
# lms> borrow U2021 B1036
# User ID: U2021
# Book ID: B1036
# User Ajay Dev cannot borrow more books.
# lms> borrow 
# User ID: U2019
# Book ID: B1032
# Borrow successful. Transaction ID: T21. Due Date: 29-11-2025.
# lms> return T1
# Transaction ID: T3003
# Return successful.
# lms> save
# All data saved to CSV successfully.
# lms> exit
# All data saved to CSV successfully.
# Exiting the program.
