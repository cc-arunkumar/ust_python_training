sales =  [1200, 1500, 800, 2200, 1700, 950]
ans = sum(sales)
ans1 = ans/len(sales)
print(ans)
print(ans1)
sales.append(1100)
sales.sort()
print(sales)
print("Highest Sales",sales[-3:])
print("Lowest Sales",sales[:2])
del sales[0]
print(sales)


# ==============sample output=====================
# 8350
# 1391.6666666666667
# [800, 950, 1100, 1200, 1500, 1700, 2200]
# Highest Sales [1500, 1700, 2200]
# Lowest Sales [800, 950]
# [950, 1100, 1200, 1500, 1700, 2200]