from exeptions import InvalidCustomerIDException,InvalidCustomerAgeException
def validate_customer_id(cid):
    if cid<=0:
        raise InvalidCustomerIDException
    return True
def validate_customer_age(age):
    if age<18 or age>60:
        raise InvalidCustomerAgeException
    return True

age=validate_customer_age(45)
print(age)
cid=validate_customer_id(1001)
print(cid)