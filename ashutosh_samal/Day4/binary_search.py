list=[1,2,3,4,5,6,7]
key=5
l=0
h=len(list)-1
b=True
while l<=h:
    mid=(l+h)//2
    if(list[mid]==key):
        b=False
        print("Element found at: ",mid)
        break
    elif(list[mid]>key):
        h=mid-1
    else:
        l=mid+1
if b:
    print("Element Not found")
    
#output
#Element found at:  4