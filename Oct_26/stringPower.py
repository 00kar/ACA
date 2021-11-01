s = input()
k = int(input())
result = ""

while k > 0:
    result += s
    k-=1

else:
    if len(s)%k == 0:   
        result = s[:len(s)//-k]
        if res == s[(len(s)//k):]:
            print(result)
        else:
            print("undifined")
    else:
        print("undifined")
