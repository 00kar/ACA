def DigitCount(num):
    count = 0
    while num:
        count += 1
        num //=10
    return count


def IsPalindrome(num):
    temp = num
    reverse = 0
    while temp:
        digit = temp % 10
        reverse = reverse*10 + digit
        temp //= 10
    if num == reverse:
        return True
    return False


a = int(input())
b = int(input())

for n in range(a, b+1):
    if IsPalindrome(n):
        print(n, end=" ")

