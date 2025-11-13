#Task Linear Search

arr=[34,22,56,67,89,76]
print("Given list ",arr)
target=int(input("Enter the element to search in the list"))
cout=0
for i in range(0,len(arr)):
    if(arr[i]==target):
        print("The element is found in the list")
        cout+=1
        break
if(cout==0):
    print("The element is not found")

#Sample Execution
# Given list  [34, 22, 56, 67, 89, 76]
# Enter the element to search in the list22
# The element is found in the list


    