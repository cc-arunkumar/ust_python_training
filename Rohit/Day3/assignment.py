# Step 1: Initialize claims data as a list of tuples
claims_data = [
    ("E101", "C001", 3200, "Travel", "2025-11-02"),
    ("E101", "C002", 1800, "Food", "2025-11-03"),
    ("E102", "C003", 4500, "Hotel", "2025-11-02"),
    ("E103", "C004", 1200, "Travel", "2025-11-02"),
    ("E102", "C005", 2200, "Travel", "2025-11-04"),
    ("E101", "C006", 4200, "Hotel", "2025-11-05")
]

# Step 2: Initialize dictionary to store total reimbursement per employee
total_rem = {}

# Step 3: Aggregate claim amounts by employee ID
for items in claims_data:
    e_id, c_id, amount, travel, date = items
    if e_id in total_rem:
        total_rem[e_id] += amount
    else:
        total_rem[e_id] = amount

# Step 4: Print employee IDs with total claims exceeding ₹10,000

for e_id in total_rem:
    if total_rem[e_id] > 10000:
        print(e_id)

# Step 5: Print the total reimbursement dictionary
print("Print the total reimbursement dictionary")
print(total_rem)

# Step 6: Initialize set to track unique employee IDs and list for first claims
avoid_duplicate = set()
elements = []

# Step 7: Extract first claim entry for each unique employee
for items in claims_data:
    if items[0] not in avoid_duplicate:
        elements.append(items)
        avoid_duplicate.add(items[0])

# Step 8: Print the list of first claims per employee
print("the list of first claims per employee")
print(elements)


# =====sample input============
# Print the total reimbursement dictionary
# {'E101': 9200, 'E102': 6700, 'E103': 1200}
# the list of first claims per employee
# [('E101', 'C001', 3200, 'Travel', '2025-11-02'), ('E102', 'C003', 4500, 'Hotel', '2025-11-02'), ('E103', 'C004', 1200, 'Travel', '2025-11-02')]
