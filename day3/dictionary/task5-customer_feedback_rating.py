# Task 5: Customer Feedback Rating 
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