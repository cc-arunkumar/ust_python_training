week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

all_ratings = week1 + week2

total_ratings = len(all_ratings)
average_rating = sum(all_ratings) / total_ratings

print("All Ratings:", all_ratings)
print("Total Ratings:", total_ratings)
print("Average Rating:", round(average_rating, 2))


all_ratings.sort()
print("Sorted Ratings:", all_ratings)


filtered_ratings = [r for r in all_ratings if r >= 3]
print("Filtered Ratings:", filtered_ratings)


highest = max(filtered_ratings)
lowest = min(filtered_ratings)

final_average = sum(filtered_ratings) / len(filtered_ratings)

print("Highest Rating:", highest)
print("Lowest Rating:", lowest)
print("Final Average Rating:", round(final_average, 2))