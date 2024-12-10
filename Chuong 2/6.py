#6.	Tính S = 1.3 +2.3 + 3.3 + ……+ n.3
n = int(input())
s = 0
for i in range(1, n+1):
     s += i * 3
print(s)