# lms.py
import os
from library import Library
from models import Book, User, Transaction
from utils import today, due_after_14_days, generate_id

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to continue...")

def print_header(title):
    clear_screen()
    print("=" * 60)
    print(f" {title.center(58)} ")
    print("=" * 60)
    print()

def get_input(prompt, required=False, input_type=str):
    while True:
        try:
            value = input(f"{prompt}: ").strip()
            if required and not value:
                print("  This field is required!")
                continue
            if not value:
                return None
            return input_type(value)
        except ValueError:
            print(f"  Invalid input. Please enter a valid {input_type.__name__}.")

# ==================== MAIN MENU ====================
def main_menu():
    print_header("LIBRARY MANAGEMENT SYSTEM")
    print("  1. Book Management")
    print("  2. User Management")
    print("  3. Borrow & Return")
    print("  4. Reports & Loans")
    print("  5. Search Books")
    print("  6. Exit")
    print()
    return get_input("Select option (1-6)", required=True)

# ==================== BOOK MENU ====================
def book_menu(lib):
    while True:
        print_header("BOOK MANAGEMENT")
        print("  1. Add New Book")
        print("  2. View Book Details")
        print("  3. Update Book")
        print("  4. Remove Book")
        print("  5. List All Books")
        print("  6. Back to Main Menu")
        print()
        
        choice = get_input("Select option (1-6)", required=True)
        
        if choice == "1":
            add_book(lib)
        elif choice == "2":
            view_book(lib)
        elif choice == "3":
            update_book(lib)
        elif choice == "4":
            remove_book(lib)
        elif choice == "5":
            list_books(lib)
        elif choice == "6":
            break
        else:
            print("  Invalid option!")
            pause()

def find_book(lib, book_id):
    """Helper to find book by ID"""
    for book in lib.books.values():
        if book.book_id == book_id:
            return book
    return None

def add_book(lib):
    print_header("ADD NEW BOOK")
    
    try:
        book_id = get_input("Book ID", required=True)
        
        # Check if book ID already exists
        if find_book(lib, book_id):
            print("\n  Book ID already exists!")
            pause()
            return
            
        title = get_input("Title", required=True)
        authors_input = get_input("Author", required=True)
        isbn = get_input("ISBN", required=True)
        
        # Check if ISBN already exists
        for book in lib.books.values():
            if book.isbn == isbn:
                print("\n  ISBN already exists!")
                pause()
                return
        
        tags_input = get_input("Tags (separate with |)", required=False) or ""
        total = get_input("Total Copies", required=True, input_type=int)
        
        # Available copies = Total copies initially
        available = total
        
        # Create Book object
        new_book = Book(
            book_id=book_id,
            title=title,
            authors=authors_input,
            isbn=isbn,
            tags=tags_input,
            total_copies=total,
            available_copies=available
        )
        
        # Add to library
        lib.books[book_id] = new_book
        
        # Save to CSV
        lib.storage.save_books(lib.books)
        
        print("\n  Book added successfully!")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def view_book(lib):
    print_header("VIEW BOOK DETAILS")
    
    book_id = get_input("Enter Book ID", required=True)
    
    try:
        book = find_book(lib, book_id)
        
        if not book:
            print(f"\n  Book not found!")
        else:
            authors_display = ', '.join(book.authors) if isinstance(book.authors, list) else book.authors
            tags_display = ', '.join(book.tags) if isinstance(book.tags, list) and book.tags else 'None'
            
            print("\n" + "-" * 60)
            print(f"  Book ID       : {book.book_id}")
            print(f"  Title         : {book.title}")
            print(f"  Author(s)     : {authors_display}")
            print(f"  ISBN          : {book.isbn}")
            print(f"  Tags          : {tags_display}")
            print(f"  Total Copies  : {book.total_copies}")
            print(f"  Available     : {book.available_copies}")
            print("-" * 60)
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def update_book(lib):
    print_header("UPDATE BOOK")
    
    book_id = get_input("Enter Book ID", required=True)
    
    try:
        book = find_book(lib, book_id)
        
        if not book:
            print(f"\n  Book not found!")
            pause()
            return
        
        authors_display = ', '.join(book.authors) if isinstance(book.authors, list) else book.authors
        tags_display = ', '.join(book.tags) if isinstance(book.tags, list) else ''
        
        print("\n Current Details:")
        print(f"  Title: {book.title}")
        print(f"  Author: {authors_display}")
        print(f"  ISBN: {book.isbn}")
        print(f"  Tags: {tags_display}")
        print(f"  Total Copies: {book.total_copies}")
        print(f"  Available Copies: {book.available_copies}")
        print("\n  (Leave blank to keep current value)\n")
        
        title = get_input("New Title", required=False)
        authors_input = get_input("New Author", required=False)
        isbn = get_input("New ISBN", required=False)
        tags_input = get_input("New Tags (| separated)", required=False)
        total = get_input("New Total Copies", required=False, input_type=int)
        
        # Update book object
        if title:
            book.title = title
        if authors_input:
            book.authors = [a.strip() for a in authors_input.split("|") if a.strip()]
        if isbn:
            book.isbn = isbn
        if tags_input:
            book.tags = [t.strip() for t in tags_input.split("|") if t.strip()]
        if total:
            # Calculate difference and adjust available copies accordingly
            difference = total - book.total_copies
            book.total_copies = total
            book.available_copies += difference
            
            # Ensure available copies don't go negative
            if book.available_copies < 0:
                print(f"\n  Warning: Available copies adjusted to 0 (cannot have negative copies)")
                book.available_copies = 0
        
        # Save to CSV
        lib.storage.save_books(lib.books)
        
        print("\n  Book updated successfully!")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def remove_book(lib):
    print_header("REMOVE BOOK")
    
    book_id = get_input("Enter Book ID to remove", required=True)
    
    try:
        book = find_book(lib, book_id)
        
        if not book:
            print(f"\n  Book not found!")
            pause()
            return
        
        # Check for active loans
        active_loans = [t for t in lib.transactions.values() 
                       if t.book_id == book_id and t.status == "borrowed"]
        
        if active_loans:
            print(f"\n  Cannot remove: {len(active_loans)} active loan(s) exist!")
            pause()
            return
        
        print(f"\n  Title: {book.title}")
        confirm = get_input("Are you sure? (yes/no)", required=True).lower()
        
        if confirm == "yes":
            del lib.books[book_id]
            lib.storage.save_books(lib.books)
            print("\n  Book removed successfully!")
        else:
            print("\n  Operation cancelled.")
            
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def list_books(lib):
    print_header("ALL BOOKS")
    
    books = lib.books
    
    if not books:
        print("  No books in the library.")
    else:
        print(f"  {'ID':<15} {'Title':<45}")
        print("  " + "-" * 60)
        for book in books.values():
            title_short = book.title[:43] + ".." if len(book.title) > 45 else book.title
            print(f"  {book.book_id:<15} {title_short:<45}")
    
    pause()

# ==================== USER MENU ====================
def user_menu(lib):
    while True:
        print_header("USER MANAGEMENT")
        print("  1. Add New User")
        print("  2. View User Details")
        print("  3. Update User")
        print("  4. List All Users")
        print("  5. Change User Status")
        print("  6. Back to Main Menu")
        print()
        
        choice = get_input("Select option (1-6)", required=True)
        
        if choice == "1":
            add_user(lib)
        elif choice == "2":
            view_user(lib)
        elif choice == "3":
            update_user(lib)
        elif choice == "4":
            list_users(lib)
        elif choice == "5":
            change_user_status(lib)
        elif choice == "6":
            break
        else:
            print("  Invalid option!")
            pause()

def find_user(lib, user_id):
    """Helper to find user by ID"""
    for user in lib.users.values():
        if user.user_id == user_id:
            return user
    return None

def validate_email(email):
    """Validate email ends with @ust.com"""
    if not email:
        return False  # Empty email is NOT allowed
    return email.endswith("@ust.com")

def add_user(lib):
    print_header("ADD NEW USER")
    
    try:
        user_id = get_input("User ID", required=True)
        
        # Check if user exists
        if find_user(lib, user_id):
            print("\n  User ID already exists!")
            pause()
            return
        
        name = get_input("Name", required=True)
        
        # Email validation loop
        while True:
            email = get_input("Email", required=True)
            if validate_email(email):
                break
            else:
                print("  Email must end with @ust.com")
        
        # Default max_loans is 5
        max_loans = 5
        
        # Create User object
        new_user = User(
            user_id=user_id,
            name=name,
            email=email,
            status="active",
            max_loans=max_loans
        )
        
        # Add to library
        lib.users[user_id] = new_user
        
        # Save to CSV
        lib.storage.save_users(lib.users)
        
        print("\n  User added successfully!")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def view_user(lib):
    print_header("VIEW USER DETAILS")
    
    user_id = get_input("Enter User ID", required=True)
    
    try:
        user = find_user(lib, user_id)
        
        if not user:
            print(f"\n  User not found!")
        else:
            active_loans = sum(1 for t in lib.transactions.values() 
                             if t.user_id == user_id and t.status == "borrowed")
            
            print("\n" + "-" * 60)
            print(f"  User ID       : {user.user_id}")
            print(f"  Name          : {user.name}")
            print(f"  Email         : {user.email}")
            print(f"  Status        : {user.status.upper()}")
            print(f"  Max Loans     : {user.max_loans}")
            print(f"  Active Loans  : {active_loans}")
            print("-" * 60)
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def update_user(lib):
    print_header("UPDATE USER")
    
    user_id = get_input("Enter User ID", required=True)
    
    try:
        user = find_user(lib, user_id)
        
        if not user:
            print(f"\n  User not found!")
            pause()
            return
        
        print("\n👤 Current Details:")
        print(f"  Name: {user.name}")
        print(f"  Email: {user.email}")
        print("\n  (Leave blank to keep current value)\n")
        
        name = get_input("New Name", required=False)
        email = get_input("New Email", required=False)
        
        # Update user object
        if name:
            user.name = name
        if email:
            user.email = email
        
        # Save to CSV
        lib.storage.save_users(lib.users)
        
        print("\n  User updated successfully!")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def list_users(lib):
    print_header("LIST USERS")
    
    users = lib.users
    
    if not users:
        print("  No users registered.")
        pause()
        return
    
    # Show filter options
    print("  Filter by:")
    print("  1. All Users")
    print("  2. Active Users Only")
    print("  3. Inactive Users Only")
    print("  4. Banned Users Only")
    print()
    
    filter_choice = get_input("Select filter (1-4)", required=True)
    
    # Filter users based on selection
    if filter_choice == "1":
        filtered_users = list(users.values())
        filter_label = "ALL USERS"
    elif filter_choice == "2":
        filtered_users = [u for u in users.values() if u.status == "active"]
        filter_label = "ACTIVE USERS"
    elif filter_choice == "3":
        filtered_users = [u for u in users.values() if u.status == "inactive"]
        filter_label = "INACTIVE USERS"
    elif filter_choice == "4":
        filtered_users = [u for u in users.values() if u.status == "banned"]
        filter_label = "BANNED USERS"
    else:
        print("  Invalid option!")
        pause()
        return
    
    # Display filtered results
    print(f"\n  {filter_label}")
    print("  " + "=" * 60)
    
    if not filtered_users:
        print(f"  No users found.")
    else:
        print(f"\n  {'ID':<15} {'Name':<45}")
        print("  " + "-" * 60)
        for user in filtered_users:
            name_short = user.name[:43] + ".." if len(user.name) > 45 else user.name
            print(f"  {user.user_id:<15} {name_short:<45}")
    
    pause()

def change_user_status(lib):
    print_header("CHANGE USER STATUS")
    
    user_id = get_input("Enter User ID", required=True)
    
    try:
        user = find_user(lib, user_id)
        
        if not user:
            print(f"\n  User not found!")
            pause()
            return
        
        print(f"\n  Current Status: {user.status.upper()}")
        print("\n  1. Activate")
        print("  2. Deactivate")
        print("  3. Ban")
        print()
        
        choice = get_input("Select option (1-3)", required=True)
        
        if choice == "1":
            user.status = "active"
            lib.storage.save_users(lib.users)
            print("\n  User activated!")
        elif choice == "2":
            user.status = "inactive"
            lib.storage.save_users(lib.users)
            print("\n  User deactivated!")
        elif choice == "3":
            user.status = "banned"
            lib.storage.save_users(lib.users)
            print("\n  User banned!")
        else:
            print("\n  Invalid option!")
            
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

# ==================== BORROW & RETURN ====================
def borrow_return_menu(lib):
    while True:
        print_header("BORROW & RETURN")
        print("  1. Borrow Book")
        print("  2. Return Book")
        print("  3. Back to Main Menu")
        print()
        
        choice = get_input("Select option (1-3)", required=True)
        
        if choice == "1":
            borrow_book(lib)
        elif choice == "2":
            return_book(lib)
        elif choice == "3":
            break
        else:
            print("  Invalid option!")
            pause()

def borrow_book(lib):
    print_header("BORROW BOOK")
    
    try:
        user_id = get_input("User ID", required=True)
        book_id = get_input("Book ID", required=True)
        
        # Validate user exists
        user = find_user(lib, user_id)
        if not user:
            print("\n  User not found!")
            pause()
            return
        
        # Validate book exists
        book = find_book(lib, book_id)
        if not book:
            print("\n  Book not found!")
            pause()
            return
        
        # Check user status and loan limit
        active_loans = sum(1 for t in lib.transactions.values() 
                          if t.user_id == user_id and t.status == "borrowed")
        
        if user.status != "active":
            print(f"\n  User is {user.status}. Cannot borrow books!")
            pause()
            return
        
        if active_loans >= user.max_loans:
            print(f"\n  User has reached maximum loan limit ({user.max_loans})!")
            pause()
            return
        
        # Check book availability
        if book.available_copies <= 0:
            print("\n  Book is not available!")
            pause()
            return
        
        # Create transaction
        tx_id = generate_id("T", lib.transactions)
        
        new_tx = Transaction(
            tx_id=tx_id,
            book_id=book_id,
            user_id=user_id,
            borrow_date=today(),
            due_date=due_after_14_days(),
            return_date=None,
            status="borrowed"
        )
        
        # Update records
        lib.transactions[tx_id] = new_tx
        book.available_copies -= 1
        
        # Save to CSV
        lib.storage.save_books(lib.books)
        lib.storage.save_transactions(lib.transactions)
        
        print("\n  Book borrowed successfully!")
        print(f"\n  Transaction ID: {new_tx.tx_id}")
        print(f"  Due Date: {new_tx.due_date}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def return_book(lib):
    print_header("RETURN BOOK")
    
    try:
        tx_id = get_input("Transaction ID", required=True)
        
        # Find transaction
        if tx_id not in lib.transactions:
            print("\n  Transaction not found!")
            pause()
            return
        
        tx = lib.transactions[tx_id]
        
        # Check if already returned
        if tx.status != "borrowed":
            print("\n  Book already returned!")
            pause()
            return
        
        # Get book
        book = find_book(lib, tx.book_id)
        if not book:
            print("\n  Book not found!")
            pause()
            return
        
        # Update transaction and book
        tx.return_date = today()
        tx.status = "returned"
        book.available_copies += 1
        
        # Save to CSV
        lib.storage.save_books(lib.books)
        lib.storage.save_transactions(lib.transactions)
        
        print("\n  Book returned successfully!")
        print(f"\n  Transaction ID: {tx.tx_id}")
        print(f"  Return Date: {tx.return_date}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

# ==================== REPORTS & LOANS ====================
def reports_menu(lib):
    while True:
        print_header("REPORTS & LOANS")
        print("  1. Library Summary")
        print("  2. Active Loans")
        print("  3. Overdue Loans")
        print("  4. User History")
        print("  5. Back to Main Menu")
        print()
        
        choice = get_input("Select option (1-5)", required=True)
        
        if choice == "1":
            show_summary(lib)
        elif choice == "2":
            show_active_loans(lib)
        elif choice == "3":
            show_overdue_loans(lib)
        elif choice == "4":
            show_user_history(lib)
        elif choice == "5":
            break
        else:
            print("  Invalid option!")
            pause()

def show_summary(lib):
    print_header("LIBRARY SUMMARY")
    
    try:
        current_date = today()
        
        active_loans = sum(1 for t in lib.transactions.values() if t.status == "borrowed")
        overdue_loans = sum(1 for t in lib.transactions.values() 
                           if t.status == "borrowed" and t.is_overdue(current_date))
        
        print("\n" + "=" * 60)
        print(f"  Total Books      : {len(lib.books)}")
        print(f"  Total Users      : {len(lib.users)}")
        print(f"  Active Loans     : {active_loans}")
        print(f"  Overdue Loans    : {overdue_loans}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def show_active_loans(lib):
    print_header("ACTIVE LOANS")
    
    try:
        loans = [t for t in lib.transactions.values() if t.status == "borrowed"]
        
        if not loans:
            print("  No active loans.")
        else:
            print(f"  {'TX ID':<10} {'User ID':<15} {'Book ID':<15} {'Due Date':<12}")
            print("  " + "-" * 52)
            for tx in loans:
                print(f"  {tx.tx_id:<10} {tx.user_id:<15} {tx.book_id:<15} {tx.due_date:<12}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def show_overdue_loans(lib):
    print_header("OVERDUE LOANS")
    
    try:
        current_date = today()
        loans = [
            t for t in lib.transactions.values()
            if t.status == "borrowed" and t.is_overdue(current_date)
        ]
        
        if not loans:
            print("  No overdue loans.")
        else:
            print(f"  {'TX ID':<10} {'User ID':<15} {'Book ID':<15} {'Due Date':<12}")
            print("  " + "-" * 52)
            for tx in loans:
                print(f"  {tx.tx_id:<10} {tx.user_id:<15} {tx.book_id:<15} {tx.due_date:<12}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def show_user_history(lib):
    print_header("USER HISTORY")
    
    user_id = get_input("Enter User ID", required=True)
    
    try:
        # Validate user exists
        user = find_user(lib, user_id)
        if not user:
            print("\n  User not found!")
            pause()
            return
        
        history = [t for t in lib.transactions.values() if t.user_id == user_id]
        
        if not history:
            print("\n  No transaction history.")
        else:
            print(f"\n  {'TX ID':<10} {'Book ID':<15} {'Borrowed':<12} {'Due':<12} {'Status':<10}")
            print("  " + "-" * 59)
            for tx in history:
                print(f"  {tx.tx_id:<10} {tx.book_id:<15} {tx.borrow_date:<12} {tx.due_date:<12} {tx.status.upper():<10}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

# ==================== SEARCH ====================
def search_books(lib):
    print_header("SEARCH BOOKS")
    
    print("  Search by:")
    title = get_input("  Title (or press Enter to skip)", required=False)
    author = get_input("  Author (or press Enter to skip)", required=False)
    tag = get_input("  Tag (or press Enter to skip)", required=False)
    
    try:
        results = list(lib.books.values())
        
        # Filter by title
        if title:
            results = [b for b in results if title.lower() in b.title.lower()]
        
        # Filter by author
        if author:
            results = [b for b in results 
                      if any(author.lower() in a.lower() for a in (b.authors if isinstance(b.authors, list) else [b.authors]))]
        
        # Filter by tag
        if tag:
            results = [b for b in results 
                      if any(tag.lower() in t.lower() for t in (b.tags if isinstance(b.tags, list) else []))]
        
        if not results:
            print("\n  No books found matching your criteria.")
        else:
            print(f"\n  Found {len(results)} book(s):\n")
            print(f"  {'ID':<10} {'Title':<35} {'Author':<20}")
            print("  " + "-" * 65)
            for book in results:
                title_short = book.title[:33] + ".." if len(book.title) > 35 else book.title
                
                if isinstance(book.authors, list):
                    author_str = ', '.join(book.authors)
                else:
                    author_str = book.authors
                
                author_short = author_str[:18] + ".." if len(author_str) > 20 else author_str
                print(f"  {book.book_id:<10} {title_short:<35} {author_short:<20}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

# ==================== MAIN ====================
def main():
    try:
        lib = Library()
        
        while True:
            choice = main_menu()
            
            if choice == "1":
                book_menu(lib)
            elif choice == "2":
                user_menu(lib)
            elif choice == "3":
                borrow_return_menu(lib)
            elif choice == "4":
                reports_menu(lib)
            elif choice == "5":
                search_books(lib)
            elif choice == "6":
                print_header("GOODBYE!")
                print("  Thank you for using the Library Management System!\n")
                break
            else:
                print("  Invalid option!")
                pause()
                
    except KeyboardInterrupt:
        print("\n\n  Program interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n  Fatal Error: {str(e)}\n")

if __name__ == "__main__":
    main()