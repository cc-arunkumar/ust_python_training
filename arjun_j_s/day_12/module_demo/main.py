from custom_exception import InvalidAgeError,InvalidNameError


def validate_age(age):
    if(18>age or age>30):
        raise InvalidAgeError(age)
    else:
        print(f"{age} is valid")

def validate_name(name):
    if(len(name.strip())==0):
        raise InvalidNameError(name)
    else:
        print(f"{name} is valid")


validate_age(10)
validate_name(' ')