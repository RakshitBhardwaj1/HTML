#problem: Write a program that reads a time duration in minutes 
#from the user and converts it to hours and minutes.
#For example,130 minutes should be displayed as "2 hours and 10 minutes".
# go to haker rank ,leefcode, codechef
num1=int(input("Enter the minute"))
hour=num1//60
minutes=(num1%60)
print(f"the time duration is {hour} hour and {minutes}  minutes")