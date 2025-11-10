#Task 1:IT Helpdesk Ticket Manager
# Scenario:
# You are developing a small internal IT Helpdesk system for your company.
# You need to manage the list of open support tickets throughout the day.

# Instructions:
    # 1. Create a list named tickets with the following ticket titles:
    # ["Email not working", "VPN issue", "System slow", "Password reset"]
    # 2. A new ticket "Printer not responding" arrives. Add it to the list.
    # (Hint: use append() )
    # 3. "System slow" issue has been resolved — remove it from the list.
    # (Hint: use remove() )
    # 4. Add two more tickets at once:
    # ["Wi-Fi disconnected", "Laptop battery issue"]
    # (Hint: use extend() )
    # 5. Display total number of open tickets.
    # (Hint: len() )
    # 6. Sort the tickets alphabetically to organize them better.
    # (Hint: sort() )
    # 7. Display all ticket names line by line using a loop.

# Expected Output(sample):
# Total open tickets: 5
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# Wi-Fi disconnected

tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
tickets.append("Printer Not Responding")
tickets.remove("System slow")
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
total_number_of_tickets = len(tickets)
sorted_tickets = sorted(tickets)
print("Total Open Tickets:", total_number_of_tickets)
print("Organized Ticket List:")
for ticket in sorted_tickets:
    print(ticket)

#Sample Output
# Total Open Tickets: 6
# Organized Ticket List:
# Email not working
# Laptop battery issue
# Password reset
# Printer Not Responding
# VPN issue
# Wi-Fi disconnected
