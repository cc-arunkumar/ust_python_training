# Task 1:IT Helpdesk Ticket Manager
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

tickets = ["Email not working","VPN issue","System slow","Password reset"]

tickets.append("Printer not responding")

tickets.remove("System slow")

tickets.extend(["Wi-Fi disconnected","Laptop battery issue"])

total_tickets=len(tickets)
print(f"Total number of open tickets raised:{total_tickets}")

tickets.sort()

for i in range(0,total_tickets):
    print(tickets[i])

# EXPECTED OUTPUT
# Total number of open tickets raised:6
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected
