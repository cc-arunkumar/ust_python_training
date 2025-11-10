#Task 5: Employee Feedback System
week1=[4,3,5,4,2]
week2=[5,4,3,5,4]
week1.extend(week2)
all_ratings=[]
all_ratings.extend(week1)
total_no_of_ratings=len(all_ratings)
print("Total Ratings:",total_no_of_ratings)
avg_rating=sum(all_ratings)/len(all_ratings)
print("Average Ratings:",avg_rating)
all_ratings.sort()
print("Sorted Ratings:",all_ratings)

new_list=[]
for each_rating in all_ratings:
    if each_rating<=3:
        all_ratings.remove(each_rating)
    else:
        new_list.append(each_rating)
print("Filtered Ratings (above 3):",new_list)
print("Highest:",new_list[-1])
print("Lowest:",new_list[0])
final_avg=sum(new_list)/len(new_list)
print("Final Average:",final_avg)

'''
Total Ratings: 10
Average Ratings: 3.9
Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
Filtered Ratings (above 3): [4, 4, 4, 5, 5, 5]
Highest: 5
Lowest: 4
Final Average: 4.5
'''