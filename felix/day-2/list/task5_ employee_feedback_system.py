# employees feedback system

week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

all_ratings = week1 + week2

print("Total Ratings: ",len(all_ratings))
print("AverageRating: ",sum(all_ratings)/len(all_ratings))

all_ratings.sort()
print("Sorted Ratings: ",all_ratings)\

filtered = []
for rating in all_ratings:
    if rating>3:
        filtered.append(rating)
print("Filtered Ratings(above 3): ",filtered)

print("Highest: ",filtered[-1])
print("Lowest: ",filtered[0])

print("Final Average: ",sum(filtered)/len(filtered))

# output

# Total Ratings:  10
# AverageRating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings(above 3):  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4
# Final Average:  4.428571428571429