# it_helpdesk_ticket_manager
tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
print(tickets)
tickets.append( "Printer not responding")
print(tickets)
tickets.remove("System slow")
print(tickets)
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
print(tickets)
print(len(tickets))
tickets.sort()
print(tickets)
for ticket in range(len(tickets)):
    print(tickets[ticket])

# ['Email not working', 'VPN issue', 'System slow', 'Password reset']
# ['Email not working', 'VPN issue', 'System slow', 'Password reset', 'Printer not responding']
# ['Email not working', 'VPN issue', 'Password reset', 'Printer not responding']
# ['Email not working', 'VPN issue', 'Password reset', 'Printer not responding', 'Wi-Fi disconnected', 'Laptop battery issue']
# 6
# ['Email not working', 'Laptop battery issue', 'Password reset', 'Printer not responding', 'VPN issue', 'Wi-Fi disconnected']
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected