feedback = { "Arjun": 5, "Neha": 4, "Vikram": 3, "Ravi": 4, "Fatima": 5}
feedback["Priya"]=4
print("Updated Feedback:",feedback)
feedback["Ravi"]+=1
print("Updated Feedback after editing:",feedback)
for rating in feedback:
    if feedback[rating]>4:
        print(f"Employee:{rating} Rating:{feedback[rating]}")
print("Average Rating:",sum(feedback.values())/len(feedback))
result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}
print("Feedback Summary:", result)


# Updated Feedback: {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Updated Feedback after editing: {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 5, 'Fatima': 5, 'Priya': 4}
# Employee:Arjun Rating:5
# Employee:Ravi Rating:5
# Employee:Fatima Rating:5
# Average Rating: 4.333333333333333
# Feedback Summary: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}