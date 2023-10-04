#assingment 7: Pattern Printing
#Problem : Create a program that prints a pattern of aterisks as shown below:
#*
#**
#***
#****
#*****
n=int(input("Enter the first number"))
for i in range(1, n+1): 
  print("*"*i)
  
for i in range(n+1, 1, -1):
    print("*"*i )
