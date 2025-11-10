arr=[50,60,100,1,4]
n=len(arr)
# for i in range(n):
#     j=i
#     while j>0 and a[j-1]>a[j]:
#         a[j],a[j-1]=a[j-1],a[j]
#         j-=1
# print(a)



for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

print("Sorted array:",arr)


# Sample output
# Sorted array: [1, 4, 50, 60, 100]
