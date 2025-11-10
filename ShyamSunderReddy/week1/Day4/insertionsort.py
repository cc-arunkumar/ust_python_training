l=[5,3,6,2,9,1]
#Using for loops
for i in range(1,len(l)):
    key=l[i]
    flag=i
    for k in range(i-1,-1,-1):
        if l[k]>key:
            l[k+1]=l[k]
            flag=k
        else:
            break
    l[flag]=key
print(l)

#Using while
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while key<l[j] and j>=0:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)