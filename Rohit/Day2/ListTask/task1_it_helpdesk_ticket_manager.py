from os import remove

tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
new_ticket  = "System slow"
tickets.append(new_ticket)
tickets.remove("System slow")
tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
print(tickets)
print(len(tickets))
tickets.sort()
print(tickets)



# ===============sample output=================
# ['Email not working', 'VPN issue', 'Password reset', 'System slow', 'Wi-Fi disconnected', 'Laptop battery 
# issue']
# 6
# ['Email not working', 'Laptop battery issue', 'Password reset', 'System slow', 'VPN issue', 'Wi-Fi disconnected']