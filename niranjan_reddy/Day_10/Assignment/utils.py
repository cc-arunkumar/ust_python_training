def prompt(text):
   return input(text).strip()
def print_book(b):
   print(f"Book_id:{b.book_id}"f"title:{b.title}"f"authors:{b.authors}"f"Isbn:{b.isbn}"f"tags:{b.tags}"f"total copies:{b.total_copies}"f"availablecopies:{b.available_copies}")
def print_user(u):
   print(f"Userid:{u.user_id}"f"name:{u.name}"f"Email:{u.email}"f"status:{u.status}"f"Maxloans:{u.max_loans}")
def print_tx(t):
      print(f"tx_id:{t.tx_id}"f"book_id:{t.book_id}"f"user_id:{t.user_id}"f"borrow_date:{t.borrow_date}"f"due_date:{t.due_date}"f"return_date:{t.return_date}"f"status:{t.status}")