"""
    You can use the range() funtion if you need to iterate over a sequence of numbers.

    It generates arithmetic progressions - a sequence of numbers where the difference between any two successive members is a constant.
"""


for i in range(5):
    print(i)

'''
    The given end point is never part of the generated sequence; it is only used to determine the length of the sequence.

    range(10) generates a sequence of 10 values, from 0 to 9, these are the indices of items in a sequence of length 10.

    If you want, the range can start at another number
    You can also specify a deifferent increment. This is called the step. By default, the step size is 1. But it can be any integer, including negative integers to generate a decreasing sequence.
'''

for a in range(5, 10):
    print(a)


print(list(range(5, 10)))

print(list(range(0, 10, 3)))


print(list(range(-10, -100, -20)))

# To iterate over the indices of a sequence, combine range() and len()
a = ["Mary", "had", "a", "little", "lamb"]
for ind in range(len(a)):
    print(ind, a[ind], len(a[ind]))
# Better to use enumerate()


# Trying to print a range returns the same range
print(range(5)) # range(5)

'''
    range() does not produce a static list, but an object that generates the numbers on demand (an iterable). This is more efficient than a list, especially for large ranges.
    If you want to make a list, you can use the list() function to convert a range into a list.
    This iterable can be passed to constructs such as for loops and functions that consume iterables.
'''

print(sum(range(5)))
