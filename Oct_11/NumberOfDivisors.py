number = int(input("number = "))
count = 1
for i in range(1, (number//2) + 1):
    if number % i == 0:
        count += 1
print("divisors = ",count)
