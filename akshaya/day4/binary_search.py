#binary search
L = [18,5, 6, 8, 14, 16]
L.sort()  

def binary_search(target):
    S = 0
    E = len(L) - 1

    while S <= E:
        mid = (S + E) // 2    

        if L[mid] == target:
            print("Element found")
            break
        elif L[mid] < target:
            S = mid + 1           
        else:
            E = mid - 1         
    else:
        print("Element not found")

binary_search(8)

# sample output
# Element found
