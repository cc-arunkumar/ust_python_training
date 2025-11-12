# tickets = ["Email not working", "VPN issue", "System slow", "Password reset"]
# tickets.append("Printer not responding")
# tickets.pop(2)
# tickets.extend(["Wi-Fi disconnected", "Laptop battery issue"])
# tot = len(tickets)
# tickets.sort
# print("total open tickets:",tot)
# print("\nOrganized ticket list:")
# for tic in tickets:
#     print(tic)


completed = ["John", "Priya", "Amit"]
completed.extend(["neha","priya"])
completed.remove("Amit")

pending = ["Meena", "Vivek", "Sita"]
all_employee = completed+pending
print(all_employee)
all_employee.sort()
print("\nAll employees(completed+pending):")
count=0
for i in all_employee:
    print()
    count+=1
print("total employees:",count)
