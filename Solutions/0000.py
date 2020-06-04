# This problem was recently asked by Google.
#
# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

import time
# import timeit
import random

# list = [7, 16, -6, 12, 15, -2]
list = [random.randint(-50, 50) for i in range(100)]


def foo1(k):
    # Sums the same two numbers.
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] + list[j] == k:
                print(True)
                exit()
    print(False)


# O(n^2)
def foo2(k):
    # Works.
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                if list[i] + list[j] == k:
                    return True  # We can just return.
                    exit()
    return False


# Internet solution. Works in O(n) because checking containment in sets
# is done in O(1), contrary to lists with O(n). Works like a charm. But
# there could be a better one.
def foo3(k):
    s = set()
    for x in list:
        if k-x in s:
            return True
        s.add(x)
    return False


# start = time.time()
print(foo3(101))
# end = time.time()
# print(end - start)
# Something
# Somethingx2
