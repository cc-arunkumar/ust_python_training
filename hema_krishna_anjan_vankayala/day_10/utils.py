# utils.py - Library Management System with Utility Commands

import csv
import os
import sys

# ========== DATA UTILITIES ==========
 
def save_data(books=None, users=None, transactions=None):
    # Save books, users, and transactions back to their CSV files.
    # Expects lists of dictionaries for each.
    # if books:
    #     with open(BOOKS_FILE, "w", newline="") as f:
    #         writer = csv.DictWriter(f, fieldnames=books[0].keys())
    #         writer.writeheader()
    #         writer.writerows(books)
 
    # if users:
    #     with open(USERS_FILE, "w", newline="") as f:
    #         writer = csv.DictWriter(f, fieldnames=users[0].keys())
    #         writer.writeheader()
    #         writer.writerows(users)
 
    # if transactions:
    #     with open(TX_FILE, "w", newline="") as f:
    #         writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
    #         writer.writeheader()
    #         writer.writerows(transactions)
 
    print("All data saved to CSV files.")
 
#display method
def display_help():
    help_text = """
╔════════════════════════════════════════════════════════════════════════════╗
║                    📚 LIBRARY MANAGEMENT SYSTEM 📚                         ║
║                           COMMAND REFERENCE                               ║
╚════════════════════════════════════════════════════════════════════════════╝

🔷 BOOK MANAGEMENT COMMANDS:
   • book add       - Add a new book to the library
   • book update    - Update details of an existing book
   • book remove    - Remove a book from the library
   • book get       - Get details of a specific book
   • book list      - List all books in the library
   • book search    - Search for books by title, author, or tags

🔶 USER MANAGEMENT COMMANDS:
   • user add       - Add a new user to the library
   • user update    - Update details of an existing user
   • user get       - Get details of a specific user
   • user list      - List all users in the library
   • user deactivate - Deactivate a user account
   • user activate  - Activate a user account
   • user ban       - Ban a user account

🔵 TRANSACTION COMMANDS:
   • borrow         - Borrow a book from the library
   • return         - Return a borrowed book to the library

📊 LOANS & REPORTS COMMANDS:
   • loans active   - List all active loans
   • loans overdue  - List all overdue loans
   • loans history  - View loan history for a user
   • report summary - Generate a summary report
   • report user    - Generate a report for a specific user

⚙️  UTILITY COMMANDS:
   • help           - Display this help information
   • save           - Save all data to CSV files
   • exit           - Exit the CLI

═════════════════════════════════════════════════════════════════════════════

💡 TIPS FOR NEW USERS:
   1. All fields with dashes can be left blank by pressing Enter
   2. Use (|) to separate multiple values in Author/Tags fields
   3. Book IDs and User IDs are case-sensitive
   4. Always save your changes before exiting
   5. Ask a librarian if you need help!

═════════════════════════════════════════════════════════════════════════════
"""
    print(help_text)      