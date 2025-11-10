#Binary Search 
li=[1,2,3,4,12,54,23,77,31]
li=sorted(li)
search_ele = 54

s=0
e=len(li)-1
found = True
while(s<=e):
    mid = (s+e)//2
    if(li[mid]==search_ele):
        found = False
        print("Element found at: ",mid)
        break
    elif(li[mid]>search_ele):
        e = mid-1
    else:
        s = mid+1
if found:
    print("Element Not Found")

#Sample Output
# Element found at: 7