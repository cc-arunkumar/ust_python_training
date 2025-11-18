from .exceptions import CustomerAgeInvalidError,CustomerIDError

def validate_cid(cid):
    try:
        if cid<=0:
            raise CustomerIDError(cid)
    except CustomerIDError as e:
        print("Error for",e)
        
def validate_age(age):
    try:
        if age<18 or age>60:
            raise CustomerAgeInvalidError(age)
    except CustomerAgeInvalidError as e:
        print("Error for",e)
    