n = int(input())
a = []

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
sumc = 0
sump = 0
for i in range(n):
    sumc += a[i][i]
    sump += a[i][n-i-1]
print(sumc)
print(sump)