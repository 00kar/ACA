num = int(input("Enter Natural number \t"))
power = degree = 1
while power <= num/3:
    degree += 1
    power = 3**degree
print(power)
