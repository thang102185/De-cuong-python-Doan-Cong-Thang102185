def check(n):
    if n < 0:
        return "Error"
    else:
        while n > 0:
            if n % 2 != 0:
                return "No"
            n //= 10
        return "Yes"
        
x, y, z = map(int, input().split())
print(check(x), check(y), check(z))