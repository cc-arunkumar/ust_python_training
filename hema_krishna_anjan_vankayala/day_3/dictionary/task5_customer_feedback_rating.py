#Task 5: Customer Feedback Rating Analyzer

# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).
# Instructions:
# 1. Create the following dictionary:
# feedback = {
#  "Arjun": 5,
#  "Neha": 4,
#  "Vikram": 3,
#  "Ravi": 4,
#  "Fatima": 5
# }

# 2. Add a new feedback: "Priya": 4 .
# 3. Increase Ravi’s rating by 1 (if not already 5).
# 4. Print all customers with a rating of 5.
# 5. Find the average rating of all customers.
# 6. Create a new dictionary using dictionary comprehension to store:
# key = customer name
# value = "Excellent" if rating ≥ 4, else "Needs Improvement" .
# 7. Print the new dictionary.

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
