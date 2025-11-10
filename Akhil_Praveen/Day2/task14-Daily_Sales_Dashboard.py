sales = [1200, 1500, 800, 2200, 1700, 950]
print("Total: ",sum(sales))
print("length: ",len(sales))
sales.append(1100)
sales.sort()
print(sales)
print("top: ",sales[-1:-4:-1])
print("lowest: ",sales[:2])
sales.pop(0)
print(sales)

# Total:  8350
# length:  6
# [800, 950, 1100, 1200, 1500, 1700, 2200]
# top:  [2200, 1700, 1500]
# lowest:  [800, 950]
# [950, 1100, 1200, 1500, 1700, 2200]