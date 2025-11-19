from custom_modules import InvalidException, InvalidErrorException

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidException("Age must be between 0 and 120.")
# def connect_to_database(db_string):
#     if db_string != "valid_db_connection_string":
#         raise InvalidErrorException("Could not connect to the database with the provided connection string.")
#     return True

validate_age(150)  # This will raise an InvalidException