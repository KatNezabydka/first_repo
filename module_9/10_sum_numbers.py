'''

'''
from functools import reduce


def sum_numbers(numbers):
    return reduce((lambda x, y: x + y), numbers)

print(sum_numbers([1, 2, 3, 4]))