n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

row_set = []
for row in a:
    row_set.append(set(row))
    
col_set = []
for j in range(m):
    col = set()
    for i in range(n):
        col.add(a[i][j])
    col_set.append(col)
    
dacbiet = set()
for i in range(n):
    for j in row_set[i]:
        if all(j in col for col in col_set):
            dacbiet.add(j)
            
print(" ".join(map(str, sorted(dacbiet))))
