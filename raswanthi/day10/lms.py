
import sys
from storage import CSVStorage
from models import Book, User
from utils import today_str, add_days, parse_comma_list, make_tx_id
from library import (
    add_book, soft_delete_book, restore_book, update_book,
    borrow_book, return_book
)

storage = CSVStorage()
current_user = None

def login():
    global current_user
    user_id = input("User ID: ").strip()
    password = input("Password: ").strip()
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        print("User not found.")
        return False
    if user.password != password:
        print("Incorrect password.")
        return False
    current_user = user
    print(f"You are Logged in as {user.name} ({user.user_id})")
    return True

def add_user():
    try:
        user_id = input("User ID: ").strip()
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        status = input("Status (active/inactive/banned): ").strip().lower()
        max_loans = int(input("Max Loans: ").strip())
        password = input("Password: ").strip()

        users = storage.load_users()
        if any(u.user_id == user_id for u in users):
            print("User ID already exists.")
            return

        user = User(user_id, name, email, status, max_loans, active_loans=0, password=password)
        users.append(user)
        storage.save_users(users)
        print("User added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def update_user():
    user_id = input("User ID to update: ").strip()
    users = storage.load_users()
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        print("User not found.")
        return

    print("Current details:")
    print(f"- Name: {user.name}")
    print(f"- Email: {user.email}")
    print(f"- Status: {user.status}")
    print(f"- Max Loans: {user.max_loans}")
    print(f"- Active Loans: {user.active_loans}")

    name = input("New Name (leave blank to keep): ").strip()
    email = input("New Email (leave blank to keep): ").strip()
    status = input("New Status (active/inactive/banned, leave blank to keep): ").strip().lower()
    max_loans_input = input("New Max Loans (leave blank to keep): ").strip()
    password = input("New Password (leave blank to keep): ").strip()

    if name:
        user.name = name
    if email:
        user.email = email
    if status:
        if status in {"active", "inactive", "banned"}:
            user.status = status
        else:
            print("Invalid status.")
            return
    if max_loans_input:
        try:
            new_max = int(max_loans_input)
            if new_max < user.active_loans:
                print("Max loans cannot be less than current active loans.")
                return
            user.max_loans = new_max
        except ValueError:
            print("Invalid max loans.")
            return
    if password:
        user.password = password

    storage.save_users(users)
    print("User updated successfully.")

def show_active_loans():
    transactions = storage.load_transactions()
    active_transactions = [t for t in transactions if t.status == 'borrowed']
    if not active_transactions:
        print("No active loans.")
        return
    for tx in active_transactions:
        print(f"Transaction ID: {tx.tx_id}, User ID: {tx.user_id}, Book ID: {tx.book_id}, Due Date: {tx.due_date}")

def show_overdue_loans():
    transactions = storage.load_transactions()
    overdue = [t for t in transactions if t.overdue == "1"]  # <-- check CSV field
    if not overdue:
        print("No overdue loans.")
        return
    for tx in overdue:
        print(f"Overdue -> TX: {tx.tx_id}, User: {tx.user_id}, Book: {tx.book_id}, Due: {tx.due_date}")


def show_available_books():
    books = storage.load_books()
    available_books = [book for book in books if book.is_available()]
    if not available_books:
        print("No available books at the moment.")
        return
    print("\nAvailable Books:")
    for book in available_books:
        print(f"Book ID: {book.book_id}, Title: {book.title}, Authors: {', '.join(book.authors)}, Copies Available: {book.available_copies}")

def save_data():
    try:
        storage.save_books(storage.load_books())
        storage.save_users(storage.load_users())
        storage.save_transactions(storage.load_transactions())
        print("All data saved to CSV successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

def display_menu():
    print("\nLibrary Management System")
    print("Please choose an option (type the number):")
    print("1. Add a Book")
    print("2. Soft Delete a Book")
    print("3. Restore a Book")
    print("4. Update a Book")
    print("5. Add a User")
    print("6. Update a User")
    print("7. Borrow a Book")
    print("8. Return a Book")
    print("9. View Active Loans")
    print("10. View Overdue Loans")
    print("11. View Available Books")
    print("12. Save Data")
    print("13. Help")
    print("14. Exit")

def help_menu():
    print("""
Commands:
  1. Add a Book
  2. Soft Delete a Book
  3. Restore a Book
  4. Update a Book
  5. Add a User
  6. Update a User
  7. Borrow a Book (requires login)
  8. Return a Book (requires login)
  9. View Active Loans
  10. View Overdue Loans
  11. View Available Books
  12. Save Data
  13. Help
  14. Exit
""")

def main():
    # Force login first
    while True:
        print("\n--- LOGIN REQUIRED ---")
        if login():
            break
        else:
            print("Login failed. Try again.\n")

    # Show menu after successful login
    while True:
        display_menu()
        try:
            choice = input("\nEnter the number of your choice: ").strip()
            if not choice.isdigit():
                print("Please enter a valid number.")
                continue
            command = int(choice)

            if command == 1:
                add_book()
            elif command == 2:
                soft_delete_book()
            elif command == 3:
                restore_book()
            elif command == 4:
                update_book()
            elif command == 5:
                add_user()
            elif command == 6:
                update_user()
            elif command == 7:
                borrow_book(current_user)
            elif command == 8:
                return_book(current_user)
            elif command == 9:
                show_active_loans()
            elif command == 10:
                show_overdue_loans()
            elif command == 11:
                show_available_books()
            elif command == 12:
                save_data()
            elif command == 13:
                help_menu()
            elif command == 14:
                save_data()
                print("Exiting the program.")
                sys.exit(0)
            else:
                print("Invalid choice! Please enter a number between 1 and 14.")
        except KeyboardInterrupt:
            print("\nInterrupted. Saving and exiting.")
            save_data()
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


#output:

# --- LOGIN REQUIRED ---
# User ID: U2011
# Password: a
# Incorrect password.
# Login failed. Try again.


# --- LOGIN REQUIRED ---
# User ID: U2030
# Password: ravi
# You are Logged in as Ravi (U2030)

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 1
# Book ID: 
# Title: 
# Authors (comma separated): 
# ISBN: 
# Tags (comma separated): 
# Total Copies: 
# Invalid input: invalid literal for int() with base 10: ''

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 11

# Available Books:
# Book ID: B1001, Title: Python Crash Course, Authors: Eric Matt
# Book ID: B1002, Title: Learning SQL, Authors: Alan Beaulieu, C
# Book ID: B1003, Title: Clean Code, Authors: Robert C. Martin, 
# Book ID: B1004, Title: Fluent Python, Authors: Luciano Ramalho
# Book ID: B1005, Title: Head First Design Patterns, Authors: Er
# Book ID: B1006, Title: The Pragmatic Programmer, Authors: Andr
# Book ID: B1007, Title: Automate the Boring Stuff, Authors: Al 
# Book ID: B1008, Title: Database System Concepts, Authors: Henr
# Book ID: B1009, Title: Operating System Concepts, Authors: Sil
# Book ID: B1010, Title: Introduction to Algorithms, Authors: CL
# Book ID: B1011, Title: Java Complete Reference, Authors: Herbe
# Book ID: B1012, Title: Effective Java, Authors: Joshua Bloch, 
# Book ID: B1013, Title: Java Concurrency in Practice, Authors: 
# Book ID: B1014, Title: You Don't Know JS, Authors: Kyle Simpso
# Book ID: B1015, Title: Eloquent JavaScript, Authors: Marijn Ha
# Book ID: B1016, Title: HTML & CSS, Authors: Jon Duckett, Copie
# Book ID: B1017, Title: Designing Data-Intensive Applications, 
# Book ID: B1018, Title: Deep Learning, Authors: Ian Goodfellow,
# Book ID: B1019, Title: Hands-On Machine Learning, Authors: Aur
# Book ID: B1020, Title: Introduction to Machine Learning, Autho
# Book ID: B1021, Title: Reinforcement Learning, Authors: Sutton
# Book ID: B1022, Title: Compilers: Principles Techniques and To
# Book ID: B1023, Title: Computer Networks, Authors: Tanenbaum, 
# Book ID: B1024, Title: Distributed Systems, Authors: Maarten v
# Book ID: B1025, Title: Big Data Fundamentals, Authors: Thomas 
# Book ID: B1026, Title: Data Engineering with Python, Authors: 
# Book ID: B1027, Title: Kafka: The Definitive Guide, Authors: G
# Book ID: B1028, Title: Spark: The Definitive Guide, Authors: B
# Book ID: B1029, Title: NoSQL Distilled, Authors: Pramod Sadala
# Book ID: B1030, Title: Learning Docker, Authors: Pethuru Raj, 
# Book ID: B1031, Title: Kubernetes in Action, Authors: Marko Lu
# Book ID: B1032, Title: Terraform Up & Running, Authors: Yevgen
# Book ID: B1033, Title: CI/CD with Jenkins, Authors: Christophe
# Book ID: B1034, Title: Cloud Architecture Patterns, Authors: B
# Book ID: B1035, Title: Azure for Architects, Authors: John Sav
# Book ID: B1036, Title: AWS Certified Solutions Architect, Auth
# Book ID: B1037, Title: GCP Architecture Framework, Authors: Go
# Book ID: B1038, Title: Data Visualization with Python, Authors
# Book ID: B1039, Title: SQL for Data Analysis, Authors: Boris P
# Book ID: B1040, Title: Introduction to Statistics, Authors: Ro
# Book ID: 41, Title: The IT Industry, Authors: Chuck Cliburn, C
# Book ID: B1042, Title: The International CTO , Authors: David 
# Book ID: B1043, Title: AWS Solutions, Authors: John legend, Da
# Book ID: B1044, Title: Tech solutions, Authors: Ron Larsan, Co
# Book ID: B1046, Title: DATA CLOUD Engineering, Authors: Chuck 

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: B1042
# Please enter a valid number.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 1
# Book ID: B1047
# Title: Generative AI and uses
# Authors (comma separated): Henry Korth
# ISBN: 9837528456
# Tags (comma separated): genai|gpt
# Total Copies: 5
# Book 'Generative AI and uses' added successfully.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 2
# Book ID to delete (soft): B1044
# Book 'Tech solutions' soft-deleted.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 11

# Available Books:
# Book ID: B1001, Title: Python Crash Course, Authors: Eric Matt
# Book ID: B1002, Title: Learning SQL, Authors: Alan Beaulieu, C
# Book ID: B1003, Title: Clean Code, Authors: Robert C. Martin, 
# Book ID: B1004, Title: Fluent Python, Authors: Luciano Ramalho
# Book ID: B1005, Title: Head First Design Patterns, Authors: Er
# Book ID: B1006, Title: The Pragmatic Programmer, Authors: Andr
# Book ID: B1007, Title: Automate the Boring Stuff, Authors: Al 
# Book ID: B1008, Title: Database System Concepts, Authors: Henr
# Book ID: B1009, Title: Operating System Concepts, Authors: Sil
# Book ID: B1010, Title: Introduction to Algorithms, Authors: CL
# Book ID: B1011, Title: Java Complete Reference, Authors: Herbe
# Book ID: B1012, Title: Effective Java, Authors: Joshua Bloch, 
# Book ID: B1013, Title: Java Concurrency in Practice, Authors: 
# Book ID: B1014, Title: You Don't Know JS, Authors: Kyle Simpso
# Book ID: B1015, Title: Eloquent JavaScript, Authors: Marijn Ha
# Book ID: B1016, Title: HTML & CSS, Authors: Jon Duckett, Copie
# Book ID: B1017, Title: Designing Data-Intensive Applications, 
# Book ID: B1018, Title: Deep Learning, Authors: Ian Goodfellow,
# Book ID: B1019, Title: Hands-On Machine Learning, Authors: Aur
# Book ID: B1020, Title: Introduction to Machine Learning, Autho
# Book ID: B1021, Title: Reinforcement Learning, Authors: Sutton
# Book ID: B1022, Title: Compilers: Principles Techniques and To
# Book ID: B1023, Title: Computer Networks, Authors: Tanenbaum, 
# Book ID: B1024, Title: Distributed Systems, Authors: Maarten v
# Book ID: B1025, Title: Big Data Fundamentals, Authors: Thomas 
# Book ID: B1026, Title: Data Engineering with Python, Authors: 
# Book ID: B1027, Title: Kafka: The Definitive Guide, Authors: G
# Book ID: B1028, Title: Spark: The Definitive Guide, Authors: B
# Book ID: B1029, Title: NoSQL Distilled, Authors: Pramod Sadala
# Book ID: B1030, Title: Learning Docker, Authors: Pethuru Raj, 
# Book ID: B1031, Title: Kubernetes in Action, Authors: Marko Lu
# Book ID: B1032, Title: Terraform Up & Running, Authors: Yevgen
# Book ID: B1033, Title: CI/CD with Jenkins, Authors: Christophe
# Book ID: B1034, Title: Cloud Architecture Patterns, Authors: B
# Book ID: B1035, Title: Azure for Architects, Authors: John Sav
# Book ID: B1036, Title: AWS Certified Solutions Architect, Auth
# Book ID: B1037, Title: GCP Architecture Framework, Authors: Go
# Book ID: B1038, Title: Data Visualization with Python, Authors
# Book ID: B1039, Title: SQL for Data Analysis, Authors: Boris P
# Book ID: B1040, Title: Introduction to Statistics, Authors: Ro
# Book ID: 41, Title: The IT Industry, Authors: Chuck Cliburn, C
# Book ID: B1042, Title: The International CTO , Authors: David 
# Book ID: B1043, Title: AWS Solutions, Authors: John legend, Da
# Book ID: B1046, Title: DATA CLOUD Engineering, Authors: Chuck 
# Book ID: B1047, Title: Generative AI and uses, Authors: Henry 

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 3
# Book ID to restore: B1044
# Book 'Tech solutions' restored.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 11

# Available Books:
# Book ID: B1001, Title: Python Crash Course, Authors: Eric Matt
# Book ID: B1002, Title: Learning SQL, Authors: Alan Beaulieu, C
# Book ID: B1003, Title: Clean Code, Authors: Robert C. Martin, 
# Book ID: B1004, Title: Fluent Python, Authors: Luciano Ramalho
# Book ID: B1005, Title: Head First Design Patterns, Authors: Er
# Book ID: B1006, Title: The Pragmatic Programmer, Authors: Andr
# Book ID: B1007, Title: Automate the Boring Stuff, Authors: Al 
# Book ID: B1008, Title: Database System Concepts, Authors: Henr
# Book ID: B1009, Title: Operating System Concepts, Authors: Sil
# Book ID: B1010, Title: Introduction to Algorithms, Authors: CL
# Book ID: B1011, Title: Java Complete Reference, Authors: Herbe
# Book ID: B1012, Title: Effective Java, Authors: Joshua Bloch, 
# Book ID: B1013, Title: Java Concurrency in Practice, Authors: 
# Book ID: B1014, Title: You Don't Know JS, Authors: Kyle Simpso
# Book ID: B1015, Title: Eloquent JavaScript, Authors: Marijn Ha
# Book ID: B1016, Title: HTML & CSS, Authors: Jon Duckett, Copie
# Book ID: B1017, Title: Designing Data-Intensive Applications, 
# Book ID: B1018, Title: Deep Learning, Authors: Ian Goodfellow,
# Book ID: B1019, Title: Hands-On Machine Learning, Authors: Aur
# Book ID: B1020, Title: Introduction to Machine Learning, Autho
# Book ID: B1021, Title: Reinforcement Learning, Authors: Sutton
# Book ID: B1022, Title: Compilers: Principles Techniques and To
# Book ID: B1023, Title: Computer Networks, Authors: Tanenbaum, 
# Book ID: B1024, Title: Distributed Systems, Authors: Maarten v
# Book ID: B1025, Title: Big Data Fundamentals, Authors: Thomas 
# Book ID: B1026, Title: Data Engineering with Python, Authors: 
# Book ID: B1027, Title: Kafka: The Definitive Guide, Authors: G
# Book ID: B1028, Title: Spark: The Definitive Guide, Authors: B
# Book ID: B1029, Title: NoSQL Distilled, Authors: Pramod Sadala
# Book ID: B1030, Title: Learning Docker, Authors: Pethuru Raj, 
# Book ID: B1031, Title: Kubernetes in Action, Authors: Marko Lu
# Book ID: B1032, Title: Terraform Up & Running, Authors: Yevgen
# Book ID: B1033, Title: CI/CD with Jenkins, Authors: Christophe
# Book ID: B1034, Title: Cloud Architecture Patterns, Authors: B
# Book ID: B1035, Title: Azure for Architects, Authors: John Sav
# Book ID: B1036, Title: AWS Certified Solutions Architect, Auth
# Book ID: B1037, Title: GCP Architecture Framework, Authors: Go
# Book ID: B1038, Title: Data Visualization with Python, Authors
# Book ID: B1039, Title: SQL for Data Analysis, Authors: Boris P
# Book ID: B1040, Title: Introduction to Statistics, Authors: Ro
# Book ID: 41, Title: The IT Industry, Authors: Chuck Cliburn, C
# Book ID: B1042, Title: The International CTO , Authors: David 
# Book ID: B1043, Title: AWS Solutions, Authors: John legend, Da
# Book ID: B1044, Title: Tech solutions, Authors: Ron Larsan, Co
# Book ID: B1046, Title: DATA CLOUD Engineering, Authors: Chuck 
# Book ID: B1047, Title: Generative AI and uses, Authors: Henry 

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 4
# Book ID to update: B1044
# Current details:
# - Title: Tech solutions
# - Authors: Ron Larsan
# - ISBN: 9897654637
# - Tags: cloud, dsa
# - Total Copies: 2
# - Available Copies: 2
# - Deleted: False
# New Title (leave blank to keep): TECH SOLUTIONS
# New Authors (comma separated, leave blank to keep): Ron Larsan
# New ISBN (leave blank to keep): 9876354637
# New Tags (comma separated, leave blank to keep): cloud|data
# New Total Copies (leave blank to keep): 4
# Book updated successfully.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 5
# User ID: U2029
# Name: Ravi 
# Email: ravi@example.com
# Status (active/inactive/banned): inactive
# Max Loans: 2
# Password: ravi
# User ID already exists.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 5
# User ID: U2030
# Name: Ravi
# Email: ravi@example.com
# Status (active/inactive/banned): active
# Max Loans: 3
# Password: ravi 
# User added successfully.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 6
# User ID to update: U2027
# Current details:
# - Name: John
# - Email: john@example.com
# - Status: active
# - Max Loans: 1
# - Active Loans: 0
# New Name (leave blank to keep): John Jeffry
# New Email (leave blank to keep): john@example.com
# New Status (active/inactive/banned, leave blank to keep): acti
# New Max Loans (leave blank to keep): 2
# New Password (leave blank to keep): john        
# User updated successfully.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 7
# Book ID: B1047
# Borrow successful. Transaction ID: T30. Due Date: 30-11-2025.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 7
# Book ID: B1047
# You have already borrowed this book and not returned it yet.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 8
# Transaction ID: B1047
# Transaction not found!

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 8
# Transaction ID: T30
# Return successful.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 9
# Transaction ID: T3001, User ID: U2001, Book ID: B1001, Due Dat
# Transaction ID: T3004, User ID: U2005, Book ID: B1004, Due Dat
# Transaction ID: T3007, User ID: U2010, Book ID: B1028, Due Dat
# Transaction ID: T3008, User ID: U2013, Book ID: B1038, Due Dat
# Transaction ID: T3010, User ID: U2015, Book ID: B1033, Due Dat
# Transaction ID: T3012, User ID: U2018, Book ID: B1035, Due Dat
# Transaction ID: T3014, User ID: U2020, Book ID: B1019, Due Dat
# Transaction ID: T3016, User ID: U2023, Book ID: B1017, Due Dat
# Transaction ID: T3018, User ID: U2025, Book ID: B1012, Due Dat
# Transaction ID: T3019, User ID: U2009, Book ID: B1005, Due Dat
# Transaction ID: T21, User ID: U2019, Book ID: B1032, Due Date:
# Transaction ID: T22, User ID: U2027, Book ID: B1043, Due Date:
# Transaction ID: T23, User ID: U2020, Book ID: B1043, Due Date:
# Transaction ID: T24, User ID: U2020, Book ID: B1044, Due Date:
# Transaction ID: T25, User ID: U2020, Book ID: B1043, Due Date:
# Transaction ID: T27, User ID: U2020, Book ID: B1045, Due Date:
# Transaction ID: T29, User ID: U2028, Book ID: B1046, Due Date:

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 10
# No overdue loans.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 10
# No overdue loans.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 12
# All data saved to CSV successfully.

# Library Management System
# Please choose an option (type the number):
# 1. Add a Book
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 13

# Commands:
#   1. Add a Book
#   2. Soft Delete a Book
#   3. Restore a Book
#   4. Update a Book
#   5. Add a User
#   6. Update a User
#   7. Borrow a Book (requires login)
#   8. Return a Book (requires login)
#   9. View Active Loans
#   10. View Overdue Loans
#   11. View Available Books
#   12. Save Data
#   13. Help
#   14. Exit


# Library Management System
# Please choose an option (type the number):
# 2. Soft Delete a Book
# 3. Restore a Book
# 4. Update a Book
# 5. Add a User
# 6. Update a User
# 7. Borrow a Book
# 8. Return a Book
# 9. View Active Loans
# 10. View Overdue Loans
# 11. View Available Books
# 12. Save Data
# 13. Help
# 14. Exit

# Enter the number of your choice: 14
# All data saved to CSV successfully.
# Exiting the program.
