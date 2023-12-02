n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))
str = " is biggest number"
if n1 < n2:
    if n2 < n3:
        print(n3,str)
    else:
        print(n2,str)
else:
    if n1 < n3:
        print(n3,str)
    else:
        print(n1,str)


