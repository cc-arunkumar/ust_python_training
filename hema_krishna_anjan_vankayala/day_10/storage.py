# load_books() -> list of Book objects
# save_books(list_of_Books)
# load_users()
# Assessment: Library Management System 4
# save_users()
# load_transactions()
# save_transactions()
import csv
class CSVStorage:
    
    def load_books(self):
        books_list = []
        with open('data/books.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books_list.append(row)
        return books_list 
            
    
    def save_books(self,list_of_Books):
        with open('data/books.csv','w',newline='') as file:
            #Create the fieldnames list
            header = ['book_id','title','authors','isbn','tags','total_copies','available_copies']
        
            #Create a DictWriter object
            writer = csv.DictWriter(file,fieldnames=header)

            #write the header to csv
            writer.writeheader()
        
            #write the  names in csv
            writer.writerows(list_of_Books)
        
    
    def load_users(self):
        users_list = []
        with open('data/users.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users_list.append(row)
        return users_list
    
    def save_users(self,list_of_users):
        with open('data/users.csv','w',newline='') as file:
            #Create the fieldnames list
            header = ['user_id','name','email','status','max_loans','active_loans']

        
            #Create a DictWriter object
            writer = csv.DictWriter(file,fieldnames=header)

            #write the header to csv
            writer.writeheader()
        
            #write the employee names in csv
            writer.writerows(list_of_users)
        
    def load_transactions(self):
        transactions_list = []
        with open('data/transactions.csv','r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions_list.append(row)
        return transactions_list
    
    def save_transactions(self,list_of_transactions):
        with open('data/transactions.csv','w',newline='') as file:
            #Create the fieldnames list
            header = ['tx_id','book_id','user_id','borrow_date','due_date','return_date','status']
        
            #Create a DictWriter object
            writer = csv.DictWriter(file,fieldnames=header)

            #write the header to csv
            writer.writeheader()
        
            #write the employee names in csv
            writer.writerows(list_of_transactions)

