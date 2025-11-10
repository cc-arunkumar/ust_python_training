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

feedback["Ravi"]+=1
# . Find the average rating of all customers.
print(feedback)
for key,values in feedback.items():
    average = sum(feedback.values()) / len(feedback)
print("Average rating: ",average)


#  Print all customers with a rating of 5
for names,ratings in feedback.items():
    if ratings==5:
        print(names)

#  Create a new dictionary using dictionary comprehension to store:
result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}

print(result)

# output
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 5, 'Fatima': 5, 'Priya': 4}
# Average rating:  4.333333333333333
# Arjun
# Ravi
# Fatima
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}