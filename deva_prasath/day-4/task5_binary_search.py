#Binary_search

def binary_search(a,search):
    left,right=0,len(a)
    while left<=right:
        mid=left+(right-left)//2
        if search==a[mid]:
            return mid
        elif a[mid]<search:
            left=mid+1
        else:
            right=mid-1
    return -1

a=[50,60,100,1,4]
search=60
print(f"The search element is present in the index: {binary_search(a,search)}")


#Sample output
# The search element is present in the index: 1

