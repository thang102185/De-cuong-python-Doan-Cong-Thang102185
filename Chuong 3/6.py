def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

def printfi(n):
    f = []
    for i in range(1, n + 1):
        f.append(fibonacci(i))
    sumf = sum(f)
    print(*f)
    print("sum =", sumf)

n = int(input())
if n > 0:
    printfi(n)
