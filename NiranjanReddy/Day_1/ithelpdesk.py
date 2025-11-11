# Task 2: IT Helpdesk Ticket Menu
print("===== UST IT Helpdesk =====")
print("1. Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Account Issue")
print("4. View Total Tickets Raised")
print("5. Exit")
choice =int(input("Enter your choice: "))
hardware=0
software=0
account=0
while choice<=5:
    if choice==1:
        print("Hardware issue recorded. IT team will repond soon.")
        hardware+=1
    elif choice==2:
        print("Software issue recorded. IT team will repond soon.")
        software+=1
    elif choice==3:
        print("Account issue recorded. IT team will repond soon.")
        account+=1
    elif choice==4:
        print(f"Hardware Tickets: {hardware}")
        print(f"Software Tickets: {software}")
        print(f"Account Tickets: {account}")
        total=hardware+software+account
        print(f"Total Tickets Raised: {total}")
    else:
        print("Exiting Helpdesk. Thank you!")
        break
    choice =int(input("Enter your choice: "))
    
    

# sample output
# ===== UST IT Helpdesk =====
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Account Issue
# 4. View Total Tickets Raised
# 5. Exit
# Enter your choice: 1
# Hardware issue recorded. IT team will repond soon.
# Enter your choice: 2
# Software issue recorded. IT team will repond soon.
# Enter your choice: 3
# Account issue recorded. IT team will repond soon.
# Enter your choice: 4
# Hardware Tickets: 1
# Software Tickets: 1
# Account Tickets: 1
# Total Tickets Raised: 3
# Enter your choice: 5
# Exiting Helpdesk. Thank you!