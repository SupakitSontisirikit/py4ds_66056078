"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    num_cha = str(num)
    if num < 100 != 0:
        if num == 1:
            return str(num) + 'st'
        if num == 2:
            return str(num) + 'nd'
        if num == 3:
            return str(num) + 'rd'
        else:
            return str(num) + 'th'
    elif num // 100 == 1:
        return str(num) + 'st'
    elif num // 100 == 2:
        return str(num) + 'nd'
    elif num // 100 == 3:
        return str(num) + 'rd'
    else:
        return str(num) + 'th'
    pass
