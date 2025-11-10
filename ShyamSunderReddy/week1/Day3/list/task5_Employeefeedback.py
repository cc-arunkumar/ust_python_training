#Task 5: Employee Feedback System
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
week1.extend(week2)
all_rating=week1
print("Total Ratings: ",len(all_rating))
print("Average Rating: ",sum(all_rating)/len(all_rating))
all_rating.sort()
print("Sorted Ratings: ",all_rating)
all_rating=list(filter(lambda x:x>3,all_rating))
print("Filtered Ratings (above 3): ",all_rating)
print("Highest: ",all_rating[0])
print("Lowest: ",all_rating[len(all_rating)-1])
print("Final Average: ",sum(all_rating)/len(all_rating))

#Sample output
# Total Ratings:  10
# Average Rating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]     
# Filtered Ratings (above 3):  [4, 4, 4, 4, 5, 5, 5]  
# Highest:  4
# Lowest:  5
# Final Average:  4.428571428571429