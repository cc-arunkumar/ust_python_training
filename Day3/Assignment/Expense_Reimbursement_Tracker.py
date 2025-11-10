claims = []
claim_id = 1
while(True):
    print("1.Submit claim\n2.Exit")
    choice = int(input("Enetr choice: "))
    if choice == 1:
        emp_id = input("Employee ID: ")
        amount = int(input("Amount: "))
        category = input("Category: ")
        date = input("Date: ")

        claims.append((emp_id,"C00"+str(claim_id),amount,category,date))
        claim_id += 1
    elif choice == 2:
        break
    print("\n")

employee_claim_amount = {}
for i in claims:
    employee_claim_amount[i[0]] = employee_claim_amount.get(i[0],0) + i[2]
print(employee_claim_amount)

list = []
for i in employee_claim_amount:
    if employee_claim_amount[i]>10000:
        list.append(i)

print("List of employees whose total >10000: ",list)

category1 = []
for i in claims:
    category1.append(i[3])

unique_category = set(category1)
print("Unique category: ",unique_category)


# output

# 1.Submit claim
# 2.Exit
# Enetr choice: 2
# {'E101': 5000, 'E103': 4700, 'E102': 12200}
# List of employees whose total >10000:  ['E102']
# Unique category:  {'Food', 'Travel', 'Hotel'}