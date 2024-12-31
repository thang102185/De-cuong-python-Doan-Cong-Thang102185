n1, m1 = map(int, input().split())
X = []
for i in range(n1):
    X.append(list(map(int, input().split())))
    
n2, m2 = map(int, input().split())
Y = []
for i in range(n2):
    Y.append(list(map(int, input().split())))
    
if n1 == n2 and m1 == m2:
    tong = []
    for i in range(n1):
        tong.append([X[i][j] + Y[i][j] for j in range(m1)])
        
    print("Ma tran tong")
    for i in range(n1):
        for j in range(m1):
            print(tong[i][j], end = ' ')
        print()

else:
    print("Du lieu vao sai")