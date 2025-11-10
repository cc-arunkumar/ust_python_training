sales = [1200, 1500, 800, 2200, 1700, 950]
total = sum(sales)
print(total)
length = len(sales)
average = total / length
print(average)

sales.append(1100)
print(sales)
sort = sorted(sales)
print(sort)

sort_desc = sorted(sales, reverse=True)
top_three = sort[-3:]
print(top_three)

low = sort[:2]
print(low)

sort_desc.pop()
print(sort_desc)
