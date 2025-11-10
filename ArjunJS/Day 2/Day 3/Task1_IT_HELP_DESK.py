#Task 1:IT Helpdesk Ticket Manager
issues=["Email not working", "VPN issue", "System slow", "Password reset"]
issues.append("Printer not responding")
issues.remove("System slow")
issues.extend(["Wi-Fi disconnected", "Laptop battery issue"])
print(f"Total Open Tickets : {len(issues)}")
issues.sort()
print("Organized Ticket List : ")
for i in issues:
    print(i)
#Output
# Total Open Tickets : 6
# Organized Ticket List : 
# Email not working
# Laptop battery issue
# Password reset
# Printer not responding
# VPN issue
# Wi-Fi disconnected