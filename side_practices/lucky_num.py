def lucky_num(arr):
    tot_count = 0
    
    for num in arr:
        count = 0
        n = arr

def main():
    n = int(input("Enter the size of array:"))
    arr = []
    for _ in range(n):
        arr.append(int(input))
    res = lucky_num(arr)
    print(res)
if __name__ == "__main__":
    main()