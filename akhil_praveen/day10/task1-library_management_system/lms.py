# lms.py
from library import Library
from models import *


def main():
    lib = Library()
    print("---------------UST Library Management System----------------")

    while True:
        # print("Available commands:\n"
        #                   "book add\nbook update <id>\nbook get <id>\nbook list\n"
        #                   "user add\nuser get <id>\nuser deactivate <id>\n"
        #                   "borrow <user_id> <book_id>\nreturn <tx_id>\n"
        #                   "report summary\nsave\nexit")
        print("Available commands:\n"
                          "1. Books Services\n"
                          "2. Users Services\n"
                          "3. Borrow Book\n"
                          "4. Return Book\n"
                          "5. Report summary \n"
                          "6. save\n"
                          "7. exit\n")
        cmd = int(input("lms> "))

        if not cmd:
            continue

        try:
            match cmd:

                # ---------------- BOOK COMMANDS ----------------
                case 1:
                    print("Books Services:\n"
                        "   1. Add new book\n"
                        "   2. Update book details\n"
                        "   3. Get book details\n"
                        "   4. Remove a book\n"
                        "   5. List of book\n"
                        "   6. Back")
                    sub = int(input("   lms> "))

                    if sub == 1:
                        book_id = input("Book ID: ")
                        isbn=input("ISBN: ")
                        lib.validate(book_id,isbn)
                        title = input("Title: ")
                        authors = input("Authors (comma): ").split(",")
                        tags = input("Tags (comma): ").split(",")
                        total = int(input("Total copies: "))
                        data = {
                            "book_id": book_id,
                            "title": title,
                            "authors": authors,
                            "isbn": isbn,
                            "tags": tags,
                            "total_copies": total,
                            "available_copies": total
                        }
                        lib.add_book(data)
                        print("Book added.")

                    elif sub == 2:
                        book_id = input("       Enter book id: ")
                        print("Enter only the data which needs to be changed else leave blank!")
                        updates = {
                            "title": input("Title: ") or None,
                            "authors": input("Authors (comma): ").split(",") or None,
                            "isbn": input("ISBN: ") or None,
                            "tags": input("Tags (comma): ").split(",") or None
                        }
                        lib.update_book(book_id, updates)
                        print("Book updated.")

                    elif sub == 3:
                        book_id = input("       Enter book id: ")
                        b = lib.get_book(book_id)
                        print(b.to_dict())

                    elif sub == 4:
                        book_id = input("       Enter book id: ")
                        lib.remove_book(book_id)
                        print("Book removed.")

                    elif sub == 5:
                        for b in lib.books:
                            print(f"{b.book_id} -> {b.title}")

                # ---------------- USER COMMANDS ----------------

                case 2:
                    print("Books Services:\n"
                        "   1. Add new user\n"
                        "   2. Get user details\n"
                        "   3. Update user name"
                        "   4. List of book\n"
                        "   5. Deactivate a user\n"
                        "   6. Reactivate user"
                        "   7. Ban a user\n" 
                        "   8. Back\n")
                    sub = int(input("   lms> "))

                    if sub == 1:
                        data = {
                            "user_id": input("User ID: "),
                            "name": input("Name: "),
                            "email": input("Email: "),
                            "status": "active",
                            "max_loans": 5
                        }
                        lib.add_user(data)
                        print("User added.")

                    elif sub == 2:
                        user_id = input("       Enter user id: ")
                        u = lib.get_user(user_id)
                        print(u.to_dict())

                    elif sub == 3:
                        user_id = input("       Enter user id: ")
                        u = lib.get_user(user_id)
                        u.name = input("Name: ")
                        print("User updated.")

                    elif sub == 4:
                        for u in lib.users:
                            print(f"{u.user_id} -> {u.name}")

                    elif sub == 5:
                        user_id = input("       Enter user id: ")
                        lib.get_user(user_id).deactivate()
                        print("Deactivated.")

                    elif sub == 6:
                        user_id = input("       Enter user id: ")
                        lib.get_user(user_id).activate()
                        print("Activated.")

                    elif sub == 7:
                        user_id = input("       Enter user id: ")
                        lib.get_user(user_id).ban()
                        print("Banned.")

                # ---------------- BORROW / RETURN --------------
                case 3:
                    user_id = input("       Enter user id: ")
                    book_id = input("       Enter book id: ")
                    tx = lib.borrow_book(user_id, book_id)
                    print("Borrowed. TX:", tx.tx_id)

                case 4:
                    tx_id = input("       Enter transaction id: ")
                    tx = lib.return_book(tx_id)
                    print("Returned.")

                # ---------------- REPORTS ----------------
                case 5:
                    print(lib.report_summary())

                # ---------------- SAVE / EXIT ----------------
                case 6:
                    lib.save_all()
                    print("Saved.")

                case 7:
                    lib.save_all()
                    print("Goodbye!")
                    break

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
