claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
 ]
total_reim={}
expense_ctg=set()
data_set=set()
for eid,cid,amt,catgry,date in claims_data:
    if cid not in data_set:
        data_set.add(cid)
        expense_ctg.add(catgry)
    if eid not in total_reim:
        total_reim[eid]=0
    total_reim[eid]+=amt
    

for eid,total in total_reim.items():
    print(f"{eid} : Rs{total}")

for eid,total in total_reim.items():
    if total>10000:
        print(eid)
        
print(expense_ctg)

#  Total reimbursement per employee
# E101 : Rs9200
# E102 : Rs6700
# E103 : Rs1200

# Set of all unique expense categories used
# {'Food', 'Hotel', 'Travel'}