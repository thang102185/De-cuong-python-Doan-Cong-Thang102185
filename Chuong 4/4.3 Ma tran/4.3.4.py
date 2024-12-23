m, n = map(int, input().split())

a = []
b = []
t = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(m):
    rowt = []
    for j in range(n):
        rowt.append(a[i][j] + b [i][j])
    t.append(rowt)

for row in t:
    print(*row)