week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

week1.extend(week2) 
all_ratings =week1

total_ratings = len(all_ratings)
average_rating = sum(all_ratings) / total_ratings
print("Total Ratings:", total_ratings)
print("Average Rating:", average_rating)

all_ratings.sort()
print("Sorted Ratings:", all_ratings)

filtered_ratings = [r for r in all_ratings if r > 3]
print("Filtered Ratings (Above 3):", filtered_ratings)

highest_rating = max(filtered_ratings)
lowest_rating = min(filtered_ratings)
print("Highest Rating:", highest_rating)
print("Lowest Rating:", lowest_rating)

final_average = sum(filtered_ratings) / len(filtered_ratings)
print("Final Average Rating:", final_average)


# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (Above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest Rating: 5
# Lowest Rating: 4
# Final Average Rating: 4.428571428571429