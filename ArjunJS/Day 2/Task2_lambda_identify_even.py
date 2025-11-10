#Task 2: Identify Even Numbers in a List
ids = [101, 102, 103, 104, 105, 106]
even_ids=list(filter(lambda id:id%2==0,ids))
print(even_ids)
#Output
# [102, 104, 106]