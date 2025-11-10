week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]


ratings = week1 + week2


total_ratings = len(ratings)
avg_rating = sum(ratings) / total_ratings

print("All Ratings:", ratings)
print("Total Ratings:", total_ratings)
print("Average Rating:", round(avg_rating, 2))


ratings.sort()
print("Sorted Ratings:", ratings)


filtered_ratings = [r for r in ratings if r >= 3]
print("Filtered Ratings:", filtered_ratings)


highest = max(filtered_ratings)
lowest = min(filtered_ratings)

final_average = sum(filtered_ratings) / len(filtered_ratings)

print("Highest Rating:", highest)
print("Lowest Rating:", lowest)
print("Final Average Rating:", round(final_average, 2))

# All Ratings: [4, 3, 5, 4, 2, 5, 4, 3, 5, 4]
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings: [3, 3, 4, 4, 4, 4, 5, 5, 5]
# Highest Rating: 5
# Lowest Rating: 3
# Final Average Rating: 4.11