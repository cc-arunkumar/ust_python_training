ids = [101, 102, 103, 104, 105, 106]
results = list(filter(lambda id: id%2==0,ids))
print(f"{results}")

# [102, 104, 106]