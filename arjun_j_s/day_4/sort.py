L=[5,3,6,2,9,1]
#Bubble Sort
n=len(L)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if(L[j]>L[j+1]):
#             L[j],L[j+1]=L[j+1],L[j]

#Insertion
for i in range(1,n):
    temp=L[i]
    for j in range(i-1,-1,-1):
        if(temp<L[j]):
            L[j],L[j+1]=L[j+1],L[j]
        else:
            break
print(L)