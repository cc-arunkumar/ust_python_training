def linear(target):
    list1 = [5, 6, 8, 14, 16]
    f=0
    for i in list1:
        if i==target:
            print("Found no: ",i)
            f=1
            break
    if f==0:
        print("Not found",target)

linear(5)
linear(18)
#Output
# Found no:  5
# Not found 18