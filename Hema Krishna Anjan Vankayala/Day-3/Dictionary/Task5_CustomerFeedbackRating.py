#Task 5: Customer Feedback Rating Analyzer

feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

feedback["Priya"]=4
feedback["Ravi"] = feedback.get("Ravi")+1 if feedback["Ravi"] < 5 else 0

sum_ratings =0
print("Customers with Ratings of 5:")
for key,value in feedback.items():
    sum_ratings += value
    if value==5:
        print(key)
print("Average Rating:",sum_ratings/len(feedback.items()))

new_dict = {}

for key,value in feedback.items():
    if value>=4:
        new_dict[key] = "Excellent"
    else:
        new_dict[key] = "Needs Improvement"
print(new_dict)

#Sample Output
# Customers with Ratings of 5:
# Arjun
# Ravi
# Fatima
# Average Rating: 4.333333333333333
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
