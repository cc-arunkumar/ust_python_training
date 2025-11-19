class InvalidException(Exception):
    def __init__(self, message="This is an invalid exception"):
        self.message = message
        super().__init__(self.message)
        
class InvalidErrorException(Exception):
    def __init__(self,message="Failed to connect to the database"):
        self.message = message
        super().__init__(self.message)
    