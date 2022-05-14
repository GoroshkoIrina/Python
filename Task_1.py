import sys
from itertools import islice

"""
nums = []
n = input('Введите число n: ')

for num in range(1, int(n)+1, 2):
    nums.append(num)

print(type(nums), sys.getsizeof(nums), nums)
"""

def num_gen(n):
    for num in range(1, int(n)+1, 2):
        yield num

my_generator = num_gen(5)
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

