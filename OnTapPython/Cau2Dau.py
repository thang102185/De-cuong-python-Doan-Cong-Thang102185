def fi(n):
    if(n == 1 or n == 2):
        return 1
    else:
        a, b = 1, 1
        for i in range(3, n+1):
            a, b = b, a+b
        return b

n = int(input())
for i in range(1, n+1):
    print(fi(i), end = " ")