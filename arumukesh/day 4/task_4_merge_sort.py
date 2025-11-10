def merge(arr,left,mid,right):
    n1=mid-left+1
    n2=right-mid
    
    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=arr[left+i]
    for j in range(n2):
        R[j]=arr[mid+j+1]
    
    i,j,key=0,0,left
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            arr[key]=L[i]
            i+=1
        else:
            arr[key]=R[j]
            j+=1
        key+=1
    while i<n1:
            arr[key]=L[i]
            i+=1
            key+=1
    while j<n2:
            arr[key]=R[j]
            j+=1
            key+=1
        
         
    
def m_sort(arr,left,right):
        if left<right:
            mid=(right+left)//2
            m_sort(arr,left,mid)
            m_sort(arr,mid+1,right)
            merge(arr,left,mid,right)

arr=[2,4,25,7,5]
m_sort(arr,0,len(arr)-1)
print(arr)




    