# ----------------------insertionsort----------------------
list1=[5,3,6,1,9,1]
n=len(list1)
for i in range(n):
    j=i
    while j>0 and list1[j-1]>list1[j]:
        list1[j-1],list1[j]=list1[j],list1[j-1]
        j-=1
print("list1 after insertion sort:",list1)

# output
# list1 after insertion sort: [1, 1, 3, 5, 6, 9]
