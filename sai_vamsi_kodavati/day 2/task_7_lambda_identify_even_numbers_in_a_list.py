# TASK 2 Identify Even numbers in a list

employee_id = [101,102,103,104,105,106,107,108,109]
even_number = list(filter(lambda id:id%2 == 0,employee_id))
print(even_number)

# Sample Output
# [102, 104, 106, 108]