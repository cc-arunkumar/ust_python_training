Library Management System (LMS)
This is a Command-Line Interface (CLI) based Library Management System (LMS) built using Python. It allows managing books, users, and transactions (borrow/return) using a modular approach with Object-Oriented Programming (OOP). The system stores data in CSV files for persistence.

Features


Add, update, and remove books and users.


Borrow and return books with due dates.


View active loans and overdue loans.


Search books by title, author, or tags.


Persistent storage using CSV files for books, users, and transactions.


Simple and clean CLI interface.


Requirements


Python 3.x


No external libraries (uses Python's built-in libraries like csv, datetime, etc.)


Project Structure
.
├── lms.py              # Main CLI entry point
├── models.py           # Classes for Book, User, Transaction
├── storage.py          # CSV-based storage implementation
├── utils.py            # Helper functions
├── data/               # Folder storing CSV files
│   ├── books.csv       # Store all books
│   ├── users.csv       # Store all users
│   └── transactions.csv # Store all transactions
└── README.md           # Project documentation

models.py
Contains the classes Book, User, and Transaction. Each class represents a real-world entity with attributes and methods that define the behavior of the system.
storage.py
Handles all interactions with CSV files, including loading and saving data for books, users, and transactions.
lms.py
The main program that interacts with the user through a CLI. It supports commands like adding books, adding users, borrowing/returning books, and viewing reports.
utils.py
Contains helper functions used across the project, such as input validation.

Setup & Installation


Clone or download the project repository.


Install Python 3.x from python.org.


Run the program using the following command:


python lms.py


CLI Commands
Book Commands


Add Book: Adds a new book to the library.
book add

Prompts:


Book ID


Title


Authors (comma separated)


ISBN


Tags (comma separated)


Total Copies




Update Book: Updates an existing book's details.
book update <book_id>



Remove Book: Removes a book from the library (if not borrowed).
book remove <book_id>



Get Book: Fetches details of a specific book.
book get <book_id>



List Books: Lists all books in the library.
book list



Search Books: Search for books by title, author, or tag.
book search <keyword>



User Commands


Add User: Adds a new user to the system.
user add



Update User: Updates an existing user's details.
user update <user_id>



Get User: Fetches details of a specific user.
user get <user_id>



List Users: Lists all users in the system.
user list



Deactivate / Activate / Ban User: Change a user's status.
user deactivate <user_id>
user activate <user_id>
user ban <user_id>



Borrow/Return Commands


Borrow Book: Borrows a book for a user.
borrow <user_id> <book_id>



Return Book: Returns a borrowed book.
return <transaction_id>



Transaction Queries


Active Loans: Lists all active loans.
loans active



Overdue Loans: Lists all overdue loans.
loans overdue



User Loan History: Displays a specific user's loan history.
loans user <user_id>



Utility Commands


Save: Saves all data to CSV files.
save



Exit: Exits the program.
exit




Example Usage
lms> book add
Book ID: B1001
Title: Python Basics
Authors: Mark Lutz
ISBN: 9781234567
Tags: programming,python
Total Copies: 3
Book added successfully.

lms> user add
User ID: U2001
Name: Arun
Email: arun@ust.com
User added successfully.

lms> borrow U2001 B1001
Borrow successful. Transaction ID: T1. Due Date: 18-11-2025.

lms> return T1
Return successful.

lms> loans active
No active loans.

lms> save
All data saved to CSV successfully.

lms> exit


Error Handling
The system handles various errors gracefully and will provide meaningful messages for invalid operations, such as:


Invalid book ID or user ID.


Attempting to borrow a book that is unavailable.


Attempting to borrow more books than the user's allowed limit.


Trying to return a book that was not borrowed.



Storage Format
The system uses CSV files for persistent storage. The CSV files are stored inside the data/ folder:


books.csv: Stores book details (book ID, title, authors, ISBN, tags, total copies, available copies).


users.csv: Stores user details (user ID, name, email, status, max loans).


transactions.csv: Stores transaction details (transaction ID, book ID, user ID, borrow date, due date, return date, status).



Future Improvements


Search Enhancements: Improve search functionality to support partial matches.


User Authentication: Add user authentication (login/logout) for better security.


Reporting: Add more detailed reports, such as overdue books per user, book availability trends, etc.


GUI Support: Implement a graphical user interface (GUI) for easier interactions.



License
This project is licensed under the MIT License - see the LICENSE file for details.

This README.md provides a detailed overview of how the Library Management System (LMS) works, its structure, usage instructions, and features. Make sure to update the document if you make any changes to the functionality or add new features.