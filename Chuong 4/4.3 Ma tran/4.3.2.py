m, n = map(int, input().split())

a = []
b = []
t = []
h = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(m):
    rowt = []
    rowh = []
    for j in range(n):
        rowt.append(a[i][j] + b [i][j])
        rowh.append(a[i][j] - b [i][j])
    t.append(rowt)
    h.append(rowh)

for row in t:
    print(*row)
for row in h:
    print(*row)