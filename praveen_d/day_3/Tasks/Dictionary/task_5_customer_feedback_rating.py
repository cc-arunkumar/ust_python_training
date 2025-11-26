# Task 5: Customer Feedback Rating
# Update Ravi: feedback["Ravi"] += 1 if feedback["Ravi"] < 5 else 0
# Filter: [name for name, rate in feedback.items() if rate == 5]
# Average: sum(feedback.values()) / len(feedback)
# Comprehension:
# result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in fee
# dback.items()}


feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

feedback["Priya"]=4

if feedback["Ravi"]!=5:
    feedback["Ravi"]+=1

total_rating=0
for key,value in feedback.items():
    if value ==5:
        print(key)

    total_rating+=value

avg_rating=total_rating/len(feedback)

print(avg_rating)

result = {
    n: ("Excellent" if r >= 4 else "Needs Improvement") 
    for n, r in feedback.items()
    }

print(feedback)
print(result)

# EXPECTED OUTPUT
# Arjun
# Ravi
# Fatima
# 4.333333333333333
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 5, 'Fatima': 5, 'Priya': 4}
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
# PS C:\UST python> 