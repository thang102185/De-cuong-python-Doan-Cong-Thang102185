#9.	Tính S = 1+ x + x2 + x3 + … + xn
x, n = map(int, input().split())
s = 0
for i in range(n + 1):
    s += x**i
print(s)