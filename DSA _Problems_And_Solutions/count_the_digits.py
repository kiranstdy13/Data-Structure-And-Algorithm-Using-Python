'''
Count the number of digits in an integer number

input = 505
output = 3

'''


n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)


# time complexity O(1) Advance

from math import *

def count_digits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1

n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

