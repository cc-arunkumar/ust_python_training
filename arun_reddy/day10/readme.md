# Library Management System (LMS)

A simple command-line application that helps manage a library. You can add books, manage users, and track who borrows books.

## What Can This System Do?

- **Manage Books**: Add new books, update information, view all books, or remove books
- **Manage Users**: Add new members, update their details, see all members, or remove members
- **Track Borrowing**: Keep track of who borrowed which book and when it should be returned
- **Save Data**: All information is saved in CSV files (simple text files)

## Before You Start

You need Python 3.x installed on your computer. No special libraries needed - just basic Python!

## How to Run the Program

1. Open a terminal/command prompt
2. Go to the folder where the files are located
3. Type: `python lms.py`
4. The program will start showing a menu

## How to Use - Step by Step

### Main Menu

When you run the program, you'll see 6 choices:
- **1. Book Services** - Add, view, update, or remove books
- **2. User Services** - Add, view, update, or remove users  
- **3. Transaction Services** - Borrow or return books
- **4. Utility Commands** - Save all data
- **5. Help** - Show help information
- **6. Exit** - Close the program

### Book Services

#### Add a Book
- Choose option 1 from the main menu
- You'll need to provide:
  - **Book ID**: A unique code (like B001, B002)
  - **Title**: Name of the book
  - **Authors**: Who wrote it (you can add multiple, separated by commas)
  - **ISBN**: The book's ISBN number
  - **Tags**: Categories (separated by commas, like "fiction,adventure")
  - **Total Copies**: How many copies the library has

#### View All Books
- Choose option 2 to see a list of all books
- Shows how many copies are available

#### Update a Book
- Choose option 3
- Enter the Book ID you want to change
- You can leave fields empty to keep the current value

#### Remove a Book
- Choose option 4
- Enter the Book ID
- Confirm by typing 'y'

### User Services

#### Add a User
- Choose option 1 from User Services menu
- You'll need to provide:
  - **User ID**: A unique code (like U001, U002)
  - **Name**: Person's full name
  - **Email**: Must end with @ust.com
  - **Status**: Choose from: active, inactive, or banned
  - **Max Loans**: Maximum books they can borrow at once

#### View All Users
- Choose option 2 to see all library members

#### Update a User
- Choose option 3
- Enter the User ID
- You can leave fields empty to keep current values

#### Remove a User
- Choose option 4
- Enter the User ID
- Confirm by typing 'y'

### Transaction Services (Borrowing & Returning)

#### Borrow a Book
- Choose option 1
- Enter the User ID (who is borrowing)
- Enter the Book ID (which book)
- The system will automatically set the due date to 14 days from today
- You'll get a Transaction ID - save this for returning the book!

#### Return a Book
- Choose option 2
- Enter the Transaction ID (from when the book was borrowed)
- The book will be marked as returned
- The book count will update

## Saving Your Data

All your information (books, users, borrowing records) is saved in CSV files in the `data` folder:
- `books.csv` - List of all books
- `users.csv` - List of all users
- `transactions.csv` - Borrowing records

You can choose "4. Utility Commands" from the main menu to manually save everything.

## Important Rules

- **Email**: User emails MUST end with @ust.com
- **Book ID**: Each book must have a unique ID
- **User ID**: Each user must have a unique ID
- **Max Loans**: Users cannot borrow more books than their max limit
- **Status**: Users must have a valid status (active/inactive/banned)
- **Active Users Only**: Only active users can borrow books

## Example Usage

### Adding a Book
```
Enter Book ID: B1001
Enter Title: Python for Beginners
Enter Authors (comma separated): Guido van Rossum
Enter ISBN: 123456789
Enter Tags (comma separated): programming,python
Enter Total Copies: 5
✓ Book added successfully.
```

### Adding a User
```
Enter User ID: U2001
Enter Name: John Doe
Enter Email: john.doe@ust.com
Enter Status (active/inactive/banned): active
Enter Max Loans (books they can borrow at once): 3
✓ User added successfully.
```

### Borrowing a Book
```
Enter User ID: U2001
Enter Book ID: B1001
✓ Borrow successful!
  Transaction ID: T1
  Due Date: 30-11-2025
```

### Returning a Book
```
Enter Transaction ID: T1
✓ Return successful.
```

## File Structure

```
day10/
├── lms.py              # Main program (run this file)
├── models.py           # Classes for Books, Users, Transactions
├── storage.py          # Handles saving and loading from CSV files
├── utils.py            # Helper functions
├── readme.md           # This file
└── data/               # Folder where all data is saved
    ├── books.csv       # All books
    ├── users.csv       # All users
    └── transactions.csv # All borrowing records
```

## Troubleshooting

**Problem**: "FileNotFoundError: No such file or directory"
- **Solution**: Make sure you're running the program from the correct folder. The `data` folder will be created automatically.

**Problem**: Cannot add a user with email
- **Solution**: Make sure the email ends with `@ust.com` (Example: `john.doe@ust.com`)

**Problem**: Cannot borrow a book
- **Solution**: Check that:
  - The user is active (status = active)
  - The user hasn't reached their borrowing limit
  - The book has copies available

**Problem**: Book ID or User ID already exists
- **Solution**: Use a different ID or update the existing one

## Tips for Using the System

1. Write down Transaction IDs when borrowing books - you'll need them to return books
2. Make sure user emails end with @ust.com
3. Use meaningful Book IDs and User IDs (like B001, U001)
4. Check the books list before borrowing to see available copies
5. Remember the due date is 14 days from the borrowing date

## Future Improvements

These features could be added in the future:
- Search for books by title or author
- View borrowing history for a user
- Show overdue books
- Email notifications
- User login/password
- Graphical interface instead of text menu

---

**Need Help?** Choose option 5 (Help) from the main menu to see a quick reference guide.

Happy reading! 📚