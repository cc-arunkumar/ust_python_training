#Identify Even Numbers in a List

ids = [101, 102, 103, 104, 105, 106]
even_ids = list(filter(lambda x: x % 2 == 0, ids))
print(even_ids)
#sample execution
#[102, 104, 106]