'''
    Extract the digits in a integer number

    input = 345
    oupt = 5 4 3
'''
# time complexity O(log 10(n))
n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

# time complexity O(1) Advance

from math import *

def count_digits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1

n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

