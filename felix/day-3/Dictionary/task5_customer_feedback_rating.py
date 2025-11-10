# task5_Customer_Feedback_Rating

feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

feedback["Priya"] = 4

feedback["Ravi"] += 1

total = 0
print("Customers with rating 5:")
for i in feedback:
    if feedback[i] == 5:
        print(i)
    total += feedback[i]

print("Average rating: ",total/len(feedback))

result = {n:("Excellent" if r>4 else "NeedImprovement") for n,r in feedback.items()}
print("New dictionary:")
print(result)

    
# output

# Customers with rating 5:
# Arjun
# Ravi
# Fatima
# Average rating:  4.333333333333333
# New dictionary:
# {'Arjun': 'Excellent', 'Neha': 'NeedImprovement', 'Vikram': 'NeedImprovement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'NeedImprovement'}