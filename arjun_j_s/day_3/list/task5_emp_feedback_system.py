#Task 5: Employee Feedback System
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
all_ratings = week1 + week2
print(f"Total Ratings : {len(all_ratings)}")
print(f"Average Ratings : {sum(all_ratings)/len(all_ratings)}")
all_ratings.sort()
print(f"Sorted Ratings : {all_ratings}")
filterd_rating = list(filter(lambda x: x>3,all_ratings))
print(f"Filtered Ratings (above 3) : {filterd_rating}")
print(f"Highest Ratings : {max(filterd_rating)}")
print(f"Lowest Rating : {min(filterd_rating)}")
print(f"Average Rating : {round(sum(filterd_rating)/len(filterd_rating),2)}")
#Output
# Total Ratings : 10
# Average Ratings : 3.9
# Sorted Ratings : [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3) : [4, 4, 4, 4, 5, 5, 5]
# Highest Ratings : 5
# Lowest Rating : 4
# Average Rating : 4.43