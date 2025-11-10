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

ids=[101,102,103,104,105,106]
even_ids=list(filter(lambda X:X%2==0,ids))
print(even_ids)

#output
# PS C:\Users\Administrator\Desktop\Training\vinutha\ust_python_training> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/vinutha/ust_python_training/Vinutha/day2/lambda_task2_even_num_list.py
# [102, 104, 106]
# PS C:\Users\Administrator\Desktop\Training\vinutha\ust_python_training> 

