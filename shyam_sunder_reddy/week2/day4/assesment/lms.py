import library, utils
import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display welcome banner"""
    clear_screen()
    print("=" * 60)
    print("🎓  WELCOME TO THE LIBRARY MANAGEMENT SYSTEM (LMS)  🎓")
    print("=" * 60)
    print()

def display_main_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("📚 MAIN MENU")
    print("=" * 60)
    print("1. 📖 MANAGE BOOKS")
    print("2. 👤 MANAGE USERS")
    print("3. 🔄 BORROW/RETURN BOOKS")
    print("4. 📋 VIEW LOANS & REPORTS")
    print("5. ℹ️  HELP & INFORMATION")
    print("6. � EXIT")
    print("=" * 60)

def display_book_menu():
    """Display book management menu"""
    print("\n" + "=" * 60)
    print("📖 BOOK MANAGEMENT")
    print("=" * 60)
    print("1. ➕ Add a New Book")
    print("2. 🔄 Update Book Details")
    print("3. ❌ Remove a Book")
    print("4. 🔍 Search for a Book")
    print("5. 📄 View Book Details")
    print("6. 📚 List All Books")
    print("7. 🔙 Back to Main Menu")
    print("=" * 60)

def display_user_menu():
    """Display user management menu"""
    print("\n" + "=" * 60)
    print("👤 USER MANAGEMENT")
    print("=" * 60)
    print("1. ➕ Add a New User")
    print("2. 🔄 Update User Details")
    print("3. 👁️  View User Details")
    print("4. 👥 List All Users")
    print("5. 🔓 Activate User")
    print("6. 🔒 Deactivate User")
    print("7. 🚫 Ban User")
    print("8. 🔙 Back to Main Menu")
    print("=" * 60)

def display_transaction_menu():
    """Display transaction menu"""
    print("\n" + "=" * 60)
    print("🔄 BORROW / RETURN BOOKS")
    print("=" * 60)
    print("1. 📤 Borrow a Book")
    print("2. 📥 Return a Book")
    print("3. 🔙 Back to Main Menu")
    print("=" * 60)

def display_loans_menu():
    """Display loans and reports menu"""
    print("\n" + "=" * 60)
    print("📋 LOANS & REPORTS")
    print("=" * 60)
    print("1. 📌 View Active Loans")
    print("2. ⏰ View Overdue Loans")
    print("3. 📜 View Loan History")
    print("4. 📊 Generate Summary Report")
    print("5. 👤 Generate User Report")
    print("6. 🔙 Back to Main Menu")
    print("=" * 60)

def manage_books():
    """Book management section"""
    while True:
        display_book_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            # Add Book
            print("\n📝 ADD NEW BOOK")
            print("-" * 40)
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            authors = input("Enter Author(s) (separated by | ): ").strip()
            isbn = input("Enter ISBN: ").strip()
            tags = input("Enter Tags (separated by | ): ").strip()
            try:
                total_copies = int(input("Enter Total Copies: ").strip())
                available_copies = int(input("Enter Available Copies: ").strip())
                
                dict_book = {
                    "book_id": book_id,
                    "title": title,
                    "authors": authors,
                    "isbn": isbn,
                    "tags": tags,
                    "total_copies": total_copies,
                    "available_copies": available_copies
                }
                result = library.add_book(dict_book)
                print(f"\n✅ {result}")
            except ValueError:
                print("\n❌ Please enter valid numbers for copies.")
        
        elif choice == "2":
            # Update Book
            print("\n🔄 UPDATE BOOK DETAILS")
            print("-" * 40)
            book_id = input("Enter Book ID to update: ").strip()
            print("(Leave blank to keep current value)")
            title = input("Enter Book Title: ").strip()
            authors = input("Enter Author(s): ").strip()
            isbn = input("Enter ISBN: ").strip()
            tags = input("Enter Tags: ").strip()
            total_copies = input("Enter Total Copies: ").strip()
            available_copies = input("Enter Available Copies: ").strip()
            
            update_data = {}
            if title:
                update_data["title"] = title
            if authors:
                update_data["authors"] = authors
            if isbn:
                update_data["isbn"] = isbn
            if tags:
                update_data["tags"] = tags
            if total_copies:
                try:
                    update_data["total_copies"] = int(total_copies)
                except ValueError:
                    print("\n❌ Invalid number for total copies.")
                    continue
            if available_copies:
                try:
                    update_data["available_copies"] = int(available_copies)
                except ValueError:
                    print("\n❌ Invalid number for available copies.")
                    continue
            
            result = library.update_book(book_id, **update_data)
            print(f"\n✅ {result}")
        
        elif choice == "3":
            # Remove Book
            print("\n❌ REMOVE BOOK")
            print("-" * 40)
            book_id = input("Enter Book ID to remove: ").strip()
            result = library.remove_book(book_id)
            print(f"\n✅ {result}")
        
        elif choice == "4":
            # Search Book
            print("\n🔍 SEARCH FOR BOOKS")
            print("-" * 40)
            keyword = input("Enter search keyword (title, author, or tags): ").strip()
            results = library.search_books(keyword)
            if results:
                print("\n📚 SEARCH RESULTS:")
                print("-" * 40)
                for i, book in enumerate(results, 1):
                    print(f"{i}. ID: {book['book_id']} | Title: {book['title']}")
                    print(f"   Author(s): {book['authors']}")
                    print(f"   Available: {book['available_copies']}/{book['total_copies']}")
                    print()
            else:
                print("\n❌ No books found matching your search.")
        
        elif choice == "5":
            # Get Book Details
            print("\n📖 VIEW BOOK DETAILS")
            print("-" * 40)
            book_id = input("Enter Book ID: ").strip()
            book = library.get_book(book_id)
            if isinstance(book, dict):
                print("\n📚 BOOK INFORMATION:")
                print("-" * 40)
                for key, value in book.items():
                    print(f"{key.upper()}: {value}")
            else:
                print(f"\n❌ {book}")
        
        elif choice == "6":
            # List All Books
            books = library.list_books()
            if books:
                print("\n📚 ALL BOOKS IN LIBRARY:")
                print("-" * 60)
                print(f"{'ID':<10} {'Title':<25} {'Author(s)':<15} {'Available':<10}")
                print("-" * 60)
                for book in books:
                    title = book['title'][:23] if len(book['title']) > 23 else book['title']
                    authors = book['authors'][:13] if len(book['authors']) > 13 else book['authors']
                    available = f"{book['available_copies']}/{book['total_copies']}"
                    print(f"{book['book_id']:<10} {title:<25} {authors:<15} {available:<10}")
            else:
                print("\n❌ No books in the library.")
        
        elif choice == "7":
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

def manage_users():
    """User management section"""
    while True:
        display_user_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            # Add User
            print("\n👤 ADD NEW USER")
            print("-" * 40)
            user_id = input("Enter User ID: ").strip()
            name = input("Enter User Name: ").strip()
            email = input("Enter Email: ").strip()
            status = input("Enter Status (active/inactive/banned): ").strip().lower()
            try:
                max_loans = int(input("Enter Max Loans (default 5): ").strip() or "5")
                
                dict_user = {
                    "user_id": user_id,
                    "name": name,
                    "email": email,
                    "status": status if status in ['active', 'inactive', 'banned'] else 'active',
                    "max_loans": max_loans
                }
                result = library.add_user(dict_user)
                print(f"\n✅ {result}")
            except ValueError:
                print("\n❌ Please enter valid information.")
        
        elif choice == "2":
            # Update User
            print("\n🔄 UPDATE USER DETAILS")
            print("-" * 40)
            user_id = input("Enter User ID to update: ").strip()
            print("(Leave blank to keep current value)")
            name = input("Enter User Name: ").strip()
            email = input("Enter Email: ").strip()
            status = input("Enter Status (active/inactive/banned): ").strip()
            max_loans = input("Enter Max Loans: ").strip()
            
            update_data = {}
            if name:
                update_data["name"] = name
            if email:
                update_data["email"] = email
            if status:
                update_data["status"] = status
            if max_loans:
                try:
                    update_data["max_loans"] = int(max_loans)
                except ValueError:
                    print("\n❌ Invalid number for max loans.")
                    continue
            
            result = library.update_user(user_id, **update_data)
            print(f"\n✅ {result}")
        
        elif choice == "3":
            # Get User Details
            print("\n👁️  VIEW USER DETAILS")
            print("-" * 40)
            user_id = input("Enter User ID: ").strip()
            user = library.get_user(user_id)
            if isinstance(user, dict):
                print("\n👤 USER INFORMATION:")
                print("-" * 40)
                for key, value in user.items():
                    print(f"{key.upper()}: {value}")
            else:
                print(f"\n❌ {user}")
        
        elif choice == "4":
            # List All Users
            print("\n👥 USER LISTING OPTIONS")
            print("-" * 40)
            print("1. Show Only ACTIVE Users")
            print("2. Show ALL Users (including inactive/banned)")
            list_choice = input("Enter your choice (1-2): ").strip()
            
            if list_choice == "1":
                users = library.list_active_users()
                if users:
                    print("\n✅ ACTIVE USERS IN SYSTEM:")
                    print("-" * 80)
                    print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Status':<10} {'Loans':<5}")
                    print("-" * 80)
                    for user in users:
                        print(f"{user['user_id']:<10} {user['name']:<20} {user['email']:<25} {user['status']:<10} {user.get('active_loans', 0):<5}")
                    print("-" * 80)
                else:
                    print("\n❌ No active users in the system.")
            
            elif list_choice == "2":
                users = library.list_all_users_with_status()
                if users:
                    print("\n📋 ALL USERS IN SYSTEM:")
                    print("-" * 90)
                    print(f"{'ID':<10} {'Name':<20} {'Email':<25} {'Status':<12} {'Loans':<5}")
                    print("-" * 90)
                    for user in users:
                        status = user['status']
                        icon = "✅" if status == "active" else "❌" if status == "banned" else "⏸️"
                        print(f"{user['user_id']:<10} {user['name']:<20} {user['email']:<25} {status:<12} {user.get('active_loans', 0):<5}  {icon}")
                    print("-" * 90)
                else:
                    print("\n❌ No users in the system.")
            else:
                print("\n❌ Invalid choice.")
        
        elif choice == "5":
            # Activate User
            print("\n🔓 ACTIVATE USER")
            print("-" * 40)
            user_id = input("Enter User ID to activate: ").strip()
            result = library.activate_user(user_id)
            print(f"\n✅ {result}")
        
        elif choice == "6":
            # Deactivate User
            print("\n🔒 DEACTIVATE USER")
            print("-" * 40)
            user_id = input("Enter User ID to deactivate: ").strip()
            result = library.deactivate_user(user_id)
            print(f"\n✅ {result}")
        
        elif choice == "7":
            # Ban User
            print("\n🚫 BAN USER")
            print("-" * 40)
            user_id = input("Enter User ID to ban: ").strip()
            result = library.ban_user(user_id)
            print(f"\n✅ {result}")
        
        elif choice == "8":
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

def manage_transactions():
    """Transaction management section"""
    while True:
        display_transaction_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            # Borrow Book
            print("\n📤 BORROW A BOOK")
            print("-" * 40)
            user_id = input("Enter User ID: ").strip()
            book_id = input("Enter Book ID to borrow: ").strip()
            result = library.borrow_book(book_id, user_id)
            print(f"\n✅ {result}")
        
        elif choice == "2":
            # Return Book
            print("\n📥 RETURN A BOOK")
            print("-" * 40)
            book_id = input("Enter Book ID to return: ").strip()
            user_id = input("Enter User ID: ").strip()
            result = library.return_book(book_id, user_id)
            print(f"\n✅ {result}")
        
        elif choice == "3":
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

def manage_loans_reports():
    """Loans and reports section"""
    while True:
        display_loans_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            # Active Loans
            print("\n📌 ACTIVE LOANS")
            print("-" * 40)
            user_id = input("Enter User ID (or press Enter for all): ").strip()
            if user_id:
                result = library.view_active_loans(user_id)
                print(f"\n{result}")
            else:
                users = library.list_users()
                print("\n📌 ALL ACTIVE LOANS:")
                print("-" * 60)
                for user in users:
                    print(f"User: {user['name']} (ID: {user['user_id']}) - Active Loans: {user.get('active_loans', 0)}")
        
        elif choice == "2":
            # Overdue Loans
            print("\n⏰ OVERDUE LOANS")
            print("-" * 40)
            user_id = input("Enter User ID (or press Enter for all): ").strip()
            if user_id:
                result = library.view_overdue_loans(user_id)
                if result:
                    print(f"\n{result}")
                else:
                    print("\n✅ No overdue loans for this user.")
            else:
                print("\n⏰ CHECKING ALL OVERDUE LOANS...")
        
        elif choice == "3":
            # Loan History
            print("\n📜 LOAN HISTORY")
            print("-" * 40)
            user_id = input("Enter User ID: ").strip()
            history = library.view_loan_history(user_id)
            if history:
                print(f"\n📜 LOAN HISTORY FOR {user_id}:")
                print("-" * 60)
                for tx in history:
                    print(tx)
            else:
                print(f"\n❌ No loan history found for user {user_id}.")
        
        elif choice == "4":
            # Summary Report
            print("\n📊 GENERATING SUMMARY REPORT...")
            print("-" * 40)
            books = library.list_books()
            users = library.list_users()
            print(f"\n📊 LIBRARY SUMMARY REPORT:")
            print("-" * 40)
            print(f"Total Books: {len(books)}")
            print(f"Total Users: {len(users)}")
            total_copies = sum(int(b.get('total_copies', 0)) for b in books)
            available_copies = sum(int(b.get('available_copies', 0)) for b in books)
            print(f"Total Copies Available: {available_copies}/{total_copies}")
            print(f"Active Users: {len([u for u in users if u.get('status') == 'active'])}")
        
        elif choice == "5":
            # User Report
            print("\n👤 GENERATE USER REPORT")
            print("-" * 40)
            user_id = input("Enter User ID: ").strip()
            user = library.get_user(user_id)
            if isinstance(user, dict):
                print(f"\n👤 USER REPORT FOR {user_id}:")
                print("-" * 40)
                for key, value in user.items():
                    print(f"{key.upper()}: {value}")
                history = library.view_loan_history(user_id)
                if history:
                    print(f"\nLoan History: {len(history)} transactions")
            else:
                print(f"\n❌ {user}")
        
        elif choice == "6":
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

def display_help_menu():
    """Display help and information"""
    print("\n" + "=" * 60)
    print("ℹ️  HELP & INFORMATION")
    print("=" * 60)
    utils.display_help()
    input("\nPress Enter to continue...")

# Main Application Loop
def main():
    display_welcome()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            manage_books()
        elif choice == "2":
            manage_users()
        elif choice == "3":
            manage_transactions()
        elif choice == "4":
            manage_loans_reports()
        elif choice == "5":
            display_help_menu()
        elif choice == "6":
            print("\n" + "=" * 60)
            print("👋 THANK YOU FOR USING LIBRARY MANAGEMENT SYSTEM!")
            print("=" * 60)
            print("Data saved. Goodbye! 📚")
            utils.save_data()
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("Please try again.")# import library as library
# import utils as utils
 
# command=""
# while command!="exit":
#     command=input("lms> ")
   
#     # Add Book
#     if command.lower().strip()=="book add":
#         book_id= input("Enter Book ID: ")
#         title= input("Enter Book Title: ")
#         author= input("Enter Book Author (separated by | ): ")
#         isbn= input("Enter Book ISBN: ")
#         tags= input("Enter Book Tags (separated by | ): ")
#         total_copies= int(input("Enter Total Copies: "))
#         available_copies= int(input("Enter Available Copies: "))
#         dict_book={"book_id":book_id,"title":title,"author":author,"isbn":isbn,"tags":tags,"total_copies":total_copies,"available_copies":available_copies}
#         library.cmd_book_add(dict_book)
   
#     # Update Book
#     elif command.lower().strip()=="book update":
#         book_id= input("Enter Book ID to update: ")
#         print("Enter new details (leave blank to keep current value):")
#         title= input("Enter Book Title: ")
#         author= input("Enter Book Author (separated by | ): ")
#         isbn= input("Enter Book ISBN: ")
#         tags= input("Enter Book Tags (separated by | ): ")
#         total_copies= input("Enter Total Copies: ")
#         available_copies= input("Enter Available Copies: ")
#         update_data={}
#         if title:
#             update_data["title"]=title
#         if author:
#             update_data["author"]=author
#         if isbn:
#             update_data["isbn"]=isbn
#         if tags:
#             update_data["tags"]=tags
#         if total_copies:
#             update_data["total_copies"]=int(total_copies)
#         if available_copies:
#             update_data["available_copies"]=int(available_copies)
#         library.cmd_book_update(book_id,**update_data)
   
#     # Remove Book
#     elif command.lower().strip()=="book remove":
#         book_id= input("Enter Book ID to remove: ")
#         library.book_remove(book_id)
   
#     # Get Book Details
#     elif command.lower().strip()=="book get":
#         book_id= input("Enter Book ID to get details: ")
#         library.get_book(book_id)
   
#     # list Book Details
#     elif command.lower().strip()=="book list":
#         library.book_list()
   
#     # search Book
#     elif command.lower().strip()=="book search":
#         keyword= input("Enter keyword to search in title, author or tags: ")
#         library.search_books(keyword)
   
#     # Add User
#     elif command.lower().strip()=="user add":
#         user_id= input("Enter User ID: ")
#         name= input("Enter User Name: ")
#         email= input("Enter User Email: ")
#         status= input("Enter User Status (active/inactive/banned): ")
#         max_loans= int(input("Enter User Max Loans: "))
#         dict_user={"user_id":user_id,"name":name,"email":email,"status":status,"max_loans":max_loans}
#         library.add_user(dict_user)
   
#     # Update User
#     elif command.lower().strip()=="user update":
#         user_id= input("Enter User ID to update: ")
#         print("Enter new details (leave blank to keep current value):")
#         name= input("Enter User Name: ")
#         email= input("Enter User Email: ")
#         status= input("Enter User Status (active/inactive/banned): ")
#         max_loans= input("Enter User Max Loans: ")
#         update_data={}
#         if name:
#             update_data["name"]=name
#         if email:
#             update_data["email"]=email
#         if status:
#             update_data["status"]=status
#         if max_loans:
#             update_data["max_loans"]=int(max_loans)
#         library.update_user(user_id,**update_data)
   
#     #Get Users Details
#     elif command.lower().strip()=="user get":
#         user_id= input("Enter User ID to get details: ")
#         library.get_user(user_id)
   
#     #list Users Details
#     elif command.lower().strip()=="user list":
#         library.list_users()
   
#     # Deactivate User
#     elif command.lower().strip()=="user deactivate":
#         user_id= input("Enter User ID to deactivate: ")
#         library.deactivate_user(user_id)
   
#     # Activate User
#     elif command.lower().strip()=="user activate":
#         user_id= input("Enter User ID to activate: ")
#         library.activate_user(user_id)
   
#     # Ban User
#     elif command.lower().strip()=="user ban":
#         user_id= input("Enter User ID to ban: ")
#         library.ban_user(user_id)
   
#     #Borrow Book
#     elif command.lower().strip()=="borrow":
#         user_id= input("Enter User ID: ")
#         book_id= input("Enter Book ID to borrow: ")
#         library.borrow_book(user_id,book_id)
   
#     #Return Book
#     elif command.lower().strip()=="return":
#         txn_id= input("Enter Transaction ID to return book: ")
#         library.return_book(txn_id)
   
#     #loans active
#     elif command.lower().strip()=="loans active":
#         user_id= input("Enter User ID to view active loans: ")
#         library.view_active_loans(user_id)
   
#     #loans overdue
#     elif command.lower().strip()=="loans overdue":
#         user_id= input("Enter User ID to view overdue loans: ")
#         library.view_overdue_loans(user_id)
   
#     #loans history
#     elif command.lower().strip()=="loans history":
#         user_id= input("Enter User ID to view loan history: ")
#         library.view_loan_history(user_id)
   
#     #utils help
#     elif command.lower().strip()=="help":
#         utils.display_help()
   
#     #save data
#     elif command.lower().strip()=="save":
#         utils.save_data()
       
#     #exit
#     elif command.lower().strip()!="exit":
#         break
   
#     else:
#         print("Invalid command. Type 'help' for a list of commands.")