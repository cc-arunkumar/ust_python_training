# IT Helpdesk Ticket Manager
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
# 7. Display all ticket names line by line using a loop


tickets=["Email not working","VPN issue","system slow","password reset"]
tickets.append("printer not responding")
tickets.remove("system slow")
tickets.extend(["wifi disconnected","laptop battery issue"])
print("total open tickets:",len(tickets))
tickets.sort()
print("organized ticket list:")
for ticket in tickets:
    print(ticket)


#o/p:
#total open tickets: 6
#organized ticket list:
#Email not working
#VPN issue
#laptop battery issue
#password reset
#printer not responding
#wifi disconnected