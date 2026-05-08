'''
Armstrong Number : An Armstrong number is a number that is equal to the sum of its own digits each raised to the
power of the number of digits. 
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. Write a Python program to check if a given number is an Armstrong number or not.
'''

n = int(input("Enter a number: "))

original_n = n

length = len(str(n))
armstrong_sum = 0

while n > 0:
    digit = n % 10
    armstrong_sum += digit ** length
    n = n // 10
if armstrong_sum == original_n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")