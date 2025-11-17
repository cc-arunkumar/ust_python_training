import os
import json
from datetime import datetime, timedelta
from library import Library
from models import User
from utils import today
import lms

# Get the base directory and data folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# File to store login attempts and lockouts
LOCKOUT_FILE = os.path.join(DATA_DIR, "lockouts.json")

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

def load_lockouts():
    """Load lockout data from file"""
    if os.path.exists(LOCKOUT_FILE):
        try:
            with open(LOCKOUT_FILE, 'r') as f:
                data = json.load(f)
                # Validate data structure
                if isinstance(data, dict):
                    return data
                return {}
        except (json.JSONDecodeError, Exception):
            # If file is corrupted, start fresh
            return {}
    return {}

def save_lockouts(lockouts):
    """Save lockout data to file"""
    with open(LOCKOUT_FILE, 'w') as f:
        json.dump(lockouts, f)

def is_locked_out(user_id):
    """Check if user is locked out"""
    lockouts = load_lockouts()
    if user_id in lockouts:
        locked_until = lockouts[user_id].get('locked_until')
        
        # Check if locked_until exists and is not None
        if locked_until:
            try:
                lockout_time = datetime.fromisoformat(locked_until)
                if datetime.now() < lockout_time:
                    remaining = lockout_time - datetime.now()
                    minutes = int(remaining.total_seconds() / 60)
                    return True, minutes
                else:
                    # Lockout expired, remove it
                    del lockouts[user_id]
                    save_lockouts(lockouts)
            except (ValueError, TypeError):
                # Invalid lockout data, remove it
                del lockouts[user_id]
                save_lockouts(lockouts)
    return False, 0

def record_failed_attempt(user_id):
    """Record a failed login attempt"""
    lockouts = load_lockouts()
    
    if user_id not in lockouts:
        lockouts[user_id] = {'attempts': 0, 'locked_until': None}
    
    lockouts[user_id]['attempts'] += 1
    
    if lockouts[user_id]['attempts'] >= 3:
        # Lock account for 1 hour
        lockout_time = datetime.now() + timedelta(hours=1)
        lockouts[user_id]['locked_until'] = lockout_time.isoformat()
        lockouts[user_id]['attempts'] = 0
        save_lockouts(lockouts)
        return True  # Account locked
    
    save_lockouts(lockouts)
    return False  # Not locked yet

def clear_failed_attempts(user_id):
    """Clear failed attempts after successful login"""
    lockouts = load_lockouts()
    if user_id in lockouts:
        del lockouts[user_id]
        save_lockouts(lockouts)

def validate_password(user_id, password, lib):
    """Validate user password"""
    # Admin credentials
    if user_id.lower() == "admin" and password == "admin":
        return True, "admin"
    
    # Regular user validation
    user = lms.find_user(lib, user_id)
    if user:
        # Password is user_id in lowercase
        if password == user_id.lower():
            return True, "user"
    
    return False, None

def register_user(lib):
    """Register a new user"""
    print_header("USER REGISTRATION")
    
    try:
        user_id = input("Enter User ID: ").strip()
        
        if not user_id:
            print("\n  User ID cannot be empty!")
            pause()
            return False
        
        # Check if user already exists
        if lms.find_user(lib, user_id) or user_id.lower() == "admin":
            print("\n  User ID already exists!")
            pause()
            return False
        
        name = input("Enter Name: ").strip()
        if not name:
            print("\n  Name cannot be empty!")
            pause()
            return False
        
        # Email validation
        while True:
            email = input("Enter Email: ").strip()
            if not email:
                print("  Email cannot be empty!")
                continue
            if email.endswith("@ust.com"):
                break
            else:
                print("  Email must end with @ust.com")
        
        # Create new user
        new_user = User(
            user_id=user_id,
            name=name,
            email=email,
            status="active",
            max_loans=5
        )
        
        lib.users[user_id] = new_user
        lib.storage.save_users(lib.users)
        
        print("\n  Registration successful!")
        print(f"  Your password is: {user_id.lower()}")
        print("  (Password is case-sensitive)")
        pause()
        return True
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
        pause()
        return False

def login_screen(lib):
    """Display login screen and handle authentication"""
    while True:
        print_header("LIBRARY MANAGEMENT SYSTEM - LOGIN")
        print("  1. Login")
        print("  2. Register")
        print("  3. Exit")
        print()
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            # Login
            print_header("LOGIN")
            user_id = input("User ID: ").strip()
            
            if not user_id:
                print("\n  User ID cannot be empty!")
                pause()
                continue
            
            # Check if account is locked
            locked, minutes = is_locked_out(user_id)
            if locked:
                print(f"\n  Account locked! Try again after {minutes} minute(s).")
                pause()
                continue
            
            password = input("Password: ").strip()
            
            # Validate credentials
            valid, role = validate_password(user_id, password, lib)
            
            if valid:
                clear_failed_attempts(user_id)
                return user_id, role
            else:
                is_locked = record_failed_attempt(user_id)
                if is_locked:
                    print("\n  Too many failed attempts!")
                    print("  Account locked for 1 hour.")
                else:
                    lockouts = load_lockouts()
                    attempts = lockouts.get(user_id, {}).get('attempts', 0)
                    remaining = 3 - attempts
                    print(f"\n  Invalid credentials! {remaining} attempt(s) remaining.")
                pause()
                
        elif choice == "2":
            # Register
            register_user(lib)
            
        elif choice == "3":
            # Exit
            return None, None
            
        else:
            print("\n  Invalid option!")
            pause()

# ==================== USER MENU ====================
def user_main_menu(lib, user_id):
    """Main menu for regular users"""
    while True:
        print_header(f"LIBRARY MANAGEMENT SYSTEM - USER: {user_id}")
        print("  1. Search Books")
        print("  2. My Active Loans")
        print("  3. My Loan History")
        print("  4. View My Profile")
        print("  5. Logout")
        print()
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            user_search_books(lib, user_id)
        elif choice == "2":
            user_active_loans(lib, user_id)
        elif choice == "3":
            user_loan_history(lib, user_id)
        elif choice == "4":
            user_view_profile(lib, user_id)
        elif choice == "5":
            print_header("LOGOUT")
            print("  Logged out successfully!\n")
            pause()
            break
        else:
            print("  Invalid option!")
            pause()

def user_search_books(lib, user_id):
    """Search books - user view with availability"""
    print_header("SEARCH BOOKS")
    
    print("  Search by:")
    title = input("  Title (or press Enter to skip): ").strip()
    author = input("  Author (or press Enter to skip): ").strip()
    tag = input("  Tag (or press Enter to skip): ").strip()
    
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
            print(f"  {'ID':<12} {'Title':<30} {'Available':<10} {'Total':<8}")
            print("  " + "-" * 60)
            for book in results:
                title_short = book.title[:28] + ".." if len(book.title) > 30 else book.title
                avail_status = "Yes" if book.available_copies > 0 else "No"
                print(f"  {book.book_id:<12} {title_short:<30} {avail_status:<10} {book.total_copies:<8}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def user_active_loans(lib, user_id):
    """View user's active loans"""
    print_header("MY ACTIVE LOANS")
    
    try:
        current_date = today()
        loans = [t for t in lib.transactions.values() 
                if t.user_id == user_id and t.status == "borrowed"]
        
        if not loans:
            print("  No active loans.")
        else:
            print(f"  {'TX ID':<12} {'Book ID':<15} {'Borrowed':<12} {'Due Date':<12} {'Status':<10}")
            print("  " + "-" * 61)
            for tx in loans:
                status = "OVERDUE" if tx.is_overdue(current_date) else "ACTIVE"
                print(f"  {tx.tx_id:<12} {tx.book_id:<15} {tx.borrow_date:<12} {tx.due_date:<12} {status:<10}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def user_loan_history(lib, user_id):
    """View user's complete loan history"""
    print_header("MY LOAN HISTORY")
    
    try:
        history = [t for t in lib.transactions.values() if t.user_id == user_id]
        
        if not history:
            print("\n  No transaction history.")
        else:
            print(f"\n  {'TX ID':<12} {'Book ID':<15} {'Borrowed':<12} {'Due':<12} {'Status':<10}")
            print("  " + "-" * 61)
            for tx in history:
                print(f"  {tx.tx_id:<12} {tx.book_id:<15} {tx.borrow_date:<12} {tx.due_date:<12} {tx.status.upper():<10}")
        
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

def user_view_profile(lib, user_id):
    """View user profile"""
    print_header("MY PROFILE")
    
    try:
        user = lms.find_user(lib, user_id)
        
        if not user:
            print("\n  User not found!")
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
            print(f"  Password      : {user_id.lower()}")
            print("-" * 60)
    except Exception as e:
        print(f"\n  Error: {str(e)}")
    
    pause()

# ==================== MAIN ====================
def main():
    try:
        lib = Library()
        
        while True:
            # Show login screen
            user_id, role = login_screen(lib)
            
            if user_id is None:
                # User chose to exit
                print_header("GOODBYE!")
                print("  Thank you for using the Library Management System!\n")
                break
            
            # Route to appropriate interface based on role
            if role == "admin":
                # Admin gets full access to original LMS
                print_header("ADMIN ACCESS GRANTED")
                print(f"  Welcome, Administrator!\n")
                pause()
                
                # Run the original LMS main loop
                while True:
                    choice = lms.main_menu()
                    
                    if choice == "1":
                        lms.book_menu(lib)
                    elif choice == "2":
                        lms.user_menu(lib)
                    elif choice == "3":
                        lms.borrow_return_menu(lib)
                    elif choice == "4":
                        lms.reports_menu(lib)
                    elif choice == "5":
                        lms.search_books(lib)
                    elif choice == "6":
                        print_header("LOGOUT")
                        print("  Admin logged out successfully!\n")
                        pause()
                        break
                    else:
                        print("  Invalid option!")
                        pause()
                        
            elif role == "user":
                # Regular user gets limited access
                user = lms.find_user(lib, user_id)
                
                if user.status != "active":
                    print_header("ACCESS DENIED")
                    print(f"  Your account is {user.status}.")
                    print("  Please contact the administrator.\n")
                    pause()
                    continue
                
                print_header("USER ACCESS GRANTED")
                print(f"  Welcome, {user.name}!\n")
                pause()
                
                # Show user menu
                user_main_menu(lib, user_id)
                
    except KeyboardInterrupt:
        print("\n\n  Program interrupted. Goodbye!\n")
    except Exception as e:
        print(f"\n  Fatal Error: {str(e)}\n")

if __name__ == "__main__":
    main()