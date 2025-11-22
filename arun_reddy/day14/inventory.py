class BookinventoyStore:
    def __init__(self):
        self.inventory=[]
    def add_book(self,title,author,quantity,price):
        book = (title, author, quantity, price)
        self.inventory.append(book)
        print("Book added successfully!\n")
    
    def display_books(self):
        print("\n--- Inventory Books ---")
        
        for book in self.inventory:
            t, a, q, p = book
            print("{:<30} {:<20} {:<10} {:<10.2f}".format(t, a, q, p))
    
    def search_book(self,title):
        print("\n--- Search Book ---")
        for book in self.inventory:
            t, a, q, p = book
            if t.lower() == title:
                print(f"Found: Title={t}, Author={a}, Quantity={q}, Price={p:.2f}\n")
                return
    
        print("Book not found.\n")
    
    
    def remove_book(self,title):
        for index, book in enumerate(self.inventory):
            if book[0].lower() == title:
                self.inventory.pop(index)
                print("Book removed successfully!\n")
                return
    
        print("Book not found.\n")
        
    def menu(self):    
        while True:
            print("===== Bookstore Inventory =====")
            print("1. Add Book")
            print("2. Display All Books")
            print("3. Search Book by Title")
            print("4. Remove Book by Title")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    title=input("Enter the title")
                    author=input("Enter the author name")
                    quantity=int(input("Enter the quantity"))
                    price=int(input("Enter the price"))
                    self.add_book(title,author,quantity,price)
                case 2:
                    self.display_books()
                case 3:
                    title=input("Enter the title")
                    self.search_book(title)
                case 4:
                    title=input("Enter the title")
                    self.remove_book(title)
                case 5:
                    return 
 
BookinventoyStore().menu()