arr = [7,24,83,45,10,98,56]

target = 10
flag=0
for i in range(len(arr)):
    if arr[i] == target:
        flag=1
        print(f"{target} is present at index {i}")
        break
if flag == 0:
    print(f"{target} is not in array")
    
# output

# 10 is present at index 4