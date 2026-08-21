# Question 6
# Write a function: Leap Year
# Determine whether a given year is a leap year. A year is leap if divisible by 4 and if divisible by 100 then also by 400.
# Input: A single integer year.
# Output: Boolean: True if leap year, else False

def LeapYear(year):
    if(year%4==0):
        return True 
    return False
y = int(input("Enter Year: "))
print(LeapYear(y))