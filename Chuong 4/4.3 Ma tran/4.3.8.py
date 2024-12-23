n = int(input())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

hoa = True
thuong = True

for i in range(n):
    for j in range(n):
        if i > j and A[i][j] != 0:
            hoa = False
        if i < j and A[i][j] != 0:
            thuong = False

if hoa:
    print("UPPER TRIANGLE")
elif thuong:
    print("LOWER TRIANGLE")
else:
    print("NONE")
