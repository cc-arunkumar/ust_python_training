# Utility functions to display Book, User, and Transaction objects in a readable format.

def print_book(b):
    
    # Join authors and tags lists into comma-separated strings if they are lists or tuples
    authors = ", ".join(b.authors) if isinstance(b.authors, (list, tuple)) else b.authors
    tags = ", ".join(b.tags) if isinstance(b.tags, (list, tuple)) else b.tags

    # Printing user details 
    print(f"""
--- BOOK ---
Book ID             : {b.book_id}
Book Title          : {b.title}
Authors of the book : {authors}
ISBN                : {b.isbn}
Tags                : {tags}
Total Copies        : {b.total_copies}
Available Copies    : {b.available_copies}
--------------""")

# Printing user details
def print_user(u):
    print(f"""
--- USER ---
User ID             : {u.user_id}
Name of the user    : {u.name}
Email               : {u.email}
Status              : {u.status}
Max Loans           : {u.max_loans}
--------------""")

# Printing transaction details
def print_tx(t):
    print(f"""
--- TRANSACTION ---
Transaction ID      : {t.tx_id}
Book ID             : {t.book_id}
User ID             : {t.user_id}
Borrowed date       : {t.borrow_date}
Due Date            : {t.due_date}
Returned date       : {t.return_date}
Status              : {t.status}
--------------------""")
