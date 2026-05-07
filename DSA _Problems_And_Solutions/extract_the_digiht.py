
n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

from math import *

def count_digits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1

n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

