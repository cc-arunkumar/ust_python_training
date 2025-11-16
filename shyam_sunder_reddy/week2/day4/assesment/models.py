class User:
    def __init__(self,user_id,name,email=None,status="active",max_loans=5,active_loans=0):
        self.user_id=user_id
        self.name=name
        self.email=email # optional
        self.status=status # active, inactive, banned
        self.max_loans=max_loans #default max loans is 5
        self.active_loans=active_loans #tracks current active loans
   
    #method to convert user object to dictionary
    def to_dict(self):
        return {
            "user_id":self.user_id,
            "name":self.name,
            "email":self.email,
            "status":self.status,
            "max_loans":self.max_loans,
            "active_loans":self.active_loans
        }
   
    #method to update user details
    def update(self,**kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
   
    #method to update user status
    def activate(self):
        self.status="active"
   
    #method to update user status
    def deactivate(self):
        self.status="inactive"
   
    #method to update user status
    def ban(self):
        self.status="banned"
   
    #check if user can borrow more books
    def can_borrow(self,active_loans):
        if self.status=="active" and active_loans < self.max_loans:
            return True
        return False
    
    #increment active loans
    def increment_loans(self):
        self.active_loans += 1
    
    #decrement active loans
    def decrement_loans(self):
        if self.active_loans > 0:
            self.active_loans -= 1
   
class Books:
    def __init__(self,book_id,title,authors,isbn,tags,total_copies,available_copies):
        self.book_id=book_id
        self.title=title
        self.authors=authors
        self.isbn=isbn
        self.tags=tags
        self.total_copies=total_copies
        self.available_copies=available_copies
   
    #method to convert book object to dictionary
    def to_dict(self):
        return {
            "book_id":self.book_id,
            "title":self.title,
            "authors":self.authors,
            "isbn":self.isbn,
            "tags":self.tags,
            "total_copies":self.total_copies,
            "available_copies":self.available_copies
        }
   
    #method to update book details
    def update(self,**kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
   
    #method to check if books is available
    def is_available(self):
        return self.available_copies > 0
 
    #method to increase the books count
    def increase_copies(self, count):
        self.total_copies += count
        self.available_copies += count
   
    #method to decrease the code
    def decrease_copies(self, count):
        if count <= self.available_copies:
            self.total_copies -= count
            self.available_copies -= count
           
#Transaction class
 
import datetime
class Transaction:
    def __init__(self, tx_id, book_id, user_id, borrow_date, due_date, return_date=None, status='borrowed'):
        self.tx_id = tx_id
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status
   
    #method to convert transaction object to dictionary
    def to_dict(self):
        return {
            'tx_id': self.tx_id,
            'book_id': self.book_id,
            'user_id': self.user_id,
            'borrow_date': self.borrow_date.strftime("%d-%m-%Y"),
            'due_date': self.due_date,
            'return_date': self.return_date if self.return_date else '',
            'status': self.status
        }
   
    #method to mark the book as returned
    def mark_returned(self, return_date):
        self.return_date = datetime.strptime(return_date, "%d-%m-%Y")
        self.status = 'returned'
   
    #method to check if the book is overdue
    def is_overdue(self,today_date):
        due_date_obj = datetime.strptime(self.due_date, "%d-%m-%Y")
        today_date_obj = datetime.strptime(today_date, "%d-%m-%Y")
        if today_date_obj>due_date_obj:
            self.status="overdue"
        return today_date_obj>due_date_obj
 