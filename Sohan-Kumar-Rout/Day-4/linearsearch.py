#Task : Linear Search

#Code
arr=[4,2,7,9,3]
tar=9

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
result = linear_search(arr,tar)
print("Index in which the Target is found is : ",result)

#output
# Index in which the Target is found is :  3