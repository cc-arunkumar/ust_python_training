linearsearh=[0,4,56,3,12,56]
target=56

flag=False
for i in range(0,len(linearsearh)):
    found_index=i
    if linearsearh[i]==target:
        print(f"element is found:{linearsearh[i]} at index {i}")
        flag=True
if flag==False:
    print("Element is not found")

# output
# element is found:56 at index 2
# element is found:56 at index 5
        
        

