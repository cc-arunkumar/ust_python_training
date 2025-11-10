#Bubble Sort
L=[5,3,6,2,9,1]
print(L)
n=len(L)
for i in range(n-1):
    for j in range(n-i-1):
        if(L[j]>L[j+1]):
            L[j],L[j+1]=L[j+1],L[j]
print("Sorted : ",L)    

#Output
# [5, 3, 6, 2, 9, 1]
# Sorted :  [1, 2, 3, 5, 6, 9]