"""
Task 5: Customer Feedback Rating Analyzer
Scenario:
Your customer service team collects feedback in a dictionary form
where key = customer name, value = their rating (out of 5).

"""

# Dictionary storing customer feedback ratings
feedback={
"Arjun":5,
"Neha":4,
"Vikram":3,
"Ravi":4,
"Fatima":5
}

# Add a new customer's rating
feedback["Priya"]=4

# Increment Ravi's rating by 1 if less than 5
if feedback["Ravi"]<5:
    feedback["Ravi"]+=1

# List of customers with a perfect rating of 5
five_star=[n for n,r in feedback.items() if r==5]
print("Customers with Rating 5:",five_star)

# Calculate and print average rating
avg=sum(feedback.values())/len(feedback)
print("Average Rating:",round(avg,2))

# Generate result mapping each customer to "Excellent" or "Needs Improvement"
result={n:("Excellent" if r>=4 else "Needs Improvement") for n,r in feedback.items()}
print(result)


# sample output

"""
Customers with Rating 5: ['Arjun', 'Ravi', 'Fatima']
Average Rating: 4.33
{'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}

"""
