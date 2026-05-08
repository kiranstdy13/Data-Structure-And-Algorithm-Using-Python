
''' 
A palindrome is a number that reads the same backward as forward. For example, 121 is a palindrome, while 123 is not. Write a Python program to check if a given number is a palindrome or not. 
Input: 121
Output: Palindrome

Explain : 
1. We take the input number from the user and store it in the variable 'n'.
2. We initialize a variable 'revers' to 0, which will be used to 
store the reversed number.
3. We use a while loop that continues until 'n' becomes 0. Inside the loop, we extract the last digit of 'n' using the modulus operator (%) and store it in the variable 'digit'.
4. We then update the 'revers' variable by multiplying it by 10 and adding the extracted digit. This effectively builds the reversed number.
5. We update 'n' by performing integer division by 10, which removes the last digit from 'n'.
6. After the loop, we compare the reversed number 'revers' with the original number 'n'. If they are equal, we print "Palindrome". Otherwise, we print "Not a palindrome".          

121 :
    1. revers = 0 * 10 + 1 = 1
    2. revers = 1 * 10 + 2 = 12
    3. revers = 12 * 10 + 1 = 121
    4. n = 0 (loop ends)
    5. revers (121) == n (121) => Palindrome 
'''


n = int(input("Enter a number: "))

revers = 0
while n > 0 :
    digit = n % 10
    revers = revers * 10 + digit
    n = n // 10

if revers == n:
    print("Palindrome")
else:
    print("Not a palindrome")