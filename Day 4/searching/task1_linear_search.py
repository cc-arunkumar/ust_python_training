#linear search

list=[33,70,1,22]

element=int(input("Enter target element:"))

for i,j in enumerate(list):
    if j==element:
        print(f"Element Found at the index of {i}")
        break

# sample output:
# Enter target element:70
# Element Found at the index of 1

    