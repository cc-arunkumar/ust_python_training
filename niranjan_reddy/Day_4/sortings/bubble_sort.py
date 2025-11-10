# Bubble Sort

list1=[23,3,45,1,34,43]
n=len(list1)
count=0

print("Before Sorting:",list1)
for i in range(n-1):
    for j in range(n-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            count+=1
    if(count==0):
        break

print("After Sorting:",list1)
    
# Sample Output

# Before Sorting: [23, 3, 45, 1, 34, 43]

# After Sorting: [1, 3, 23, 34, 43, 45]