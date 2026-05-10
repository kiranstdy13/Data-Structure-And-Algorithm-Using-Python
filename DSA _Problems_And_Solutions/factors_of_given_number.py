'''
factor is a number that divides another number evenly, without leaving a remainder. For example, the factors of 12 are 1, 2, 3, 4, 6, and 12 because each of these numbers divides 12 evenly.
To find the factors of a given number, you can use the following Python code:

```python
'''

n = int(input("Enter a number: "))
FACTORS = []
for i in range(1,n//2 +1):
    if n % i == 0:
        FACTORS.append(i)

FACTORS.append(n)  # The number itself is also a factor  
print(f"The factors of {n} are: {FACTORS}")
