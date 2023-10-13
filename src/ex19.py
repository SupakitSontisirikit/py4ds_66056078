"""
Exercise 19 : Password Generator
"""
import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'    # 26
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    # 26
NUMBERS = '1234567890'                          # 10
SPECIAL = '~!@#$%^&*()_+'                       # 13

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def gen_password(char_num):
    # TODO : complete this
    pas = []
    if char_num < 12:
        char_num = 12
    pas.append((random.choice(LOWER_LETTERS)))
    pas.append((random.choice(UPPER_LETTERS)))
    pas.append((random.choice(NUMBERS)))
    pas.append((random.choice(SPECIAL)))
    for i in range(char_num-4):
        pas.append(random.choice(ALL_CHARS))
    return pas
    pass
