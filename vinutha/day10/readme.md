Library Management System
A simple library management system to manage books, users, and transactions (borrow/return). This system allows administrators to add, update, search, and manage books and users, as well as view the borrowing history and overdue loans.

Features
Book Management:

Add, update, remove, and list books.
Search books by title, author, or tag.
View detailed information about a specific book.
User Management:

Add, update, and manage users.
Deactivate, activate, or ban users.
View user details and loan history.
Transaction Management:

Borrow and return books.
Track active loans and overdue books.
View loan history for specific users.
Data Persistence:

Data is stored in CSV files for easy access and updates.
You can save and load books, users, and transactions from CSV.
Prerequisites
Python 3.x
Libraries used:
datetime: For handling dates and times.
csv: For reading and writing CSV files.
File Structure
lms.py: Main script file containing the logic for interacting with the user and handling different operations.
models.py: Contains the classes for Book, User, and Transaction, along with the associated methods.
storage.py: Handles the CSV storage and loading for books, users, and transactions.
data/: Folder to store the CSV files for books, users, and transactions (if applicable).
Installation
Clone or download the repository.
Make sure you have Python 3 installed on your machine. You can download it from here.
Install any dependencies using pip (if required, specify them in a requirements.txt file).
Run the lms.py script to start the Library Management System:
```bash python lms.py

Commands

Book Management:

1: Add Book 2: Update Book 3: Remove Book 4: Get Book Details 5: List Books 6: Search Books

User Management:

7: Add User 8: Update User 9: Get User Details 10: List Users 11: Deactivate/Activate/Ban User

Transaction Management:

12: Borrow Book 13: Return Book 14: View Active Loans 15: View Overdue Loans 16: View User Loan History

Miscellaneous:

17: Save Data to CSV 18: Exit 19: Help

CSV File Format

The system reads and writes data from the following CSV files:

Books: book_id, title, authors, isbn, tags, total_copies, available_copies

Users: user_id, name, email, status, max_loans, password

Transactions: tx_id, book_id, user_id, borrow_date, due_date, return_date, status

Contributing

If you'd like to contribute to this project, feel free to fork it and submit a pull request. Please ensure that any changes you make are well-documented.

License

This project is open-source and available under the MIT License.