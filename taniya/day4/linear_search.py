# Linear Search Implementation
numbers = [10, 20, 30, 45, 50, 75]   # List of numbers

# Take input from user for the target number
target = int(input("Enter number to search: "))

found = False   # Flag to check if element is found

# Loop through the list
for i in range(len(numbers)):
    # Compare each element with target
    if numbers[i] == target:
        print(f"{target} found at position {i}")  # Print index if found
        found = True
        break   # Exit loop once found

# If not found after loop ends
if not found:
    print(f"{target} not found in the list.")

# -------------------------
# Example Run (Input: 45)
# Enter number to search: 45
# 45 found at position 3
#
# Example Run (Input: 100)
# Enter number to search: 100
# 100 not found in the list.