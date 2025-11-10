def binary(target):
    list1 = [18,5, 6, 8, 14, 16] 
    list1.sort()
    l=0
    r=len(list1)-1
    mid=(l+r)//2
    f=0
    while l<=r:
        if list1[mid]==target:
            print("Found no: ",target)
            f=1
            break
        elif list1[mid]>target:
            r=mid-1
        else:
            l=mid+1
        mid=(l+r)//2
    if f==0:
        print("Not found",target)

binary(5)
binary(18)
#Output
# Found no:  5
# Found no:  18 