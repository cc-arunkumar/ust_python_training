#Insertion
L=[5,3,6,2,9,1]
print(L)
n=len(L)
for i in range(1,n):
    temp=L[i]
    for j in range(i-1,-1,-1):
        if(temp<L[j]):
            L[j],L[j+1]=L[j+1],L[j]
        else:
            break
print("Sorted : ",L)  

#Output
# [5, 3, 6, 2, 9, 1]
# Sorted :  [1, 2, 3, 5, 6, 9]