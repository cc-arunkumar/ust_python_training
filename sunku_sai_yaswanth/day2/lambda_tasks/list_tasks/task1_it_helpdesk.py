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

tickets=["Email not working", "VPN issue", "System slow", "Password reset"]
tickets.append("Printer not responding")
tickets.remove( "System slow" )

tickets2=["Wi-Fi disconnected", "Laptop battery issue"]
tickets3=tickets+tickets2
print(tickets3)
print("Total open tickets=",len(tickets3))
sorted(tickets3)

print("Organized Ticket List:")
for ticket in tickets3:
    print(ticket)




# sample output
# Total open tickets= 6
# Organized Ticket List:
# Email not working
# VPN issue
# Password reset
# Printer not responding
# Wi-Fi disconnected
# Laptop battery issue