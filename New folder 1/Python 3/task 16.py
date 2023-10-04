limit = int(input("Enter the number"))
num1 = 0
num2 = 1
num3 = 0
print(num1)
for num in range(1, limit+1):
      num1=num2
      num2=num3
      num3=num1+num2
      print(num3)