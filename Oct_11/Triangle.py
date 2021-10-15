a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a+b > c and a+c > b and b+c > a:
    if a >= b and a >= c:
        cosAlfa = (b**2 + c**2 - a**2) / 2*b*c
    elif b >= a and b >= c:
        cosAlfa = (a**2 + c**2 - b**2) / 2*a*c
    else:
        cosAlfa = (a**2 + b**2 - c**2) / 2*a*b
    print("Acute Triangle") if cosAlfa > 0 else print("Right Triangle") if cosAlfa == 0 else print("Ostuse Triangle")
else:
    print("NO Triangle")
