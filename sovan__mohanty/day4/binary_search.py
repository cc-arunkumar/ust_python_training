#Task Binary Search
ar=[34,55,67,32,21]
print("Given list: ",ar)
start=0
end=len(ar)
mid=(start+end)//2
target=int(input("Enter the element to search in the list"))
cout=0
while(start<=end):
    if(ar[mid]==target):
        print("The element is found in the list")
        cout+=1
        break
    elif(target>ar[mid]):
        start=mid
        start+=1
    elif(target<ar[mid]):
        end=mid
        end-=1
    mid=(start+end)//2
if(cout==0):
    print("The element is not found in the list")

#Sample Execution
# Given list:  [34, 55, 67, 32, 21]
# Enter the element to search in the list34
# The element is found in the list
