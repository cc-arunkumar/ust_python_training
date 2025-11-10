li=[1,2,2,12,13,14,6,7,19,15,11,10]

for i in range(1,len(li)):
    key = li[i]
    pos = i
    
    for j in range(i-1,-1,-1):
        if li[j]>key:
            li[j+1] = li[j]
            pos = j 
        else:
            break 
    li[pos] = key 
print(li)
