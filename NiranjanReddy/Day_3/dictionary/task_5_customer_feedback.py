# Task 5: Customer Feedback Rating Analyzer
feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

# 2. Add a new feedback: "Priya": 4 
feedback["Priya"]=4



print("After adding priya:", feedback)

# 3. Increase Ravi’s rating by 1 (if not already 5)
if feedback["Ravi"]!=5:
    feedback["Ravi"]+=1

print("Increase Ravi’s rating by 1: ",feedback)


# 4. Print all customers with a rating of 5
ratings=[name for name, rate in feedback.items() if rate == 5]

print(ratings)

# 5. Find the average rating of all customers.
for key,values in feedback.items():
    average=sum(feedback.values()) / len(feedback)
print("Avarage:",average)

# 6. Create a new dictionary using dictionary comprehension to store:
result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}

print(result)


# # Sample Output
# After adding priya: {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Increase Ravi’s rating by 1:  {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 5, 'Fatima': 5, 'Priya': 4}
# ['Arjun', 'Ravi', 'Fatima']
# Avarage: 4.333333333333333
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}



