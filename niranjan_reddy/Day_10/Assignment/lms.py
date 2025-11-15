
from library import Library
from models import *
from utils import *



library1=Library()

while True:
    command=input("lms> ").strip().split()

    if not command:
        continue
    try:
        if command[0]=="help":
            print("""Available commands:
                book add/update/remove/get/list/search
                user add/update/get/list/activate/deactivate/ban
                borrow <user_id> <book_id>
                return <transaction_id>
                loans active/overdue/user <user_id>
                report summary/user <user_id>
                save
                exit
                """)
        elif command[0]=="book":
            if command[1]=="add":
                book_id=input("Book ID: ")
                title=input("Title: ")
                authors=input("Authors: ")
                isbn=input("ISBN: ")
                tags=input("Tags: ")
                total_copies=input("Total Copies: ")
                library1.add_book(book_id,title,authors,isbn,tags,total_copies)
                print("Book added successfully.")

            elif command[1]=="update":
                books_id=command[2]
                print(book.to_dick())
                title=input("Title to be update : ")
                authors=input("Authors to be update: ")
                isbn=input("ISBN to be update: ")
                tags=input("Tags to be update: ")

                library1.update_book(books_id,
                    title=title or None,
                    authors=authors or None,
                    isbn=isbn or None,
                    tags=tags or None
                )
                print("Book updated Successfully.")
            
            elif command[1]=="remove":
                library1.remove_book(command[2])
                print("Book Removed Successfully.")
            
            elif command[1]=="get":
                book=library1.books.get(command[2])
                if not book:
                    print("Book doesn't exists")
                else:
                    print_book(book)
            elif command[1]=="list":
                for book in library1.books.values():
                    print_book(book)

            elif command[1] == "search":
                mode = command[2]
                text = " ".join(command[3:])
                if mode == "title":
                    add = library1.search_books(title=text)
                elif mode == "author":
                    add = library1.search_books(author=text)
                else:
                    add = library1.search_books(tag=text)
                for b in add:
                    print_book(b)
            
        elif command[0]=="user":
            user=library1.users.get(command[2])
            if command[1]=="add":
                user_id=print("User ID: ")
                name=print("Name: ")
                email=print("Email: ")
                library1.add_user(user_id,name,email)
                print("User added Successfully.")

            elif command[1]=="update":
                users_id=command[2]
                print(user.to_dick())

                name=input("name to be update : ")
                email=input("email to be update: ")
                if "@" not in email:
                    print("Invalid: missing @ symbol")
                elif "." not in email.split("@")[-1]:
                    print("Invalid: domain must contain a dot")
                else:
                    print("Valid email format!")

                library1.update_email(user_id,
                            name=name or None,
                            email=email or None
                )
                print("User updated Successfully.")
                
            elif command[1] == "get":
                users= library1.users.get(command[2])
                if not users:
                    print("User not found.")
                else:
                    print_user(users)
            
            elif command[1] == "list":
                for u in library1.users.values():
                    print_user(u)

            elif command[1] == "activate":
                library1.users[command[2]].activate()
                print("User activated.")

            elif command[1] == "deactivate":
                library1.users[command[2]].deactivate()
                print("User deactivated.")

            elif command[1] == "ban":
                library1.users[command[2]].ban()
                print("User banned.")
            
        elif command[0] == "borrow":
            txn, due = library1.borrow_book(command[1], command[2])
            print(f"Borrow successful. Transaction ID: {txn}. Due Date: {due}.")

        elif command[0] == "return":
            library1.return_book(command[1])
            print("Return successful.")\
            

        elif command[0] == "loans":
            if command[1] == "active":
                res = library1.active_loans()
                if not res: print("No active loans.")
                for t in res: print_tx(t)

            elif command[1] == "overdue":
                res = library1.overdue_loans()
                if not res: print("No overdue loans.")
                for t in res: print_tx(t)

            elif command[1] == "user":
                res = library1.user_history (command[2])
                for t in res: print_tx(t)

        
        elif command[0] == "report":

            if command[1] == "summary":
                print(f"Total books: {len(library1.books)}")
                print(f"Total users: {len(library1.users)}")
                print(f"Active loans: {len(library1.active_loans())}")
                print(f"Overdue loans: {len(library1.overdue_loans())}")

            elif command[1] == "user":
                res = library1.user_history(command[2])
                for t in res: print_tx(t)

        
        elif command[0] == "save":
            library1.save_all()
            print("All data saved to CSV successfully.")

        elif command[0] == "exit":
            print("Thank You!")
            break

    except Exception as e:
        print("An error occured:", e)
    





