# 6. Print all unique employee names who are enrolled in any course (no
# duplicates).
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
# 7. Print the new dictionary
feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}

feedback["Priya"] = 4
if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1

for name, rate in feedback.items():
    if rate == 5:
        print(name)

avg = sum(feedback.values()) / len(feedback)
print("Average:", avg)

new_feedback = {}
for name, rate in feedback.items():
    if rate >= 4:
        new_feedback[name] = "Excellent"
    else:
        new_feedback[name] = "Needs Improvement"

print(new_feedback)
# sample output
# Arjun
# Ravi
# Fatima
# Average: 4.333333333333333
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}