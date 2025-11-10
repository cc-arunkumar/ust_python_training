claims_data = [
 ("E101", "C001", 3200, "Travel", "2025-11-02"),
 ("E101", "C002", 1800, "Food", "2025-11-03"),
 ("E102", "C003", 4500, "Hotel", "2025-11-02"),
 ("E103", "C004", 1200, "Travel", "2025-11-02"),
 ("E102", "C005", 2200, "Travel", "2025-11-04"),
 ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# claims = set()
total_rem = {}
for items in claims_data:
    # print(items[0])
    e_id,c_id,amount,travel,date=items
    if items[0] in total_rem:
        total_rem[e_id]+=amount
    else:
        total_rem[e_id]=amount


for items in total_rem:
    # print(items)
    if total_rem[items]>10000:
        print(items)

print(total_rem)

# print(claims_data[0])
avoid_duplicate=set()
elements=[]
# print(claims_data[0][0])
for items in claims_data:
    if items[0] not in avoid_duplicate:
        # print(items)
        elements.append(items)
        avoid_duplicate.add(items[0])

print(elements)




    
