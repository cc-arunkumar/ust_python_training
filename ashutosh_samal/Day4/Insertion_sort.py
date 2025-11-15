#insertion sort
arr=[5,3,6,9,1]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    
print(arr)


#Sample Execution
#[1, 3, 5, 6, 9]