import math

def find_n(x, ep):
    if ep <= 0 or ep >= 1:
        return
    n = 0
    while math.fabs(x**n / math.factorial(n)) < ep:
        n += 1
    return n
ep, x = map(float, input().split())
n = find_n(x, ep)
s = 0
for i in range(n+1):
    s += x**n / math.factorial(n)
print("{:.2f}".format(s))