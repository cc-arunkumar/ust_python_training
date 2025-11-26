
list1=[16,14,5,6,8]
# output:[5,6,8,14,16]
key=0
# [14,16|,5,6,8]
for i in range(1,len(list1)):
    key= list1[i] #14-->5
    j=i-1 #0--->1
    while j>=0 and key<list1[j]: #16>14---->16>5
        list1[j+1]=list1[j] #[16,16,5,6,8]----->[14,16,16,6,8]
        j-=1  #-1--->0
    list1[j+1]=key #[14,16,5,6,8]---->[14,5,16,6,8]
       

print(list1)

# EXPECTED OUTPUT
# [5, 6, 8, 14, 16]


