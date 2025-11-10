arr = [13,15,43,34,24,53,64]

target = 24
left = 0
right = len(arr) - 1
flag = 0
while(left<right):
    mid = (left + right)//2
    if arr[mid] == target:
        print(f"{target} is found at index {mid}")
        flag = 1
        break
    elif arr[mid] > target:
        left = mid-1
    else:
        right = mid+1

if flag == 0:
    print(f"{target} is not in array")
    
# output

# 24 is found at index 4