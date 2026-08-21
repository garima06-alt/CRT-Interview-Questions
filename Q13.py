# Question 13
# Count Number of Digits in an Integer
# Count digits in an integer without converting it to string.
# Input: An integer num.
# Output: Count of digits.

n = int(input("Enter a number: "))
count = 0 
while(n>0):
    n = n//10
    count = count + 1
print(count)
    
    