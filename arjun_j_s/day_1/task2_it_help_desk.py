# Task 2: IT Helpdesk Ticket Menu
issues={
    "hardware":0,
    "software":0,
    "network":0,
    "total":0
}
ch='Y'
while(ch=='Y' or ch=='y'):
    print("====== UST IT Helpdesk ======")
    print("1. Raise Hardware Issue")
    print("2. Raise Software Issue")
    print("3. Raise Network Issue")
    print("4. View Total Tickets Raised")
    print("5. Exit")
    n=int(input("Choose choice:"))
    if(n==1):
        issues["hardware"]+=1
        issues["total"]+=1
        print("Hardware issue recorded. IT team will respond soon.")
    elif(n==2):
        issues["software"]+=1
        issues["total"]+=1
        print("Software issue recorded. IT team will respond soon.")
    elif(n==3):
        issues["network"]+=1
        issues["total"]+=1
        print("Network issue recorded. IT team will respond soon.")
    elif(n==4):
        print(f"Hardware Tickets:{issues["hardware"]}")
        print(f"Software Tickets:{issues["software"]}")
        print(f"Network Tickets:{issues["network"]}")
        print(f"Total Tickets Raised:{issues["total"]}")
    elif(n==5):
        print("Exiting Helpdesk. Thank you!")
        break
    else:
        print("Provide a number within range!!")
    ch=input("\nDo you wish to continue(Y/N)")
#Output
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Choose choice:1
# Hardware issue recorded. IT team will respond soon.

# Do you wish to continue(Y/N)y
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Choose choice:2
# Software issue recorded. IT team will respond soon.

# Do you wish to continue(Y/N)y
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Choose choice:3
# Network issue recorded. IT team will respond soon.

# Do you wish to continue(Y/N)y
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Choose choice:4
# Hardware Tickets:1
# Software Tickets:1
# Network Tickets:1
# Total Tickets Raised:3

# Do you wish to continue(Y/N)y
# ====== UST IT Helpdesk ======
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets Raised
# 5. Exit
# Choose choice:5
# Exiting Helpdesk. Thank you!