
#Task 2 Insertion Sort
ar=[44,32,56,21,4]
print("Given list: ",ar)
for i in range(1,len(ar)):
    temp=ar[i]
    j=i-1
    while(j>=0 and temp<ar[j]):
        ar[j+1]=ar[j]
        j-=1
        ar[j+1]=temp
print("Sorted it using Insertion sort",ar)

#Sample Execution
# Given list:  [44, 32, 56, 21, 4]
# Sorted it using Insertion sort [4, 21, 32, 44, 56]
