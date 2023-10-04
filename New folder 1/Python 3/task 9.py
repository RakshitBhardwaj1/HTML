side1=eval(input(f"Enter the side1 of a triangle"))
side2=eval(input(f"Enter the side2 of a triangle"))
side3=eval(input(f"Enter the side3 of a triangle"))
if side1==side2==side3:
    print("The Triangle is Equilateral")
elif side1==side2 or side2==side3 or side1==side3:
    print("The Triangle is Isosceles")     
else:
    print("scalen Triangle")    