def kqua(n):
    if n < 0:
        return "Error"
    else:
        so_max = -1
        while n > 0:
            if (n % 10) > so_max:
                so_max = n % 10
            
            n //= 10
        return so_max
    
x, y, z = map(int, input().split())
print(kqua(x), kqua(y), kqua(z))