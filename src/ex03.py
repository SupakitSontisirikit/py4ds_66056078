"""
Execise 3
"""


def is_odd(num):
    """
    Check if a number is odd.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    # TODO : complete this
    if type(num) == int:
        if num % 2 == 0:
            return False
        else:
            return True
    else:
        return False
    pass


def is_even(num):
    """
    Determines if a given number is even.

    Parameters:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    # TODO : complete this
    if type(num) == int:
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        return False
    pass
