# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the
# original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
# expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

import random
import math
import timeit

# list = [1, 2, 3, 4, 5]
# list = [2, 2, 3, 2, 2]
# list = [random.randint(1, 10) for i in range(1000)]  # This is huge.
list = [i for i in range(1, 100)]


def foo1():
    # Uses division.
    new_list = []
    for i in range(len(list)):
        product = 1
        for j in range(len(list)):
            product *= list[j]
        # Floor division to keep integers.
        new_list.append(product // list[i])

    return new_list


def foo2():
    # No division, uses slices, but still quite slow.
    new_list = []
    for i in range(len(list)):
        left_slice = list[:i]
        right_slice = list[i+1:]
        slices = left_slice + right_slice
        product = 1
        for j in range(len(slices)):
            product *= slices[j]
        new_list.append(product)

    return new_list


def foo3():
    # List comprehension one liner that actually works lol.
    product = 1
    new_list = [math.prod([product * j for j in list[:i] + list[i+1:]])
                for i in range(len(list))]

    return new_list


# Pretty much the same time, but foo3 looks the fastest.
print(timeit.timeit(foo1, number=100))
print(timeit.timeit(foo2, number=100))
print(timeit.timeit(foo3, number=100))
