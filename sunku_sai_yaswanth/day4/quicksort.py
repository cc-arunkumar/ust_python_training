# -------------------quicksort------------------------
def quick_sort(sort):
    if len(sort) <= 1:
        return sort
    pivot = sort[len(sort) // 2]
    left = [x for x in sort if x < pivot]
    middle = [x for x in sort if x == pivot]
    right = [x for x in sort if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sort=[12,1,23,2,45,6,8,2,0]

sorted_arr = quick_sort(sort)
print(f"Sorted array: {sorted_arr}")

# øutput
# Sorted array: [0, 1, 2, 2, 6, 8, 12, 23, 45]