#Task 2: Identify Even Numbers in a List

employee_id = [101,102,103,104,105,106]
even_ids = list(filter(lambda ids:ids%2==0,employee_id))
print(even_ids)

#Sample Execution
# [102, 104, 106]