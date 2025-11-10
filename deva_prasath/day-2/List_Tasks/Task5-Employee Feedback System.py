#Task 5: Employee Feedback System

week1=[4, 3, 5, 4, 2]
week2=[5, 4, 3, 5, 4]
all_ratings=week1+week2
print("Total ratings:",len(all_ratings))
print("Average ratings: ",sum(all_ratings)/len(all_ratings))
all_ratings.sort()
print("Sorted ratings: ",all_ratings)
filterd_list=[]
for i in all_ratings:
    if i>3:
        filterd_list.append(i)
print("Filtered rating(above 3): ",filterd_list)
print("Highest:",max(all_ratings))
print("Lowest:",min(all_ratings))
fin_avg=sum(filterd_list)/len(filterd_list)
print("Final Average:",round(fin_avg,2))


# Total ratings: 10
# Average ratings:  3.9
# Sorted ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered rating(above 3):  [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 2
# Final Average: 4.43

