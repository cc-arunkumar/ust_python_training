#Binary Search
li=[10,20,30,40,50,60,70,80,90,100]
key=50
l=0
h=len(li)-1
b=True
while l<=h:
    mid=(l+h)//2
    if(li[mid]==key):
        b=False
        print("Element found at: ",mid)
        break
    elif(li[mid]>key):
        h=mid-1
    else:
        l=mid+1
if b:
    print("Element Not found")
    
#Sample output
#Element found at:  4