# Task 2: Employee Training Progress Tracker
# Scenario:
# You are tracking employees who have completed their mandatory “Cyber Security Awareness” training.

# Step 1: Create list of completed employees
completed = ["John", "Priya", "Amit"]

# Step 2: Add new employees who completed training
completed.append("Neha")
completed.append("Rahul")

# Step 3: Remove employee who left the company
completed.remove("Amit")

# Step 4: Create list of pending employees
pending = ["Meena", "Vivek", "Sita"]

# Step 5: Merge both lists
completed.extend(pending)

# Step 6: Sort alphabetically
completed.sort()

# Step 7: Print final list and count
print("All Employees (Completed + Pending):\n", completed)
print("Total Employees:", len(completed))


# Sample Output:
# All Employees (Completed + Pending):
# ['John', 'Meena', 'Neha', 'Priya', 'Rahul', 'Sita', 'Vivek']
# Total Employees: 7
