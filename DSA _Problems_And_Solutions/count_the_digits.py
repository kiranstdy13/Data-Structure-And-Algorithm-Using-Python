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
