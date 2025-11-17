from exceptions import InvalidCustomerIdException,InvalidCustomerAgeException


def id_validation(cid):
            if cid<0:
                raise InvalidCustomerIdException
            True

def age_validation(age):
            if age<0:
                raise InvalidCustomerAgeException
            True
    
def main():
       id_validation(-1)

if __name__  == "__main__":
        main()



