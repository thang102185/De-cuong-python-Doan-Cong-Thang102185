m, n, k = map(int, input().split())
a = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
cnt = 0
for i in range(m):
    for j in range(n):
        if k == a[i][j]:
            cnt += 1

print(cnt)