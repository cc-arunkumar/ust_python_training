#Task 5 Employee Feedback System
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
all_ratings=week1+week2
print("Total Ratings: ",len(all_ratings))
average_rating=sum(all_ratings)/len(all_ratings)
print("Average Rating: ",average_rating)
all_ratings.sort()
new_list=[]
for rating in all_ratings:
    if(rating>3):
        new_list.append(rating)
print("Sorted Ratings: ",all_ratings)
print("Filtered Ratings(above 3): ",new_list)
print("Highest: ",new_list[len(new_list)-1])
print("Lowest: ",new_list[0])
#Sample Executions
# Total Ratings:  10
# Average Rating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings(above 3):  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4

