a=float(input("enter the first side"))
b=float(input("enter the second side"))
c=float(input("enter the third side"))
if((a+b>c)and(b+c>a)and(a+c>b)):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5

    print("the area of the triangle is",area)
else:
    print("triangle is not possible")     
