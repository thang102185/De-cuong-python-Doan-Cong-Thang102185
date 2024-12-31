n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
c = int(input())
if c == 0:
    for i in range(n):
        if i % 2 == 0:
            a[i].sort(reverse = True)
        else:
            a[i].sort(reverse = False)
elif c == 1:
    for i in range(n):
        if i % 2 == 0:
            a[i].sort(reverse = False)
        else:
            a[i].sort(reverse = True)
            
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()