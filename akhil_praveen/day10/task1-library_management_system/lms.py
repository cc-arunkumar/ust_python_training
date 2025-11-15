# lms.py
from library import Library
from models import *


def main():
    lib = Library()
    print("Library Management System (Type 'help' for commands)")

    while True:
        cmd = input("lms> ").strip().split()

        if not cmd:
            continue

        try:
            match cmd[0]:

                # ---------------- BOOK COMMANDS ----------------
                case "book":
                    sub = cmd[1]

                    if sub == "add":
                        data = {
                            "book_id": input("Book ID: "),
                            "title": input("Title: "),
                            "authors": input("Authors (comma): ").split(","),
                            "isbn": input("ISBN: "),
                            "tags": input("Tags (comma): ").split(","),
                            "total_copies": int(input("Total copies: ")),
                            "available_copies": int(input("Available copies: "))
                        }
                        lib.add_book(data)
                        print("Book added.")

                    elif sub == "update":
                        book_id = cmd[2]
                        updates = {
                            "title": input("Title: ") or None,
                            "isbn": input("ISBN: ") or None
                        }
                        lib.update_book(book_id, updates)
                        print("Book updated.")

                    elif sub == "get":
                        b = lib.get_book(cmd[2])
                        print(b.to_dict())

                    elif sub == "remove":
                        lib.remove_book(cmd[2])
                        print("Book removed.")

                    elif sub == "list":
                        for b in lib.books:
                            print(b.to_dict())

                # ---------------- USER COMMANDS ----------------

                case "user":
                    sub = cmd[1]

                    if sub == "add":
                        data = {
                            "user_id": input("User ID: "),
                            "name": input("Name: "),
                            "email": input("Email: "),
                            "status": "active",
                            "max_loans": 5
                        }
                        lib.add_user(data)
                        print("User added.")

                    elif sub == "get":
                        u = lib.get_user(cmd[2])
                        print(u.to_dict())

                    elif sub == "update":
                        u = lib.get_user(cmd[2])
                        u.name = input("Name: ")
                        print("User updated.")

                    elif sub == "deactivate":
                        lib.get_user(cmd[2]).deactivate()
                        print("Deactivated.")

                    elif sub == "activate":
                        lib.get_user(cmd[2]).activate()
                        print("Activated.")

                    elif sub == "ban":
                        lib.get_user(cmd[2]).ban()
                        print("Banned.")

                # ---------------- BORROW / RETURN --------------
                case "borrow":
                    tx = lib.borrow_book(cmd[1], cmd[2])
                    print("Borrowed. TX:", tx.tx_id)

                case "return":
                    tx = lib.return_book(cmd[1])
                    print("Returned.")

                # ---------------- REPORTS ----------------
                case "report":
                    if cmd[1] == "summary":
                        print(lib.report_summary())

                # ---------------- SAVE / EXIT ----------------
                case "save":
                    lib.save_all()
                    print("Saved.")

                case "exit":
                    lib.save_all()
                    print("Goodbye!")
                    break

                case "help":
                    print("Available commands:\n"
                          "book add\nbook update <id>\nbook get <id>\nbook list\n"
                          "user add\nuser get <id>\nuser deactivate <id>\n"
                          "borrow <user_id> <book_id>\nreturn <tx_id>\n"
                          "report summary\nsave\nexit")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
