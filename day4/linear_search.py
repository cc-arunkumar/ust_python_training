numbers = [10,20,30,45,50,75]
target = int(input("enter number to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} found at position {i}")
        found = True
        break
if not found:
    print(f"{target} not found in the list.")