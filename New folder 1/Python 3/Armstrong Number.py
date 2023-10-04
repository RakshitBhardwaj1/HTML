# Assignment 9: Armstrong Number Checker
# Problem: Build a program that check if a given number is an Armstrong number
#(a number that is equal to the sum
#of its own digits each raised to the power of the number of digits).
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3=371.
number=int(input("Enter the number"))

num_digits= len(str(number))
sum_of_cubes =0
temp=number
while temp>0:
    digit=temp%10
    sum_of_cubes += digit ** num_digits
    temp//=10
if number == sum_of_cubes:
        print(f"{number}is an Armstrong number.")
else:
        print(f"{number} is not Armstrong number.")


