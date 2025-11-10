tickets=["Email not working","VPN issue","System slow","Password reset"]
print(tickets)
tickets.append("Printer not responding")
print(tickets)
tickets.remove("System slow")
print(tickets)
wifi=["wifi disconnected","Laptop battery issue"]
tickets.extend(wifi)
print(tickets)
print (len(tickets))

for ticket in tickets:
    print(ticket)
