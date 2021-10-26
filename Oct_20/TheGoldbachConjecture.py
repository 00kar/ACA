def IsPrime(num):
    if num <= 1:
        return False
    for divisor in range(2, (num//2)+1):
        if num % divisor == 0:
            return False
    return True
    
def GoldbachConjecture(number):
    for summable in range(2, (number//2)+1):
        if IsPrime(summable):
            if IsPrime(number - summable):
                print(f'{number} = {summable} + {number - summable}')
                break

n= int(input())
GoldbachConjecture(n)
