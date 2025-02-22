"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    if len(num_list) == 0:
        return 0
    else:
        x = 0
        for i in num_list:
            x = x + i
        return x


def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    if len(num_list) == 0:
        return 1
    else:
        x = 1
        for i in num_list:
            x = x * i
        return x