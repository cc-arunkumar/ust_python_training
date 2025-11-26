list=[10,11,15,20,25]
target=15
is_found=False
for i in range(len(list)):
    if(target==list[i]):
        print(f"Index:{i}")
        is_found=True
if is_found==False:
    print("Target not found")

# EXPECTED OUTPUT:
# Index:2
