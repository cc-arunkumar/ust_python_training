#QuickSort
L=[5,3,6,2,9,1]
print(L)
start=0
n=len(L)-1
def part(L,start,end):
    pivot=L[end]
    i=start-1
    for j in range(start,end):
        if(L[j]<=pivot):
            i+=1
            L[i],L[j]=L[j],L[i]  
    L[i+1],L[end]=L[end],L[i+1]
    return i+1
def quicksort(L,start,end):
    if(start<end):
        pos = part(L,start,end)
        quicksort(L,start,pos-1)
        quicksort(L,pos+1,end)

quicksort(L,start,n) 
print(L)
#Output
# [5, 3, 6, 2, 9, 1]
# [1, 2, 3, 5, 6, 9]
    
    
    