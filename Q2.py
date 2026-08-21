# Question 2
# Palindrome Number
# Determine whether an integer is a palindrome without converting it to a string.
# Input: x: Integer
# Output: Boolean: True if x is a palindrome, else False
# Example:  
x = int(input("Enter a number: "))
original = x
rev = 0
while(x>0):
        rev = rev * 10
        rev += x % 10
        x = x // 10
print("--------------------------------------------------------------------------------------")
print(f"Original number: {original}")
print(f"Reversed number: {rev}")

if(original==rev):
    print("Palindrome")
else: 
    print("Not Palindrome")  
    
