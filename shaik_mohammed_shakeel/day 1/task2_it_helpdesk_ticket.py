
# Task 2: IT Helpdesk Ticket Menu
# Objective: 
# 	Create a command-line helpdesk ticket system for employees to raise and track IT issues such as hardware, software, or network problems.

print("UST IT Helpdesk")
print("1. Raise Hardware Issue")
print("2. Raise Software Issue")
print("3. Raise Network Issue")
print("4. View Total Tickets")
print("5. Exit")
hwtick=0
swtick=0
nwtick=0

while True:
    count=hwtick+swtick+nwtick
    a=int(input("Enter Your Choice: "))
    if (a==1):
        print("Hardware issue recorded. IT team will respond soon.")
        hwtick+=1
    elif (a==2):
        print("Software issue recorded. IT team will respond soon.")
        swtick+=1
    elif (a==3):
        print("Network issue recorded. IT team will respond soon.")
        nwtick+=1
    elif(a==4):
        print("Hardware Tickets: ",hwtick)
        print("Software Tickets: ",swtick)
        print("Network Tickets: ",nwtick)
        print("Total Tickets Raised",count)
    elif(a==5):
        print("Exiting Helpdesk. Thank you")
        break
    else:
        print("Invalid Number")


# Sample Output
# UST IT Helpdesk
# 1. Raise Hardware Issue
# 2. Raise Software Issue
# 3. Raise Network Issue
# 4. View Total Tickets
# 5. Exit
# Enter Your Choice: 1
# Hardware issue recorded. IT team will respond soon.
# Enter Your Choice: 3
# Network issue recorded. IT team will respond soon.
# Enter Your Choice: 4
# Hardware Tickets:  1
# Software Tickets:  0
# Network Tickets:  1
# Total Tickets Raised 2
# Enter Your Choice: 5
# Exiting Helpdesk. Thank you