
class CustomerAgeInvalidError(Exception):
    def __init__(self,age):
        super().__init__(f"age is invalid: {age}")

class CustomerIDError(Exception):
    def __init__(self, cid):
        super().__init__(f"customer id invalid: {cid}")