def tangdan(n):
    if n < 0:
        return "Error"
    else:
        check = True
        while n > 0:
            n1 = n % 10
            n2 = n // 10 % 10
            if(n1 < n2):
                check = False
                break
            n //= 10

        if check:
            return "Yes"
        else:
            return "No"

a, b, c = map(int, input().split())
print(tangdan(a), tangdan(b), tangdan(c))