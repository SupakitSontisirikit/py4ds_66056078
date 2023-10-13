"""
Exercise 14
"""


def average(num_list: list) -> None:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    if len(num_list) == 0:
        return None
    else:
        x = 0
        for i in num_list:
            x = x + i
        y = x / len(num_list)
    return y