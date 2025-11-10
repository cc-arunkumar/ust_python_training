# Expense_Reimbursement_Tracker

claim=7
claims_data = [
 ("E101", "C1", 3200, "Travel", "2025-11-02"),
 ("E101", "C2", 1800, "Food", "2025-11-03"),
 ("E102", "C3", 4500, "Hotel", "2025-11-02"),
 ("E103", "C4", 1200, "Travel", "2025-11-02"),
 ("E102", "C5", 2200, "Travel", "2025-11-04"),
 ("E101", "C6", 4200, "Hotel", "2025-11-05")
]
amount_per_emp={}

def read_claims():
    global claim
    global claims_data
    emp_id = input("Enter the employee id: ")
    amount = int(input("Enter the amount: "))
    cate = input("Enter the category: ")
    date = input("Enter the date(yyyy-mm-dd): ")
    claim+=1
    claims_data.append((emp_id,"C"+str(claim),amount,cate,date))
    print("Claim entered successfully!")

def cal_amount():
    global amount_per_emp
    
    for clm in claims_data:
        if clm[0] in amount_per_emp:
            amount_per_emp[clm[0]]+=clm[2]
        else:
            amount_per_emp[clm[0]]=clm[2]
    for i in amount_per_emp:
        print(f"{i} -> {amount_per_emp[i]}")
def list_emp():
    if len(amount_per_emp) == 0:
        print("Calculate total first! choice 2")
    else:
        print("List of employees whose total > ₹10,000")
        # print(amount_per_emp)
        for i in amount_per_emp:
            if amount_per_emp[i]>10000:
                print(i)
def set_cate():
    cate=set()
    for clm in claims_data:
        cate.add(clm[3])
    print(cate)

def display():
    for i in claims_data:
        print(i)
        print("")



print("=====  Expense Reimbursement Tracker =====")
print("1. Store claims")
print("2. Calculate total amount")
print("3. List of employees whose total > ₹10,000")
print("4. Set of all unique expense categories used")
print("5. Display all claims")
print("6. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice==1):
        read_claims()
    elif(choice==2):
        cal_amount()
    elif(choice==3):
        list_emp()
    elif(choice==4):
        set_cate()
    elif(choice==5):
        display()
    elif(choice==6):
        print("Thank you!")
        break
    else:
        print("Invalid choice please enter valid choice.")
    print("")


# =====  Expense Reimbursement Tracker =====
# 1. Store claims
# 2. Calculate total amount
# 3. List of employees whose total > ₹10,000
# 4. Set of all unique expense categories used
# 5. Display all claims
# 6. Exit
# Enter your choice: 1
# Enter the employee id: E101
# Enter the amount: 1245
# Enter the category: Food
# Enter the date(yyyy-mm-dd): 2025-11-7
# Claim entered successfully!

# Enter your choice: 2
# E101 -> 10445
# E102 -> 6700
# E103 -> 1200

# Enter your choice: 3
# List of employees whose total > ₹10,000
# E101

# Enter your choice: 4
# {'Travel', 'Hotel', 'Food'}

# Enter your choice: 5
# ('E101', 'C1', 3200, 'Travel', '2025-11-02')

# ('E101', 'C2', 1800, 'Food', '2025-11-03')

# ('E102', 'C3', 4500, 'Hotel', '2025-11-02')

# ('E103', 'C4', 1200, 'Travel', '2025-11-02')

# ('E102', 'C5', 2200, 'Travel', '2025-11-04')

# ('E101', 'C6', 4200, 'Hotel', '2025-11-05')

# ('E101', 'C8', 1245, 'Food', '2025-11-7')


# Enter your choice: 6
# Thank you!