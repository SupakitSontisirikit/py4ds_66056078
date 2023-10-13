"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    if len(num_list) == 0:
        return None
    else:
        num_list.sort()
        x = len(num_list) // 2
        if len(num_list) % 2 == 0:
            return (num_list[x] + num_list[x - 1]) / 2
        else:
            return num_list[x]