a=[50,60,100,1,4]
n=len(a)
Boolean=False
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            Boolean=True
    if Boolean==False:
        break
print("Sorted array:",a)

# Sample output
# Sorted array: [1, 4, 50, 60, 100]






