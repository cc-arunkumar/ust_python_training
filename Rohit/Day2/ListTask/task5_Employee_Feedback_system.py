week1 =[4, 3, 5, 4, 2]

week2 = [5, 4, 3, 5, 4]
list.extend(week1,week2)
all_ratings = week1
print(all_ratings)
print(sum(all_ratings))
print(sum(all_ratings)/len(all_ratings))

all_ratings.sort()
print(all_ratings)
# filterSalary= list(filter(lambda sal: sal>50000 , salaries))
# print(bonus)

filtering = list(filter(lambda x:x>3,all_ratings))
print("All ratings after filtering",filtering)
print("Final average after cleaning",sum(filtering)/len(filtering))


# ================sample output=================

# [4, 3, 5, 4, 2, 5, 4, 3, 5, 4]
# 39
# 3.9
# [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# All ratings after filtering [4, 4, 4, 4, 5, 5, 5]
# Final average after cleaning 4.428571428571429 