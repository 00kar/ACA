num = int(input("number = "))
product = 1
while num:
    remainder = num % 10
    if remainder != 0:
        product *= remainder
    num //= 10

print("product = ",product)
