# 📚 Library Management System (LMS) - Complete Guide

## 🎯 Overview

Welcome to the **Library Management System (LMS)** - A child-friendly, easy-to-use terminal-based application for managing a library's books and users. This system helps manage books, user accounts, borrowing/returning books, and generating comprehensive reports.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- CSV data files (pre-configured in `data/` folder)

### Installation & Setup

1. **Navigate to the project directory:**
   ```powershell
   cd d:\Training\hema_krishna_anjan_vankayala\day_10
   ```

2. **Ensure the data directory exists with required CSV files:**
   ```
   data/
   ├── books.csv
   ├── users.csv
   └── transactions.csv
   ```

3. **Run the application:**
   ```powershell
   python lms.py
   ```

---

## 🎮 User Interface Guide

### Main Menu
The application opens with a friendly main menu offering 6 options:

```
🎓 WELCOME TO THE LIBRARY MANAGEMENT SYSTEM (LMS) 🎓
============================================================
📚 MAIN MENU
============================================================
1. 📖 MANAGE BOOKS
2. 👤 MANAGE USERS
3. 🔄 BORROW/RETURN BOOKS
4. 📋 VIEW LOANS & REPORTS
5. ℹ️  HELP & INFORMATION
6. 🚪 EXIT
```

---

## 📖 Feature Descriptions

### 1️⃣ MANAGE BOOKS

**Add a New Book**
- Unique Book ID
- Book Title
- Author(s) - separate multiple with `|`
- ISBN number
- Tags - separate multiple with `|`
- Total Copies available
- Available Copies for borrowing

**Update Book Details**
- Modify any book information
- Leave fields blank to keep current values

**Remove a Book**
- Delete a book from the library

**Search for Books**
- Search by title, author, or tags
- Returns all matching results

**View Book Details**
- See complete information for a specific book

**List All Books**
- View a formatted table of all books

---

### 2️⃣ MANAGE USERS

**Add a New User**
- User ID
- User Name
- Email address
- Status (active/inactive/banned)
- Maximum loans allowed (default: 5)

**Update User Details**
- Modify user information
- Leave fields blank to keep current values

**View User Details**
- See complete information for a specific user

**List All Users**
- View a formatted table of all users

**User Status Management**
- **Activate**: Enable a user to borrow books
- **Deactivate**: Temporarily disable a user
- **Ban**: Permanently prevent a user from borrowing

---

### 3️⃣ BORROW/RETURN BOOKS

**Borrow a Book**
- User provides their User ID
- User provides the Book ID to borrow
- System checks:
  - User is active
  - User hasn't exceeded max loans
  - Book has available copies
- Book copies reduced by 1
- Active loans count increased by 1

**Return a Book**
- User provides Book ID and User ID
- System checks if user has active loans
- Book copies increased by 1
- Active loans count decreased by 1

---

### 4️⃣ VIEW LOANS & REPORTS

**View Active Loans**
- See current active loans for a specific user
- Shows count of books currently borrowed

**View Overdue Loans**
- Identify books not returned by due date

**View Loan History**
- Complete transaction history for a user

**Generate Summary Report**
- Total books in library
- Total users registered
- Available vs Total copies
- Number of active users

**Generate User Report**
- Complete user profile
- Transaction history
- Current borrowing status

---

### 5️⃣ HELP & INFORMATION

Display comprehensive help information about:
- All available commands
- System features
- Tips for new users
- Data entry guidelines

---

## 📊 Data Structure

### Users CSV Fields
```
user_id | name | email | status | max_loans | active_loans
```

### Books CSV Fields
```
book_id | title | authors | isbn | tags | total_copies | available_copies
```

### Transactions CSV Fields
```
tx_id | book_id | user_id | borrow_date | due_date | return_date | status
```

---

## 💡 Pro Tips & Best Practices

### For Librarians:
1. **Regular Backups**: Save data frequently (use the Save option)
2. **User Management**: Monitor active/inactive users regularly
3. **Stock Control**: Check available copies vs total copies
4. **Reports**: Generate summary reports at end of day

### For Students/Kids:
1. **Check Availability**: Always check if a book is available before requesting
2. **Return on Time**: Note the due date when borrowing
3. **One at a Time**: Don't borrow more than your max loans limit
4. **Ask for Help**: Ask a librarian if unsure about the system

### Data Entry Tips:
- Use `|` (pipe) character to separate multiple values
- Leave fields blank with Enter to skip optional fields
- Book IDs and User IDs are case-sensitive
- Email should follow standard format

---

## ⚙️ System Features & Benefits

### ✅ Easy Navigation
- Menu-driven interface with clear options
- Emoji icons for better visual understanding
- Simple yes/no confirmations

### ✅ Error Handling
- User-friendly error messages
- Input validation for all fields
- Prevents invalid operations (e.g., negative copies)

### ✅ Data Persistence
- Automatic save to CSV files
- No data loss between sessions
- Transaction history maintained

### ✅ Comprehensive Reporting
- Multiple report types
- Summary statistics
- User-specific analytics

### ✅ User-Friendly Design
- Clear prompts and messages
- Formatted tables for easy reading
- Back navigation from sub-menus

---

## 🔄 Workflow Example

### Scenario: A student borrowing a book

1. **Student approaches the counter** with User ID
2. **Librarian opens LMS** → Main Menu
3. **Select**: "3. BORROW/RETURN BOOKS" → "1. Borrow a Book"
4. **Enter**: Student's User ID and desired Book ID
5. **System checks**:
   - Is user active? ✓
   - Does user have loan capacity? ✓
   - Are copies available? ✓
6. **System confirms**: "Book borrowed successfully"
7. **Book details** updated automatically
8. Student can now take the book

---

## 🐛 Troubleshooting

### "Book ID not found"
- Verify the Book ID exists
- Check if ID is spelled correctly (case-sensitive)
- Use "List All Books" to see available IDs

### "User cannot borrow more books"
- User has reached max loan limit
- User status might be inactive or banned
- Return a book first to free up quota

### "No available copies of the book"
- All copies are currently borrowed
- Check the book's availability status
- Ask if/when copies will be returned

### CSV File Errors
- Ensure `data/` folder exists
- Check file permissions
- Verify CSV format hasn't been corrupted

---

## 📈 Future Enhancements

Suggested improvements for future versions:
1. **Fine Management**: Track and calculate late fees
2. **Email Notifications**: Send reminders for due dates
3. **Book Reviews**: Allow users to rate and review books
4. **Advanced Search**: Filter by publication year, genre
5. **Export Reports**: Generate PDF/Excel reports
6. **Multi-language Support**: Support multiple languages
7. **Barcode Scanning**: QR/Barcode integration

---

## 📞 Support & Contact

For issues or questions:
1. Check the "Help & Information" section in the app
2. Review this README document
3. Contact your system administrator
4. Check error messages carefully for guidance

---

## 📋 Project Files

```
day_10/
├── lms.py          # Main CLI application
├── library.py      # Core business logic
├── models.py       # Data models (User, Books, Transaction)
├── storage.py      # CSV storage operations
├── utils.py        # Utility functions
├── README.md       # This file
└── data/
    ├── books.csv
    ├── users.csv
    └── transactions.csv
```

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Object-Oriented Programming (OOP)
- ✅ File I/O operations (CSV handling)
- ✅ Menu-driven CLI applications
- ✅ Data validation and error handling
- ✅ Project organization and modularity
- ✅ User-friendly interface design

---

## 📝 Version Information

- **Version**: 1.0 (Enhanced Edition)
- **Last Updated**: November 2025
- **Python Version**: 3.7+
- **Status**: Fully Functional

---

## 🎉 Enjoy Using the Library Management System!

Remember: A well-organized library is a happy library! 📚✨

---

**Happy Reading! 🎓📖**
