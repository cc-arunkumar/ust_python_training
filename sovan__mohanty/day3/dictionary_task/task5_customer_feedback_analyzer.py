#Task5 Customer Feedback Analyzer

feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}
feedback["Priya"]=4
feedback["Ravi"] += 1 if feedback["Ravi"] < 5 else 0
filt=[name for name, rate in feedback.items() if rate == 5]
avg=sum(feedback.values()) / len(feedback)
result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}
print(result)

#Sample Executions
#{'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}

