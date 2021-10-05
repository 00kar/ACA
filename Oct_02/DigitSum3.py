number = int(input("Enter a three-digit number\t"))
result = 0
while number:
    result += number%10
    number //= 10
print("Summary of digits", result)
