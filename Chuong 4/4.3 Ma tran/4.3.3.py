m, n, p= map(int, input().split())

a = []
b = []
t = [[0 for i in range(p)] for _ in range(m)]
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(m):
    for j in range(p):
        for k in range(n):
            t[i][j] += a[i][k] * b[k][j]

for i in t:
    print(*i)