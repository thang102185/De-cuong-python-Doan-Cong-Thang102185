#12.	Tính S = 1 + 3! + 5! + … + (2n+1)!
import math
n = int(input())
s = 0
for i in range(n + 1):
    s += math.factorial(2*i+1)
print(s)