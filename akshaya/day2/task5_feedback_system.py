# Task 5: Employee Feedback System


week1 = [4, 3, 5, 4, 2]


week2 = [5, 4, 3, 5, 4]
all_ratings = week1 + week2

print("Total Ratings:", len(all_ratings))
print("Average Rating:", round(sum(all_ratings) / len(all_ratings), 2))


all_ratings.sort()
print("Sorted Ratings:", all_ratings)


filtered = [r for r in all_ratings if r > 3]


print("Filtered Ratings (above 3):", filtered)
print("Highest:", max(filtered))
print("Lowest:", min(filtered))
print("Final Average:", round(sum(filtered) / len(filtered), 2))

#sample output
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 4
# Final Average: 4.43
