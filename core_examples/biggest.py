n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))

if n1 < n2:
    if n2 < n3:
        print(n3," is biggest number")
    else:
        print(n2," is biggest number")
else:
    if n1 < n3:
        print(n3," is biggest number")
    else:
        print(n1," is biggest number")


