def required_fields(data, fields):
    """
    Check if all required fields exist in a dictionary.
    
    Args:
        data (dict): The dictionary to validate.
        fields (list): List of required keys.

    Returns:
        bool: True if all fields are present, False otherwise.
    """
    for item in fields:
        # Check if the current field is missing in the data dictionary
        if item not in data:
            return False
    # All fields are present
    return True


def to_int(value):
    """
    Convert a value to an integer if possible.

    Args:
        value: The value to convert.

    Returns:
        int: Converted integer on success.
        ValueError: Returns the exception if conversion fails.
    """
    try:
        # Try converting the value to integer
        return int(value)
    except ValueError as e:
        # Return the exception object if conversion fails
        return e
