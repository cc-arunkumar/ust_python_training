from customer_package import( CustomerAgeInvalidError,CustomerIDError,validate_cid,validate_age)


try:
    validate_cid(-5)
except CustomerIDError as e:
    print("Error:", e)

try:
    validate_age(75)
except CustomerAgeInvalidError as e:
    print("Error:", e)

print("Done!")