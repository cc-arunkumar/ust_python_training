
# Task 5: Customer Feedback Rating Analyzer

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





feedback = {"Arjun": 5,"Neha": 4,"Vikram": 3,"Ravi": 4,"Fatima": 5}
feedback["Priya"]=4
print(feedback)

if feedback["Ravi"]<5:
    feedback["Ravi"]+=1

for name, val in feedback.items():
    if val==5:
        print(name)


avg_rating = sum(feedback.values()) / len(feedback)
print("Average rating:", avg_rating)

rating_summary = {customer: ("Excellent" if rating >= 4 else "Needs Improvement")
                  for customer, rating in feedback.items()}

print("Rating summary:")
print(rating_summary)

# Sample Output
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Arjun
# Ravi
# Fatima
# Average rating: 4.333333333333333
# Rating summary:
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}