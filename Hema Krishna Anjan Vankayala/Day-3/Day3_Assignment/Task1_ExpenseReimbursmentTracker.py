#Assignment 1 — Expense Reimbursement Tracker
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

new_data = {}
categories = set()
for data in claims_data:
    categories.add(data[3])
    if data[0] not in new_data.keys():
        new_data[data[0]]=data[2]
    else:
        new_data[data[0]] = data[2] + new_data.get(data[0])
print("Total Reimursement for Employees:",new_data)
# print("List of employees > 10000:")
# for data in new_data.items():
#     if data[1]>=10000:
#         print(data[0],"->",data[1])

print("Unique Categories:",categories)

#Sample Output
# Total Reimursement for Employees: {'E101': 9200, 'E102': 6700, 'E103': 1200}
# Unique Categories: {'Food', 'Travel', 'Hotel'}
