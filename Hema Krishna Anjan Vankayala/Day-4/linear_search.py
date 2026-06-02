li=[1,2,3,4,12,54,23,45,77]
search_ele = 54
if search_ele in li:
    for i in range(len(li)):
        if li[i]==search_ele:
            print(f"{search_ele} is Found at {i} index")
else:
    print("Element Not Found")
