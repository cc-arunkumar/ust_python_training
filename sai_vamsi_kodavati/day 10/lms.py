# Assessment: Library Management System

# Detailed Technical Requirements
# 1. Overview & Scope
# You will build a Command-Line Library Management System (LMS) using:
# Object-Oriented Programming
# Exception Handling (already covered in training)
# CSV-based storage
# Clean and simple CLI interface
# Modular design


# System must support:
# Managing Books
# Managing Users
# Borrow/Return functionality
# Searching & basic reporting
# Persistent storage using CSV file


# Importing models and utilities
from models import Book, User
from library import Library
from utils import print_book, print_user, print_tx

# ------------------- AUTHENTICATION -------------------
# Function to authenticate a user before allowing certain actions
def authenticate_user(library, user_id):
    user = library.get_user(user_id)  # Retrieve user object by ID
    if not user:
        print("User not found.")
        return False

    # Simple password check (password = user_id)
    password_user = input("Enter Password (same as User ID): ")
    if password_user != user_id:
        print("Incorrect password.")
        return False

    return True


# ------------------- EMAIL VALIDATION -------------------
import re

# Function to validate email format using regex
def get_valid_email(prompt=" Email:"):
    # Regex pattern for common valid email formats
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email = input(prompt).strip()
        if re.match(pattern, email):
            return email
        print("Invalid email. Please enter a valid email address (e.g., user@example.com).")


# ------------------- MAIN LMS PROGRAM -------------------
def main():
    library = Library()  

    print("\n Welcome to Library Management System (CLI)\n")

    # ------------------- MAIN MENU LOOP -------------------
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Books")
        print("2. Users")
        print("3. Borrow / Return")
        print("4. Loans")
        print("5. Reports")
        print("6. Save Data")
        print("7. Exit")
        print("===============================")

        choice = input("Enter choice (1-7): ")

        # ------------------- BOOKS MENU -------------------
        match choice:
            case "1":
                while True:
                    print("\n------ BOOKS MENU ------")
                    print("A. Add Book")
                    print("B. Update Book")
                    print("C. Remove Book")
                    print("D. Get Book")
                    print("E. List Books")
                    print("F. Search Books")
                    print("G. Back to main menu")
                    print("------------------------")

                    book_choice = input("Choice: ").lower()

                    match book_choice:

                        # ------------ Add Book ------------
                        case "a":
                            try:
                                book_id = input("Book ID: ")
                                title = input("Title of the Book: ")
                                authors = input("Author of the Book: ")
                                isbn = input("ISBN (International Standard Book Number): ")
                                tags = input("Tags: ")
                                total = int(input("Total Copies: "))

                                # Book model requires available copies as well
                                available = total

                                book = Book(
                                    book_id, title, authors,
                                    isbn, tags, total, available
                                )

                                # Add book to library
                                library.add_book(book) 
                                print("Book added successfully.")

                            except Exception as e:
                                print("Please enter a value to add.", e)

                        # ------------ Update Book ------------
                        case "b":
                            book_id = input("Book ID to update: ")
                            book = library.get_book(book_id)

                            if not book:
                                print(" Book not found.")
                                continue

                            # Get updated values or use existing ones
                            title = input(f"Title of the Book [{book.title}]: ") or book.title
                            authors_raw = input(f"Authors [{', '.join(book.authors)}]: ")
                            authors = authors_raw if authors_raw else book.authors
                            isbn = input(f"ISBN [{book.isbn}]: ") or book.isbn
                            tags_raw = input(f"Tags [{', '.join(book.tags)}]: ")
                            tags = tags_raw if tags_raw else book.tags
                            total_raw = input(f"Total Copies [{book.total_copies}]: ")
                            total = int(total_raw) if total_raw else book.total_copies

                            try:
                                book.update(
                                    title=title,
                                    authors=authors,
                                    isbn=isbn,
                                    tags=tags,
                                    total_copies=total,
                                )
                                print(" Book updated Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Remove Book ------------
                        case "c":
                            try:
                                book_id = input("Book ID to remove: ")
                                library.remove_book(book_id)
                                print(" Book removed Successfully.")
                            except Exception as e:
                                print(" Error:", e)

                        # ------------ Get Book ------------
                        case "d":
                            book_id = input("Book ID: ")
                            book_get = library.get_book(book_id)
                            if book_get:
                                print_book(book_get)
                            else:
                                print(" Book not found.")

                        # ------------ List Books ------------
                        case "e":
                            for book_get in library.list_books():
                                print_book(book_get)

                        # ------------ Search Books ------------
                        case "f":
                            print("Search By:")
                            print("1. Title of the book")
                            print("2. Author of the book")
                            print("3. Tag of the book")
                            search_choice = input("Enter your Choice: ")

                            match search_choice:
                                case "1":
                                    text = input("Enter the title of the book: ")
                                    results = library.search_books_by_title(text)
                                case "2":
                                    text = input("Enter the author's name: ")
                                    results = library.search_books_by_author(text)
                                case "3":
                                    text = input("Enter the tag of the book: ")
                                    results = library.search_books_by_tag(text)
                                case _:
                                    print("Invalid selection.")
                                    continue

                            # Display search results
                            for book_choice in results:
                                print_book(book_choice)

                        # Back to main menu
                        case "g":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- USERS MENU -------------------
            case "2":
                while True:
                    print("\n------ USERS MENU ------")
                    print("A. Add User")
                    print("B. Update User")
                    print("C. Get User")
                    print("D. List Users")
                    print("E. Activate user")
                    print("F. Deactivate user")
                    print("G. Ban user")
                    print("H. Back to main menu")
                    print("------------------------")

                    user_choice = input("Choice: ").lower()

                    match user_choice:
                        # ------------ Add User ------------
                        case "a":
                            try:
                                user_id = input("User ID: ")
                                name = input("User Name: ")
                                # Validate email
                                email = get_valid_email()  
                                user = User(user_id, name, email)
                                library.add_user(user)
                                print(" User added Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Update User ------------
                        case "b":
                            user_id = input("User ID: ")

                            if not authenticate_user(library, user_id):
                                continue

                            user = library.get_user(user_id)
                            if not user:
                                print(" User not found.")
                                continue

                            name = input(f"Name [{user.name}]: ") or user.name
                            email = input(f"Email [{user.email}]: ") or user.email  

                            try:
                                library.update_user(user_id, name=name, email=email)
                                print("User updated Successfully.")
                            except Exception as e:
                                print("Error:", e)

                        # ------------ Get User ------------
                        case "c":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                user = library.get_user(user_id)
                                if user:
                                    print_user(user)
                                else:
                                    print("User not found.")

                        # ------------ List Users ------------
                        case "d":
                            for u1 in library.list_users():
                                print_user(u1)

                        # ------------ Activate User ------------
                        case "e":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.activate_user(user_id)
                                print("User Activated Successfully.")

                        # ------------ Deactivate User ------------
                        case "f":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.deactivate_user(user_id)
                                print("User Deactivated Successfully.")

                        # ------------ Ban User ------------
                        case "g":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                library.ban_user(user_id)
                                print("User Banned.")

                        # Back to main menu
                        case "h":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- BORROW / RETURN MENU -------------------
            case "3":
                while True:
                    print("\n------ BORROW / RETURN ------")
                    print("A. Borrow Book")
                    print("B. Return Book")
                    print("C. Back")
                    print("-----------------------------")

                    borrow_choice = input("Choice: ").lower()

                    match borrow_choice:
                        # ------------ Borrow Book ------------
                        case "a":
                            user_id = input("User ID: ")
                            if not authenticate_user(library, user_id):
                                continue
                            book_id = input("Book ID: ")

                            try:
                                tx, due = library.borrow_book(user_id, book_id)
                                print("Borrow successful.")
                                print_tx(tx)
                            except Exception as e:
                                print(" Error:", e)

                        # ------------ Return Book ------------
                        case "b":
                            tx_id = input("Transaction ID: ")

                            try:
                                tx = library.return_book(tx_id)
                                print("Return successful.")
                                print_tx(tx)
                            except Exception as e:
                                print(" Error:", e)

                        # Back to previous menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- LOANS MENU -------------------
            case "4":
                while True:
                    print("\n------ LOANS MENU ------")
                    print("A. Active Loans")
                    print("B. Overdue Loans")
                    print("C. Back to main menu")
                    print("------------------------")

                    loan_choice = input("Choice: ").lower()

                    match loan_choice:
                        # Show all active loans
                        case "a":
                            loans = library.get_active_loans()
                            for tx in loans:
                                print_tx(tx)

                        # Show overdue loans
                        case "b":
                            overdue = library.get_overdue_loans()
                            if overdue:
                                for tx in overdue:
                                    print_tx(tx)
                            else:
                                print("No overdue loans at the moment.")

                        # Back to main menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- REPORTS MENU -------------------
            case "5":
                while True:
                    print("\n------ REPORTS MENU ------")
                    print("A. Summary Report")
                    print("B. User Loan History")
                    print("C. Back to main menu")
                    print("--------------------------")

                    report_choice = input("Choice: ").lower()

                    match report_choice:
                        # Summary report of library stats
                        case "a":
                            book_choice, u, a, o = library.summary_report()
                            print(f"""
------- SUMMARY REPORT -------
Total Books     : {book_choice}
Total Users     : {u}
Active Loans    : {a}
Overdue Loans   : {o}
------------------------------
""")

                        # Show specific user's loan history
                        case "b":
                            user_id = input("User ID: ")
                            if authenticate_user(library, user_id):
                                for tx in library.get_user_loans(user_id):
                                    print_tx(tx)

                        # Back to main menu
                        case "c":
                            break

                        case _:
                            print("Invalid choice.")

            # ------------------- SAVE DATA -------------------
            case "6":
                library.save_all()
                print("Data saved successfully.")

            # ------------------- EXIT PROGRAM -------------------
            case "7":
                print("Exiting LMS. Thank You!")
                break

            case _:
                print("Invalid choice! Enter 1-7.")


# ------------------- RUN PROGRAM -------------------
if __name__ == "__main__":
    main()



#  Welcome to Library Management System (CLI)


# ========== MAIN MENU ==========
# 1. Books
# 2. Users
# 3. Borrow / Return
# 4. Loans
# 5. Reports
# 6. Save Data
# 7. Exit
# ===============================
# Enter choice (1-7): 1

# ------ BOOKS MENU ------
# A. Add Book
# B. Update Book
# C. Remove Book
# D. Get Book
# E. List Books
# F. Search Books
# G. Back to main menu
# ------------------------
# Choice: a
# Book ID: B101
# Title of the Book: Ust Python
# Author of the Book: Arun 
# ISBN (International Standard Book Number): 1796419637
# Tags: Python|Sql
# Total Copies: 3
# Book added successfully.

# ------ BOOKS MENU ------
# A. Add Book
# B. Update Book
# C. Remove Book
# D. Get Book
# E. List Books
# F. Search Books
# G. Back to main menu
# ------------------------
# Choice: b
# Book ID to update: B1003
# Title of the Book [Clean Code]: Clean Code
# Authors [Robert C. Martin]: Robert C. Martin
# ISBN [9780132350884]: 9780132350885
# Tags [software, clean-code, programming]: software,programming
# Total Copies [4]: 4
#  Book updated Successfully.

# ------ BOOKS MENU ------
# A. Add Book
# B. Update Book
# C. Remove Book
# D. Get Book
# E. List Books
# F. Search Books
# G. Back to main menu
# ------------------------
# Choice: e

# --- BOOK ---
# Book ID             : B1001
# Book Title          : Python Crash Course
# Authors of the book : Eric Matthes
# ISBN                : 9781593279288
# Tags                : python, beginner, programming
# Total Copies        : 5
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1002
# Book Title          : Learning SQL
# Authors of the book : Alan Beaulieu
# ISBN                : 9780596520830
# Tags                : sql, database, beginner
# Total Copies        : 4
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1003
# Book Title          : Clean Code
# Authors of the book : Robert C. Martin
# ISBN                : 9780132350885
# Tags                : software,programming
# Total Copies        : 4
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1004
# Book Title          : Fluent Python
# Authors of the book : Luciano Ramalho
# ISBN                : 9781491946008
# Tags                : python, advanced, programming
# Total Copies        : 3
# Available Copies    : 1
# --------------

# --- BOOK ---
# Book ID             : B1005
# Book Title          : Head First Design Patterns
# Authors of the book : Eric Freeman
# ISBN                : 9780596007126
# Tags                : design-patterns, oop, architecture
# Total Copies        : 3
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1006
# Book Title          : The Pragmatic Programmer
# Authors of the book : Andrew Hunt
# ISBN                : 9780201616224
# Tags                : software, best-practices
# Total Copies        : 5
# Available Copies    : 5
# --------------

# --- BOOK ---
# Book ID             : B1007
# Book Title          : Automate the Boring Stuff
# Authors of the book : Al Sweigart
# ISBN                : 9781593275990
# Tags                : automation, python, beginner
# Total Copies        : 6
# Available Copies    : 5
# --------------

# --- BOOK ---
# Book ID             : B1008
# Book Title          : Database System Concepts
# Authors of the book : Henry Korth
# ISBN                : 9780078022159
# Tags                : database, dbms, theory
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1009
# Book Title          : Operating System Concepts
# Authors of the book : Silberschatz
# ISBN                : 9781118063330
# Tags                : os, theory, system
# Total Copies        : 3
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1010
# Book Title          : Introduction to Algorithms
# Authors of the book : CLRS
# ISBN                : 9780262032933
# Tags                : algorithms, dsa, competitive
# Total Copies        : 5
# Available Copies    : 5
# --------------

# --- BOOK ---
# Book ID             : B1011
# Book Title          : Java Complete Reference
# Authors of the book : Herbert Schildt
# ISBN                : 9781260440232
# Tags                : java, programming, reference
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1012
# Book Title          : Effective Java
# Authors of the book : Joshua Bloch
# ISBN                : 9780134685991
# Tags                : java, clean-code, software
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1013
# Book Title          : Java Concurrency in Practice
# Authors of the book : Brian Goetz
# ISBN                : 9780321349606
# Tags                : java, concurrency, advanced
# Total Copies        : 2
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1014
# Book Title          : You Don't Know JS
# Authors of the book : Kyle Simpson
# ISBN                : 9781491904244
# Tags                : javascript, web, programming
# Total Copies        : 5
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1015
# Book Title          : Eloquent JavaScript
# Authors of the book : Marijn Haverbeke
# ISBN                : 9781593279509
# Tags                : javascript, web, beginner
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1016
# Book Title          : HTML & CSS
# Authors of the book : Jon Duckett
# ISBN                : 9781118008188
# Tags                : web, design, frontend
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1017
# Book Title          : Designing Data-Intensive Applications
# Authors of the book : Martin Kleppmann
# ISBN                : 9781449373320
# Tags                : systems, distributed, architecture
# Total Copies        : 4
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1018
# Book Title          : Deep Learning
# Authors of the book : Ian Goodfellow
# ISBN                : 9780262035613
# Tags                : ai, ml, deep-learning
# Total Copies        : 3
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1019
# Book Title          : Hands-On Machine Learning
# Authors of the book : Aurelien Geron
# ISBN                : 9781492032649
# Tags                : ml, python, ai
# Total Copies        : 4
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1020
# Book Title          : Introduction to Machine Learning
# Authors of the book : Alpaydin
# ISBN                : 9780262028189
# Tags                : ml, theory, data
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1021
# Book Title          : Reinforcement Learning
# Authors of the book : Sutton & Barto
# ISBN                : 9780262039246
# Tags                : rl, ai, advanced
# Total Copies        : 2
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1022
# Book Title          : Compilers: Principles Techniques and Tools
# Authors of the book : Aho & Ullman
# ISBN                : 9780321486813
# Tags                : compiler, theory
# Total Copies        : 2
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1023
# Book Title          : Computer Networks
# Authors of the book : Tanenbaum
# ISBN                : 9780132126953
# Tags                : networks, theory, system
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1024
# Book Title          : Distributed Systems
# Authors of the book : Maarten van Steen
# ISBN                : 9781543057386
# Tags                : distributed, systems, theory
# Total Copies        : 3
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1025
# Book Title          : Big Data Fundamentals
# Authors of the book : Thomas Erl
# ISBN                : 9780134291079
# Tags                : big-data, data-engineering
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1026
# Book Title          : Data Engineering with Python
# Authors of the book : Paul Crickard
# ISBN                : 9781789535365
# Tags                : data-engineering, python
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1027
# Book Title          : Kafka: The Definitive Guide
# Authors of the book : Gwen Shapira
# ISBN                : 9781491936160
# Tags                : data-streaming, kafka
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1028
# Book Title          : Spark: The Definitive Guide
# Authors of the book : Bill Chambers
# ISBN                : 9781491912218
# Tags                : big-data, spark
# Total Copies        : 3
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1029
# Book Title          : NoSQL Distilled
# Authors of the book : Pramod Sadalage
# ISBN                : 9780132983716
# Tags                : database, nosql, theory
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1030
# Book Title          : Learning Docker
# Authors of the book : Pethuru Raj
# ISBN                : 9781784397937
# Tags                : devops, docker, containers
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1031
# Book Title          : Kubernetes in Action
# Authors of the book : Marko Luksa
# ISBN                : 9781617293726
# Tags                : devops, kubernetes, orchestration
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1032
# Book Title          : Terraform Up & Running
# Authors of the book : Yevgeniy Brikman
# ISBN                : 9781492046903
# Tags                : devops, infrastructure
# Total Copies        : 2
# Available Copies    : 2
# --------------

# --- BOOK ---
# Book ID             : B1033
# Book Title          : CI/CD with Jenkins
# Authors of the book : Christopher Grant
# ISBN                : 9781787287600
# Tags                : devops, cicd, automation
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1034
# Book Title          : Cloud Architecture Patterns
# Authors of the book : Bill Wilder
# ISBN                : 9781449319779
# Tags                : cloud, architecture, patterns
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1035
# Book Title          : Azure for Architects
# Authors of the book : John Savill
# ISBN                : 9781119559535
# Tags                : cloud, azure, architecture
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1036
# Book Title          : AWS Certified Solutions Architect
# Authors of the book : Ben Piper
# ISBN                : 9781119504214
# Tags                : cloud, aws, certification
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1037
# Book Title          : GCP Architecture Framework
# Authors of the book : Google Press
# ISBN                : 9781098112934
# Tags                : cloud, gcp, architecture
# Total Copies        : 3
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1038
# Book Title          : Data Visualization with Python
# Authors of the book : Kirill Eremenko
# ISBN                : 9781788295758
# Tags                : data, visualization, python
# Total Copies        : 4
# Available Copies    : 3
# --------------

# --- BOOK ---
# Book ID             : B1039
# Book Title          : SQL for Data Analysis
# Authors of the book : Boris Paskhaver
# ISBN                : 9781492072261
# Tags                : data, sql, analytics
# Total Copies        : 4
# Available Copies    : 4
# --------------

# --- BOOK ---
# Book ID             : B1040
# Book Title          : Introduction to Statistics
# Authors of the book : Ron Larson
# ISBN                : 9780321912749
# Tags                : math, statistics, probability
# Total Copies        : 5
# Available Copies    : 5
# --------------

# --- BOOK ---
# Book ID             : B101
# Book Title          : Ust Python
# Authors of the book : Arun
# ISBN                : 1796419637
# Tags                : Python|Sql
# Total Copies        : 3
# Available Copies    : 3
# --------------

# ------ BOOKS MENU ------
# A. Add Book
# B. Update Book
# C. Remove Book
# D. Get Book
# E. List Books
# F. Search Books
# G. Back to main menu
# ------------------------
# Choice: g

# ========== MAIN MENU ==========
# 1. Books
# 2. Users
# 3. Borrow / Return
# 4. Loans
# 5. Reports
# 6. Save Data
# 7. Exit
# ===============================
# Enter choice (1-7): 2

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: 1
# Invalid choice.

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: a
# User ID: U2036
# User Name: Niranjan
#  Email:niru@gmail.com
#  User added Successfully.

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: b
# User ID: U2002
# Enter Password (same as User ID): U2002
# Name [Riya Sharma]: RIya
# Email [riya.sharma@ust.com]: riya.sharma@ust.com
# User updated Successfully.

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: e
# User ID: U2002
# Enter Password (same as User ID): U2002
# User Activated Successfully.

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: g
# User ID: U2003
# Enter Password (same as User ID): U2003
# User Banned.

# ------ USERS MENU ------
# A. Add User
# B. Update User
# C. Get User
# D. List Users
# E. Activate user
# F. Deactivate user
# G. Ban user
# H. Back to main menu
# ------------------------
# Choice: h

# ========== MAIN MENU ==========
# 1. Books
# 2. Users
# 3. Borrow / Return
# 4. Loans
# 5. Reports
# 6. Save Data
# 7. Exit
# ===============================
# Enter choice (1-7): 4

# ------ LOANS MENU ------
# A. Active Loans
# B. Overdue Loans
# C. Back to main menu
# ------------------------
# Choice: a

# --- TRANSACTION ---
# Transaction ID      : T3001
# Book ID             : B1001
# User ID             : U2001
# Borrowed date       : 2025-10-01
# Due Date            : 2025-10-15
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3004
# Book ID             : B1004
# User ID             : U2005
# Borrowed date       : 2025-11-01
# Due Date            : 2025-11-15
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3007
# Book ID             : B1028
# User ID             : U2010
# Borrowed date       : 2025-11-05
# Due Date            : 2025-11-19
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3008
# Book ID             : B1038
# User ID             : U2013
# Borrowed date       : 2025-11-06
# Due Date            : 2025-11-20
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3010
# Book ID             : B1033
# User ID             : U2015
# Borrowed date       : 2025-11-07
# Due Date            : 2025-11-21
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3012
# Book ID             : B1035
# User ID             : U2018
# Borrowed date       : 2025-11-08
# Due Date            : 2025-11-22
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3014
# Book ID             : B1019
# User ID             : U2020
# Borrowed date       : 2025-11-01
# Due Date            : 2025-11-15
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3016
# Book ID             : B1017
# User ID             : U2023
# Borrowed date       : 2025-11-03
# Due Date            : 2025-11-17
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3018
# Book ID             : B1012
# User ID             : U2025
# Borrowed date       : 2025-11-04
# Due Date            : 2025-11-18
# Returned date       : None
# Status              : borrowed
# --------------------

# --- TRANSACTION ---
# Transaction ID      : T3019
# Book ID             : B1005
# User ID             : U2009
# Borrowed date       : 2025-11-05
# Due Date            : 2025-11-19
# Returned date       : None
# Status              : borrowed
# --------------------

# ------ LOANS MENU ------
# A. Active Loans
# B. Overdue Loans
# C. Back to main menu
# ------------------------
# Choice: c

# ========== MAIN MENU ==========
# 1. Books
# 2. Users
# 3. Borrow / Return
# 4. Loans
# 5. Reports
# 6. Save Data
# 7. Exit
# ===============================
# Enter choice (1-7): 5

# ------ REPORTS MENU ------
# A. Summary Report
# B. User Loan History
# C. Back to main menu
# --------------------------
# Choice: a

# ------- SUMMARY REPORT -------
# Total Books     : 41
# Total Users     : 26
# Active Loans    : 10
# Overdue Loans   : 0
# ------------------------------


# ------ REPORTS MENU ------
# A. Summary Report
# B. User Loan History
# C. Back to main menu
# --------------------------
# Choice: c

# ========== MAIN MENU ==========
# 1. Books
# 2. Users
# 3. Borrow / Return
# 4. Loans
# 5. Reports
# 6. Save Data
# 7. Exit
# ===============================
# Enter choice (1-7): 7
# Exiting LMS. Thank You!