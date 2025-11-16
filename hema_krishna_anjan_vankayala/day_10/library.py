from storage import CSVStorage
from models import User,Books,Transaction
import utils
import datetime

#book not availbale
class InvalidBookError(Exception):
    pass
 
#user not present
class InvalidUserError(Exception):
    pass
 
#book not present in data
class BookNotAvailableError(Exception):
    pass
 
#user error
class UserNotAllowedError(Exception):
    pass
 
#transaction error
class TransactionError(Exception):
    pass
 
#wrong Input
class ValidationError(Exception):
    pass

# ========== HELPER FUNCTIONS ==========
def generate_transaction_id():
    """Generate next transaction ID"""
    transactions = CSVStorage().load_transactions()
    if not transactions:
        return "T3001"
    last_tx = transactions[-1]
    last_id = int(last_tx['tx_id'][1:])
    return f"T{last_id + 1}"

def add_transaction_record(tx_id, book_id, user_id, borrow_date, due_date, return_date="", status="borrowed"):
    """Add a new transaction record to CSV"""
    transactions = CSVStorage().load_transactions()
    tx_dict = {
        'tx_id': tx_id,
        'book_id': book_id,
        'user_id': user_id,
        'borrow_date': borrow_date,
        'due_date': due_date,
        'return_date': return_date,
        'status': status
    }
    transactions.append(tx_dict)
    CSVStorage().save_transactions(transactions)

def update_transaction_record(tx_id, return_date, status="returned"):
    """Update transaction record when book is returned"""
    transactions = CSVStorage().load_transactions()
    for tx in transactions:
        if tx['tx_id'] == tx_id:
            tx['return_date'] = return_date
            tx['status'] = status
            CSVStorage().save_transactions(transactions)
            return True
    return False

# ========== ORIGINAL FUNCTIONS START HERE ==========
#     'book_id': 'B001',
#     'title': 'The Great Gatsby',
#     'authors': 'F. Scott Fitzgerald',
#     'isbn': '9780743273565',
#     'tags': 'classic|fiction',
#     'total_copies': 3
# }
 
# update_books = ('B001', {
#     'title': 'The Great Gatsby - Updated Edition',
#     'authors': 'F. Scott Fitzgerald',
#     'isbn': '9780743273565',
#     'tags': 'classic|fiction|novel',
#     'total_copies': 5
# })
 
def find_book(books, book_id):
    for book in books:
        if book['book_id'] == book_id:
            return True
    return False
           
def add_book(books_dict):
    books = CSVStorage().load_books()
    book_id = books_dict['book_id']
    if find_book(books, book_id):
        return ("Book ID exists.")
   
    title = books_dict['title']
    authors = books_dict['authors']
    isbn = books_dict['isbn']
    tags = books_dict['tags']
    
    try:
        available_copies = int(books_dict['available_copies'])
        total = int(books_dict['total_copies'])
    except ValueError:
        return "Total copies and Available copies should be integers."
        
    b = Books(book_id=book_id, title=title, authors=authors, isbn=isbn, tags=tags,
              total_copies=total, available_copies=available_copies)
   
    books.append(b.to_dict())
    # print(books)
    CSVStorage().save_books(books)
    return "Book added successfully."
   
def update_book(book_id,**update_data):
 
    books = CSVStorage().load_books()
    for book in books:
        if book['book_id'] == book_id:
            try:
                total_copies=int(update_data['total_copies'])
                available_copies=int(update_data['available_copies'])
                
            except ValueError:
                return "Total copies and Available copies should be integers."
            b = Books(
                book_id=book_id,
                title=update_data['title'],
                authors=update_data['authors'],
                isbn=update_data['isbn'],
                tags=update_data['tags'],
                total_copies=int(update_data['total_copies']),
                available_copies=int(update_data['available_copies'])
            )
            b.update(**update_data)
            book.update(b.to_dict())
            CSVStorage().save_books(books)
            return "Book updated successfully."
    return "Book ID not found."
 
def remove_book(book_id):
    books = CSVStorage().load_books()
    for book in books:
        if book['book_id'] == book_id:
            books.remove(book)
            CSVStorage().save_books(books)
            return "Book removed successfully."
    return  "Book ID not found."
 
def get_book(book_id):
    books = CSVStorage().load_books()
    for book in books:
        if book['book_id'] == book_id:
            # Convert numeric fields from string to int
            book['total_copies'] = int(book['total_copies'])
            book['available_copies'] = int(book['available_copies'])
            return book
    return None
 
def list_books():
    books = CSVStorage().load_books()
    # Convert numeric fields from string to int for all books
    for book in books:
        book['total_copies'] = int(book['total_copies'])
        book['available_copies'] = int(book['available_copies'])
    return books
 
#search by title substring author tag
def search_books(query):
    books = CSVStorage().load_books()
    results = []
    query_lower = query.lower()
    for book in books:
        if (query_lower in book['title'].lower() or
            query_lower in book['authors'].lower() or
            query_lower in book['tags'].lower()):
            # Convert numeric fields from string to int
            book['total_copies'] = int(book['total_copies'])
            book['available_copies'] = int(book['available_copies'])
            results.append(book)
    return results
 
def add_user(user_dict):
    users = CSVStorage().load_users()
    user_id = user_dict['user_id']
    for user in users:
        if user['user_id'] == user_id:
            return "User ID exists."
    # Required fields
    name = user_dict.get('name')
    email = user_dict.get('email')
    if not name or not email:
        return "ERROR: 'name' and 'email' are required fields."

    # Validate email domain
    if not isinstance(email, str) or not email.lower().endswith('@ust.com'):
        return "ERROR: Invalid email domain. Email must end with '@ust.com'."

    # Validate status
    status = user_dict.get('status', 'active')
    if status not in ('active', 'inactive', 'banned'):
        return "ERROR: Invalid status. Must be one of: active, inactive, banned."

    # Numeric fields
    try:
        max_loans = int(user_dict.get('max_loans', 5))
    except Exception:
        return "ERROR: max_loans must be an integer."
    try:
        active_loans = int(user_dict.get('active_loans', 0))
    except Exception:
        return "ERROR: active_loans must be an integer."

    u = User(user_id=user_id, name=name, email=email, status=status, max_loans=max_loans, active_loans=active_loans)
    users.append(u.to_dict())
    CSVStorage().save_users(users)
    return "User added successfully."
 
def update_user(user_id, **update_data):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            # Validate incoming fields
            if 'email' in update_data:
                new_email = update_data['email']
                if not isinstance(new_email, str) or not new_email.lower().endswith('@ust.com'):
                    return "ERROR: Invalid email domain. Email must end with '@ust.com'."
            if 'status' in update_data:
                new_status = update_data['status']
                if new_status not in ('active', 'inactive', 'banned'):
                    return "ERROR: Invalid status. Must be one of: active, inactive, banned."

            # Ensure numeric fields are correctly typed if provided
            if 'max_loans' in update_data:
                try:
                    update_data['max_loans'] = int(update_data['max_loans'])
                except Exception:
                    return "ERROR: max_loans must be an integer."
            if 'active_loans' in update_data:
                try:
                    update_data['active_loans'] = int(update_data['active_loans'])
                except Exception:
                    return "ERROR: active_loans must be an integer."

            u.update(**update_data)
            user.update(u.to_dict())
            CSVStorage().save_users(users)
            return "User updated successfully."
    return "User ID not found."
 
def get_user(user_id):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            # Convert numeric fields from string to int
            user['max_loans'] = int(user['max_loans'])
            user['active_loans'] = int(user.get('active_loans', 0))
            return user
    return None
 
def list_users():
    users = CSVStorage().load_users()
    # Convert numeric fields from string to int for all users
    for user in users:
        user['max_loans'] = int(user['max_loans'])
        user['active_loans'] = int(user.get('active_loans', 0))
    return users

def list_active_users():
    """List only active users (excluding inactive and banned)"""
    users = CSVStorage().load_users()
    # Convert numeric fields from string to int
    for user in users:
        user['max_loans'] = int(user['max_loans'])
        user['active_loans'] = int(user.get('active_loans', 0))
    active_users = [u for u in users if u['status'] == 'active']
    return active_users

def list_all_users_with_status():
    """List all users with their status information"""
    users = CSVStorage().load_users()
    # Convert numeric fields from string to int
    for user in users:
        user['max_loans'] = int(user['max_loans'])
        user['active_loans'] = int(user.get('active_loans', 0))
    return users
 
def deactivate_user(user_id):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            u.deactivate()
            users.remove(user)
            user.update(u.to_dict())
            users.append(user)
            CSVStorage().save_users(users)
            return "User deactivated successfully."
    return "User ID not found."
 
def activate_user(user_id):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            u.activate()
            user.update(u.to_dict())
            CSVStorage().save_users(users)
            return "User activated successfully."
    return "User ID not found."
 
def ban_user(user_id):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            u.ban()
            user.update(u.to_dict())
            CSVStorage().save_users(users)
            return "User banned successfully."
    return "User ID not found."
 
def borrow_book(book_id, user_id):
    books = CSVStorage().load_books()
    users = CSVStorage().load_users()
   
    # Find the book
    for book in books:
        if book['book_id'] == book_id:
            b = Books(
                book_id=book['book_id'],
                title=book['title'],
                authors=book['authors'],
                isbn=book['isbn'],
                tags=book['tags'],
                total_copies=int(book['total_copies']),
                available_copies=int(book['available_copies'])
            )
            break
    else:
        return "Book ID not found."
   
    # Find the user
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            break
    else:
        return "User ID not found."
   
    active_loans = u.active_loans
    # Check if user is banned
    if u.status == 'banned':
        return f"ERROR: User account is banned and cannot borrow books."
    
    # Check if user is inactive
    if u.status == 'inactive':
        return f"ERROR: User account is inactive. Please contact library staff to reactivate."
    
    # Check if user has reached maximum loans
    if active_loans >= u.max_loans:
        return f"ERROR: User has reached maximum allowed loans ({active_loans}/{u.max_loans}). Please return a book first."
   
    # Check if book is available
    if b.available_copies <= 0:
        return "ERROR: No available copies of the book. Please try again later."
   
    # Process borrowing
    b.available_copies -= 1
    u.active_loans += 1
   
    # Update book and user records
    for book in books:
        if book['book_id'] == b.book_id:
            book.update(b.to_dict())
            break
   
    for user in users:
        if user['user_id'] == u.user_id:
            user.update(u.to_dict())
            break
   
    CSVStorage().save_books(books)
    CSVStorage().save_users(users)
    
    # ===== ADD TRANSACTION RECORD =====
    tx_id = generate_transaction_id()
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    due_date = (datetime.datetime.today() + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
    add_transaction_record(tx_id, book_id, user_id, today, due_date, "", "borrowed")
   
    return "Book borrowed successfully."
 
def return_book(book_id, user_id):
    books = CSVStorage().load_books()
    users = CSVStorage().load_users()
    transactions = CSVStorage().load_transactions()
   
    # Find the book
    for book in books:
        if book['book_id'] == book_id:
            b = Books(
                book_id=book['book_id'],
                title=book['title'],
                authors=book['authors'],
                isbn=book['isbn'],
                tags=book['tags'],
                total_copies=int(book['total_copies']),
                available_copies=int(book['available_copies'])
            )
            break
    else:
        return "Book ID not found."
   
    # Find the user
    for user in users:
        if user['user_id'] == user_id:
            u = User(
                user_id=user['user_id'],
                name=user['name'],
                email=user['email'],
                status=user['status'],
                max_loans=int(user['max_loans']),
                active_loans=int(user.get('active_loans', 0))
            )
            break
    else:
        return "User ID not found."
   
    # Check if user has any active loans
    if u.active_loans <= 0:
        return "User has no active loans to return."
   
    # Find the transaction record for this book and user
    tx_id = None
    for tx in transactions:
        if tx['book_id'] == book_id and tx['user_id'] == user_id and tx['status'] == 'borrowed':
            tx_id = tx['tx_id']
            break
    
    if not tx_id:
        return "No active loan found for this book and user."
   
    # Process returning
    b.available_copies += 1
    u.active_loans -= 1
   
    # Update book and user records
    for book in books:
        if book['book_id'] == b.book_id:
            book.update(b.to_dict())
            break
   
    for user in users:
        if user['user_id'] == u.user_id:
            user.update(u.to_dict())
            break
   
    CSVStorage().save_books(books)
    CSVStorage().save_users(users)
    
    # ===== UPDATE TRANSACTION RECORD =====
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    update_transaction_record(tx_id, today, "returned")
   
    return "Book returned successfully."
 
def view_active_loans(user_id):
    users = CSVStorage().load_users()
    for user in users:
        if user['user_id'] == user_id:
            active_loans = int(user.get('active_loans', 0))
            return active_loans
    return None
 
def view_overdue_loans(user_id):
    transactions = CSVStorage().load_transactions()
    for transaction in transactions:
        if transaction['user_id'] == user_id and transaction['status'] == 'overdue':
            return f"Overdue loans for user {user_id}: [Transaction ID: {transaction['transaction_id']}]"
 
def view_loan_history(user_id):
    transactions = CSVStorage().load_transactions()
    history = []
    for transaction in transactions:
        if transaction['user_id'] == user_id:
            history.append(transaction)
    return history
 
# print(add_user({'user_id': 'U2026', 'name': 'Karan Singh', 'email': 'karan.sign@gmail.com','status':'active','max_loans':'2'}))
# print(update_user('U2026', {'name': 'Karan S Singh', 'email': 'karaan.dign@gmail.com','status':'active','max_loans':'3'}))
# print(get_user('U2026'))
# print(list_users())
# print(deactivate_user('U2026'))
# print(activate_user('U2026'))
# print(ban_user('U2026'))
# print(borrow_book('B1029','U2026'))