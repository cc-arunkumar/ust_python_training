# employee_feedback_system
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
all_ratings = week1+week2
print("Total: ",len(all_ratings))
print("Average: ",sum(all_ratings)/len(all_ratings))
all_ratings.sort()
print("Sorted Ratings: ",all_ratings)
filtered_ratings = list(filter(lambda rate:rate>3,all_ratings))
print("Filtered Ratings: ",filtered_ratings)
print("Highest: ",filtered_ratings[-1])
print("Lowest: ",filtered_ratings[0])
print("Final Average: ",sum(filtered_ratings)/len(filtered_ratings))

# Total:  10
# Average:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings:  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4
# Final Average:  4.428571428571429