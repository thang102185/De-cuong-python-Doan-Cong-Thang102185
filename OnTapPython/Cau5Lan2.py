n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
for i in range(n):
    a[i].sort()
    
print(n, m)
for i in range(n):
    for j in range(m):
        print(a[i][j], end = " ")
    print()