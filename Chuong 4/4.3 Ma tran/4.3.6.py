n = int(input())
a = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

dx = True

for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] != a[j][i]:
            dx = False
            break
    if not dx:
        break

if dx:
    print("YES")
else:
    print("NO")
