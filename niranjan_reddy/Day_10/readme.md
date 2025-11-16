Library Management System (LMS)

A simple, menu-based command-line program that allows you to manage books, library members, and borrowing records.
Everything is stored in easy-to-read CSV files so your data stays saved even after closing the program.
________________________________________

What This System Can Do

Book Management
•	Add new books
•	Update book details
•	View all books
•	Search by title, author, or tag
•	Remove books

User Management
•	Add new users
•	Update user information
•	Activate, deactivate, or ban users
•	View all users
•	See a user’s borrowing history

Borrowing & Returning
•	Borrow a book (with automatic due date)
•	Return a book
•	Track active and overdue loans

Data Handling
•	All data is stored in CSV text files
•	Automatically loads everything when the program starts
•	You can save all data anytime through the menu
________________________________________

Before You Start
You only need:
->Python 3.x
->No third-party libraries
To check your version:
python --version
________________________________________

How to Run the Program
1.	Open your terminal or command prompt
2.	Navigate to the project folder
3.	Run:

python lms.py
The program will start and show the main menu.
________________________________________

Main Menu Overview
When the program starts, you will see:
1. Books
2. Users
3. Borrow / Return
4. Loans
5. Reports
6. Save Data
7. Exit
Here’s what each menu contains:
________________________________________

BOOK SERVICES
Add a Book
You will provide:
•	Book ID (unique)
•	Title
•	Authors (comma-separated)
•	ISBN
•	Tags (comma-separated)
•	Total copies
The system calculates available copies automatically.
________________________________________

View All Books
Displays all books with:
•	Title
•	Authors
•	Tags
•	Total & available copies
________________________________________

Update a Book
Enter the book ID and modify the fields you want.
Leave a field blank to keep its existing value.
________________________________________

Remove a Book
You can remove a book only if:
•	It exists
•	It is NOT currently borrowed
________________________________________

Search Books
You may search by:
•	Title
•	Author name
•	Tag/category
All searches are case-insensitive.
________________________________________

USER SERVICES
Add a User
You will provide:
•	User ID (unique)
•	Name
•	Email
•	Status (active / inactive / banned)
•	Maximum allowed loans
Email is validated before saving.
________________________________________

View All Users
Lists all registered users.
________________________________________

Update a User
Modify name, email, status, or loan limit.
________________________________________

Change User Status
•	Activate user
•	Deactivate user
•	Ban user
Users must be active to borrow books.
________________________________________

TRANSACTION SERVICES (Borrow / Return)

Borrow a Book

You must enter:
•	User ID
•	Book ID
The system checks:
•	User exists
•	User is active
•	Book exists
•	Copies available
•	User has not reached max loan limit
A new transaction is created with:
•	Borrow date = today
•	Due date = +14 days
You will receive a Transaction ID.
________________________________________

Return a Book
Enter the Transaction ID created when borrowing.
The system will:
•	Mark the book as returned
•	Update available copies
•	Store the return date
________________________________________

LOANS MENU

Here you can:
•	View all active loans
•	View all overdue loans (based on today’s date)
•	View a specific user’s borrowing history
________________________________________

REPORTS MENU
Provides a quick summary:
•	Number of books
•	Number of users
•	Active loans
•	Overdue loans
________________________________________

Saving Your Data

All data is saved into:
data/books.csv
data/users.csv
data/transactions.csv
To manually save at any point:
________________________________________

6. Save Data

The system also loads everything automatically at startup.
________________________________________

Project Structure

project/
│
├── lms.py                # Main program
├── models.py             # Book, User, Transaction classes
├── library.py            # Core logic for system operations
├── storage.py            # Reading/writing CSV files
├── utils.py              # Display helpers
│
└── data/
    ├── books.csv
    ├── users.csv
    └── transactions.csv
________________________________________

Important Rules & Validations
•	Book IDs and User IDs must be unique
•	Users must be active to borrow
•	Cannot remove a book if it’s borrowed
•	Users cannot exceed their max loan limit
•	Borrowing the same book multiple times without returning is not allowed
•	ISBN numbers must be unique
________________________________________

Example Interactions

Adding a Book

Book ID: B101
Title of the Book: Learn Python
Author of the Book: Mark Lutz
ISBN (International Standard Book Number): 987654321
Tags: python,programming
Total Copies: 3
Book added Successfully.

Adding a User

User ID: U501
User Name: Alice
Email: alice@domain.com
Status: active
Max Loans: 2
User added Successfully.

Borrowing

User ID: U501
Book ID: B101
Borrow successful!
Transaction ID      : T21
Book ID             : B1003
User ID             : U2002
Borrowed date       : 16-11-2025
Due Date            : 30-11-2025
Returned date       : None
Status              : borrowed

Returning
Transaction ID: T1
Book returned successfully.
________________________________________

Troubleshooting
“Book/User not found”
Check the ID again — IDs must match exactly.
“Book not available”

All copies are currently borrowed.
“User not allowed to borrow”
Ensure:
•	User status = active
•	User has not reached loan limit
“Cannot return book”
Wrong or already completed transaction ID.
________________________________________

Tips for Smooth Usage
•	Keep Book IDs like B001, B002 for clarity
•	Keep User IDs like U001, U002
•	Always write down the Transaction ID after borrowing
•	Use the Reports menu to track overdue books
•	Save periodically using option 6
________________________________________

Future Enhancements (Optional)
•	User login system
•	Email reminders for overdue books
•	GUI or web interface
•	Book recommendations
•	Automatic backups

