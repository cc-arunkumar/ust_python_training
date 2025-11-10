list1=[2,9,10,23,78,90]
l=0
h=len(list1)-1
target=90

while l<=h:
    mid=(l+h)//2
    if list1[mid]==target:
        print("Target element:",list1[mid])
        break
    elif list1[mid]>target:
        h=mid-1
    elif list1[mid]<target:
        l=mid+1
        
        