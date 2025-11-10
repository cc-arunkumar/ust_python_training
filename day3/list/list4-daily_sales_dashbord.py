# Task 4: Daily Sales Dashboard
sales=[1200, 1500, 800, 2200, 1700, 950]
total=sum(sales)
print("Total sales:",total)
length=len(sales)
avg=total/length
print("Average sales:",avg)
sales.append(1100)
sort_asc=sorted(sales)
print("Sorted Sales:",sort_asc)
print("Top 3 sales:",sort_asc[-3:])
print("lowest 2 sales:",sort_asc[:2])
sort_asc.pop(0)
print("Updated Sales after removing smallest:",sort_asc)



# Total sales: 8350
# Average sales: 1391.6666666666667
# Sorted Sales: [800, 950, 1100, 1200, 1500, 1700, 2200]
# Top 3 sales: [1500, 1700, 2200]
# lowest 2 sales: [800, 950]
# Updated Sales after removing smallest: [950, 1100, 1200, 1500, 1700, 2200]