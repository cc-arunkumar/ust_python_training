# TASK 5 -  Employee Feedback System

week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

all_ratings = week1 + week2

print("Total Ratings: ",len(all_ratings))

total_sum = sum(all_ratings)

print("Average Rating: ",total_sum/len(all_ratings))

all_ratings.sort()
print("Sorted Ratings: ",all_ratings)

filtered_rating = []
for i in all_ratings:
    if i > 3:
        filtered_rating.append(i)

print("Filtered Ratings (above 3): ",filtered_rating)
print("Highest: ",max(filtered_rating))
print("Lowest: ",min(filtered_rating))
total = sum(filtered_rating)
print("Final Average: ",total/len(filtered_rating))

# Sample Output
# Total Ratings:  10
# Average Rating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3):  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4
# Final Average:  4.428571428571429





