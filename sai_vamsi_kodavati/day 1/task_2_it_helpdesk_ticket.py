# TASK-2 IT Helpdesk Ticket

print("Hello")
tickets = 0

print("1.Raise Hardware Issue")
print("2.Raise Software Issue")
print("3.Raise Network Issue")
print("4.Raise View Total Tickets Raised")
print("5.Exit")

htickets = 0
stickets = 0
ntickets = 0

while True:
    tickets = htickets + stickets + ntickets

    issue = int(input("Enter your choice: "))

    if(issue == 1):
        print("Hardware issue recorded.IT team will respond soon")
        htickets += 1
    elif(issue == 2):
        print("Software issue recorded.IT team will respond soon")
        stickets += 1

    elif(issue == 3):
        print("Network issue recorded.IT team will respond soon")
        ntickets += 1

    elif(issue == 4):
        print("Hardware Tickets: ",htickets)
        print("Software Tickets: ",stickets)
        print("Network Ticket: ",ntickets)
        print("total tickets",tickets)

    elif(issue == 5):
        print("Exiting Helpdesk! Thank You")
        

    else:
        print("Invalid Choice")
        break

# Sample Output

# Hello
# 1.Raise Hardware Issue
# 2.Raise Software Issue
# 3.Raise Network Issue
# 4.Raise View Total Tickets Raised
# 5.Exit
# Enter your choice: 1
# Hardware issue recorded.IT team will respond soon
# Enter your choice: 2
# Software issue recorded.IT team will respond soon
# Enter your choice: 3
# Network issue recorded.IT team will respond soon
# Enter your choice: 4
# Hardware Tickets:  1
# Software Tickets:  1
# Network Ticket:  1
# total tickets 3
# Enter your choice: 5
# Exiting Helpdesk! Thank You
# Enter your choice: 6
# Invalid Choice



