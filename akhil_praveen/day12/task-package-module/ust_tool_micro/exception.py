class BlankFieldError(Exception):
    def __init__(self, id,field):
        super().__init__(f"{field} not found in {id} ")