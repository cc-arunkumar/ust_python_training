# Task 1: Employee Access Control System
# Scenario:
# Your company maintains a set of employees who have access to the Production
# Server and another set for those who have access to the Testing Server.

# Step 1: Initialize sets for production and test environment access
prod_access = {"John", "Priya", "Amit", "Neha"}
test_access = {"Amit", "Neha", "Rahul", "Sita"}

# Step 2: Find users who have access to both environments
print("common users")
print(prod_access.intersection(test_access))  # Common users

# Step 3: Combine all users who have access to either environment
print("All unique users")
print(prod_access.union(test_access))  # All unique users

# Step 4: Find users who have access to production but not test
print("exclusive to prod_access")
print(prod_access.difference(test_access))  # Exclusive to prod_access

# Step 5: Add a new user to production access

prod_access.add("Ravi")

# Step 6: Remove a user from test access
test_access.discard("Rahul")  # Safe removal (no error if not present)

# Step 7: Create a sorted list of all users with any access
finalList = set(sorted(prod_access.union(test_access)))
print(f"print the sorted list: {finalList}")

# ===============sample output===================
# common users
# {'Amit', 'Neha'}
# All unique users
# {'Priya', 'Neha', 'John', 'Sita', 'Rahul', 'Amit'}
# exclusive to prod_access
# {'Priya', 'John'}
# print the sorted list: {'Neha', 'Priya', 'John', 'Sita', 'Ravi', 'Amit'}
