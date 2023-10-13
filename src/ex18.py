"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(qty, price):
    x = qty // 9
    sum_price = (qty - x) * price
    return sum_price
    pass
