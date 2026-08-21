# Question 1
# Reverse a number
# Reverse the digits of an integer.
# Input: An integer number.
# Output: Reversed integer.

def reverse(x):
    rev = 0
    while(x>0):
        rev = rev * 10
        rev += x % 10
        x = x // 10
    return rev

x = int(input("Enter a number: "))
original = x
print(f"Original number: {original}")
print(f"Reversed number: {reverse(x)}")
