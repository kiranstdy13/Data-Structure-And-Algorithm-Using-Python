'''
    Extract the digits in a integer number

    input = 345
    oupt = 5 4 3
'''

n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10


