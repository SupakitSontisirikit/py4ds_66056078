"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    mode = 0
    x = 0
    if num_list.__len__() == 0:
        return None
    else:
        for i in num_list:
            y = num_list.count(i)
            if y > x:
                x = y
                mode = i
        return mode