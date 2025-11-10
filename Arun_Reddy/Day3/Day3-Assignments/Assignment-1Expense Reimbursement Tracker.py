# employee reimbursement claims 
# employee={calimid,amount,category,date}
claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

employee_data=[]

def submit_employee(empid,cid,amount,category,date):
    employee_data.append({
    "Empid":empid,
    "Claimid":cid,
     "Amount":amount,
     "Category":category,
     "Date":date
     }
    )
employes=[]
submit_employee("E101", "C001", 3200, "Travel", "2025-11-02")
submit_employee("E101", "C002", 1800, "Food", "2025-11-03")
submit_employee("E102", "C003", 4500, "Hotel", "2025-11-02")
submit_employee("E103", "C004", 1200, "Travel", "2025-11-02")
submit_employee("E102", "C005", 2200, "Travel", "2025-11-04")

for k in employee_data:
        print(f"{k["Empid"]},{k["Claimid"]} {k["Amount"]} {k["Category"]} {k["Date"]}")
        if k["Amount"]>10000:
              employes.append(k["Empid"])
print(employes)

# total claim per emploee
my_dict={}
uniq_categ=set()
for k in employee_data:
      uniq_categ.add(k["Category"])
      empid=k["Empid"]
      if my_dict.get(empid):
            my_dict[empid]+=k["Amount"]
      else:
            my_dict[empid]=k["Amount"]
print(my_dict)
print(uniq_categ)

# ================Sample Execution================
# E101,C001 3200 Travel 2025-11-02
# E101,C002 1800 Food 2025-11-03
# E102,C003 4500 Hotel 2025-11-02
# E103,C004 1200 Travel 2025-11-02
# E102,C005 2200 Travel 2025-11-04
# []
# {'E101': 5000, 'E102': 6700, 'E103': 1200}
# {'Travel', 'Food', 'Hotel'}



    







