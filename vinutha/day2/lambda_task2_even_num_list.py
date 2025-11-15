# Task 2: Identify Even Numbers in a List
# You have a list of employee IDs, and you need to filter out only even IDs for an internal audit.
# Requirement:
# Use a lambda function with the filter() method to select even IDs.
# Example Input:
# ids = [101, 102, 103, 104, 105, 106]
# Expected Output:
# [102, 104, 106]
# (Hint: Use filter(lambda x: condition, list))

#Code

# Create a list of IDs
ids = [101, 102, 103, 104, 105, 106]

# Use the filter() function with a lambda expression to select only even IDs
# lambda X: X % 2 == 0 → returns True if X is divisible by 2 (i.e., even), otherwise False
# filter() applies this condition to each element in 'ids'
# list() converts the filtered result into a list
even_ids = list(filter(lambda X: X % 2 == 0, ids))

# Print the list of even IDs
print(even_ids)


#output
# PS C:\Users\Administrator\Desktop\Training\vinutha\ust_python_training> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/vinutha/ust_python_training/Vinutha/day2/lambda_task2_even_num_list.py
# [102, 104, 106]
# PS C:\Users\Administrator\Desktop\Training\vinutha\ust_python_training> 

