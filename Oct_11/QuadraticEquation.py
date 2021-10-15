from math import sqrt

def Discriminant(a:float, b:float, c:float):
        return (b**2) - (4*a*c)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Non-quadratic Equation")
    if b == 0:
        if c == 0:
            print("Infinite Solutions")
        else:
            print("No Solutions")
    else:
        print("One Solution:", -c/b)
else:
    D = Discriminant(a, b, c)
    print("Quadratic Equation")
    print("Discriminant:",D)
    if D > 0:
        print("Two Solutions:", (-b + sqrt(D)) / 2*a, (-b - sqrt(D)) / 2*a)
    elif D == 0:
        print("One Solution:", -b/2*a)
    else:
        print("No Solutions")
