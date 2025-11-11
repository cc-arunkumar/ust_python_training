# Task 5: Employee Feedback System
week1_ratings = [4, 3, 5, 4, 2]
week2_ratings = [5, 4, 3, 5, 4]
all_ratings=week1_ratings+week2_ratings
total=len(all_ratings)
print("Total Ratings:",total)
average=sum(all_ratings)/total
print("Average Ratings:",average)
all_ratings.sort()
print("Sorted Ratings:",all_ratings)
good_rating=[]
for rating in all_ratings:
    if rating>3:
        good_rating.append(rating)
print("Filtered Ratings (above 3):",good_rating)
print("Highest:",good_rating[-1])
print("Lowest:",good_rating[0])
final_average=sum(good_rating)/len(good_rating)
print(f"Final Average: {final_average:.2f}")
# Sample output
# Total Ratings: 10
# Average Ratings: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 4
# Final Average: 4.43