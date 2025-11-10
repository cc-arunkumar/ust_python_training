# Task 5: Customer Feedback Rating
# Analyzer
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
# Dictionary Tasks 4
# 2. Add a new feedback: "Priya": 4 .
# 3. Increase Ravi’s rating by 1 (if not already 5).
# 4. Print all customers with a rating of 5.
# 5. Find the average rating of all customers.
# 6. Create a new dictionary using dictionary comprehension to store:
# key = customer name
# value = "Excellent" if rating ≥ 4, else "Needs Improvement" .
# 7. Print the new dictionary.

#Code:

feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}
feedback["Priya"]=4
feedback["Ravi"] += 1 if feedback["Ravi"] < 5 else 0
print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)
average_rating = sum(feedback.values()) / len(feedback)
print("Average Rating:", round(average_rating, 2))
feedback_status = {customer: ("Excellent" if rating >= 4 else "Needs Improvement") 
                   for customer, rating in feedback.items()}
print("Feedback Status:", feedback_status)

#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task5_Feedback_Rating.py
# Customers with rating 5:
# Arjun
# Ravi
# Fatima
# Average Rating: 4.33
# Feedback Status: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
# PS C:\Users\303379\day3_training>