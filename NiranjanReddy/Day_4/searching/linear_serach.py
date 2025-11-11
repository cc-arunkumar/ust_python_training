# linear Search

arr=[3,5,23,45,54,67,90,455]

target=90

for num in range(len(arr)):
    if target==arr[num]:
        print("The target index in the array is:",num)
        break

else:
    print("Index Not found")

# Sample output
# The target index in the array is: 6