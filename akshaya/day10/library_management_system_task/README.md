# Library Management System (LMS)

This is a Library Management System (LMS) implemented in Python. It allows users to manage books, users, and transactions in a command-line interface (CLI). The system supports features like borrowing and returning books, managing users, soft-deleting and recovering books, and generating reports.

## Features:
- Add, update, and remove books (soft delete).
- Add, update, or manage users.
- Borrow and return books with automatic due dates.
- View active and overdue loans.
- Generate reports for books, users, and transactions.

---

## How to Run the Program

### Prerequisites:
1. **Python 3.x**: Make sure Python 3.x is installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Install dependencies**: The program uses external libraries. Install them using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

    > **Note**: If there's no `requirements.txt` file, you can manually install required libraries like `datetime`, `uuid`, and any other dependencies used in the code.

3. **CSV Storage**: The system uses CSV files to store book, user, and transaction data. Make sure the following CSV files are available:
    - `books.csv` – For storing book details.
    - `users.csv` – For storing user details.
    - `transactions.csv` – For storing transactions (borrowed books).

### Running the Program:
1. Open a terminal or command prompt.

2. Navigate to the directory where the `lms.py` file is located.

3. Run the program with the following command:
    ```bash
    python lms.py
    ```

4. The CLI will display the main menu and prompt you for your choices.

---

## CLI Commands List

### Main Menu:
Once the program starts, you will see the main menu with the following options:

1. **Manage Books**
    - Add, update, or remove books from the library.
2. **Manage Users**
    - Add, update, or manage users in the system.
3. **Borrow / Return Books**
    - Borrow or return books for users.
4. **View Loans**
    - View active and overdue loans.
5. **View Reports**
    - Generate summary and user transaction reports.
6. **Save Changes**
    - Save changes made to books, users, and transactions.
7. **Exit**
    - Exit the program.

### Manage Books:
1. **Add Book**: Add a new book to the library by providing details like book ID, title, authors, ISBN, tags, total copies, and available copies.
2. **Update Book**: Update the details of an existing book.
3. **Remove Book (Soft Delete)**: Mark a book as deleted, which will set its available copies to 0 and clear its details. Soft-deleted books cannot be borrowed.
4. **Get Book**: Retrieve the details of a specific book by its ID.
5. **List Books**: View all books in the library.
6. **Search Books**: Search for books by title, author, or tag.

### Manage Users:
1. **Add User**: Add a new user by providing user ID, name, email, and maximum allowed loans.
2. **Update User**: Update the details of an existing user.
3. **Get User**: Retrieve the details of a specific user by their ID.
4. **List Users**: View all users in the system.
5. **Change User Status**: Change the status of a user (activate, deactivate, ban).
6. **Report User Transactions**: View a user's transaction history.

### Borrow / Return Books:
1. **Borrow Book**: Borrow a book by providing the user ID and book ID. If the user has not reached their maximum loan limit, the book will be borrowed.
2. **Return Book**: Return a borrowed book by providing the transaction ID. The book’s available copies will be updated.

### View Loans:
1. **Active Loans**: View all currently active (borrowed) loans.
2. **Overdue Loans**: View all overdue loans.
3. **Loans by User**: View loans by a specific user.

### View Reports:
1. **Summary Report**: View a summary of the library's current state, including the total number of books, active loans, and overdue loans.
2. **User Report**: View all transactions for a specific user.

### Save Changes:
- Save the current state of books, users, and transactions to the corresponding CSV files.

---

## Example Steps

### Step 1: Start the program
```bash
python lms.py
Manage Books

To add a book, choose option 1 (Manage Books) → 1 (Add Book) and provide the required details:

Book ID: B1001
Title: Learning Python
Authors: Mark Lutz
ISBN: 9780596158101
Tags: python, programming
Total Copies: 5
Available Copies: 5
Manage Users

To add a user, choose option 2 (Manage Users) → 1 (Add User) and provide the required details:

User ID: U101
Name: John Doe
Email: john@ust.com
Max Loans (default 0): 5
Borrow a Book

To borrow a book, choose option 3 (Borrow / Return Books) → 1 (Borrow Book):

User ID: U101
Book ID to borrow: B1001


After confirming the borrow, the book is borrowed.
Return a Book

To return a book, choose option 3 (Borrow / Return Books) → 2 (Return Book):

Transaction ID: T1


Confirm the return and the book’s available copies will be updated.
View Loans

To view active loans, choose option 4 (View Loans) → 1 (Active Loans).