"""
Exercise 17
"""
import random


def roll_dice(num_of_dice):
    """
    Calculate the total sum of rolling a certain number of dice.

    Parameters:
        num_of_dice (int): The number of dice to roll.

    Returns:
        int: The total sum of the dice rolls.
    """
    dice = [1,2,3,4,5,6]
    x = 0
    if num_of_dice == 0:
        return 0
    else:
        for i in range(num_of_dice):
            x = x + random.choice(dice)
        return x
    pass
