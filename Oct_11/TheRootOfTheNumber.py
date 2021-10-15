def Root(num):
    sum = 0
    print(num)
    while num:
        sum += num % 10
        num //= 10
    if sum >= 10:
        Root(sum)
    else:
        print(sum)

number = int(input("number = "))
Root(number)
