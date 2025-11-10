tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
print(tickets)

tickets.append("Printer not responding")  
print(tickets)

tickets.remove("System slow")  
print(tickets)

list2 = ["Wi-Fi disconnected", "Laptop battery issue"]
tickets.extend(list2)  
print(tickets)

print(len(tickets))  

sort = sorted(tickets)
print(sort)

for tkt in tickets:
    print(tkt)

