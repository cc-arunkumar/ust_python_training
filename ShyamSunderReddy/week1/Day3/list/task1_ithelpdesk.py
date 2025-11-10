#Task 1:IT Helpdesk Ticket Manager
issues=["Email not working", "VPN issue", "System slow", "Password reset"]
issues.append( "Printer not responding")
issues.remove("System slow")
issues.extend(["Wi-Fi disconnected", "Laptop battery issue"]
)
print("Total open tickets: ",len(issues))
issues.sort()
for str in issues:
    print(str)

#sample output
#Total open tickets:  6
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected