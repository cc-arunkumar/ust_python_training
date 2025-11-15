#Linear Search

# List of elements
a = [50, 60, 100, 1, 4]

# Element to search in the list
search = 100

# Loop through the list to find the element
for i in range(len(a)):
    if search == a[i]:  # If the element is found
        print(f"The element is: {search} present at {i}")  # Print the element and its index


##Sample output
#The element is:100 present at 2
