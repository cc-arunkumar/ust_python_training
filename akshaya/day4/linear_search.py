#linear search
L=[3,2,4,8,7]
def linear(target):
    for i in L:
        if i==target:
            print("element found")
            break
    else:
        print("element not found")
linear(10)

#sample output
#element not found