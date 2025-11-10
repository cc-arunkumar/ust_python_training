# Task 2: IT Helpdesk Ticket Menu
# Objective:
# Simulate a basic IT Helpdesk system where employees can raise hardware, software, or network issues,
# and track the total number of tickets raised.

Total_Tickets_Raised = 0

while True:
    print("====== UST IT Helpdesk ======")
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Hardware issue recorded. IT team will respond soon.")
        Total_Tickets_Raised += 1   

    elif choice == '2':
        print("Software issue recorded. IT team will respond soon.")
        Total_Tickets_Raised += 1   

    elif choice == '3':
        print("Network issue recorded. IT team will respond soon.")
        Total_Tickets_Raised += 1  

    elif choice == '4':
        print(f"Total Tickets Raised so far: {Total_Tickets_Raised}")

    elif choice == '5':
        print("Thank you! Have a great day.")
        break

    else:
        print("Invalid choice. Please try again.")




#     ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 2
# Software issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 3
# Network issue recorded. IT team will respond soon.

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 4
# Total Tickets Raised so far: 3

# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 5
# Thank you! Have a great day.
