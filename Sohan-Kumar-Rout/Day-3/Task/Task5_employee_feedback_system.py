# Task 5: Employee Feedback System

#Code
week1 =[4,3,5,4,2]
week2 =[5,4,3,5,4]

all_ratings = week1
all_ratings.extend(week2)
print("Total Ratings : ",len(all_ratings))
print("Average Rating : ",sum(all_ratings)/len(all_ratings))
all_ratings.sort()
print("Sorted Rating : ",all_ratings)
filter_rating =[]
for rate in all_ratings:
    if(rate>3):
        filter_rating.append(rate)
print("Filtered Ratings (above 3) : ",filter_rating)
highest_rating = max(filter_rating)
lowest_rating = min(filter_rating)
print("Highest Rating : ",highest_rating)
print("Lowest Rating : ",lowest_rating)
print("Final Average : ",sum(filter_rating)/len(filter_rating))

#Sample Output
# Total Ratings :  10
# Average Rating :  3.9
# Sorted Rating :  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3) :  [4, 4, 4, 4, 5, 5, 5]
# Highest Rating :  5
# Lowest Rating :  4
# Final Average :  4.428571428571429


