"""
Exercise 11
"""


def get_hr_min_sec(sec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        sec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    hr = sec//3600
    x = sec % 3600
    mi = x//60
    se = x % 60

    if hr == 0 and mi != 0 and se != 0:
        return str(mi) + 'm' + ' ' + str(se) +'s'
    elif hr != 0 and mi == 0 and se != 0:
        return str(hr) + 'h' + ' ' + str(se) +'s'
    elif hr == 0 and mi == 0:
        return str(se) +'s'
    elif hr == 0 and se == 0:
        return str(mi) + 'm'
    elif mi == 0 and se == 0:
        return str(hr) + 'h'
    else:
        return str(hr) + 'h' + ' ' + str(mi) + 'm' + ' ' + str(se) +'s'
    pass
