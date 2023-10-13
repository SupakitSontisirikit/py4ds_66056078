"""
Execise 2
"""


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # TODO : complete this
    f = celsius*(9/5) + 32
    return f
    pass


def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # TODO : complete this
    c = (5/9)*(fahrenheit - 32)
    return c
    pass
