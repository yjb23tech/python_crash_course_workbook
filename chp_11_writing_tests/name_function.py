def get_formatted_name(first, last, middle_name=''):
    """Generate a neatly formatted full name"""

    if middle_name:
        full_name = (f"{first} {middle_name} {last}")
    else:
        full_name = (f"{first} {last}")
    
    return full_name.title()

