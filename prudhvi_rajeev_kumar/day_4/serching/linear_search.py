def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
        
arr = [1, 3, 2, 67, 34, 23]
target = 23
result = linear_search(arr, target)
print("The target value 23 is in index : ", result)

#Sample Output
#The target value 23 is in index :  5
