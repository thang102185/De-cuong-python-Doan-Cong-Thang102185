m, n = map(int, input().split())

matrix = []
tong = 0

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
    tong += sum(row)

tbc = tong / (m * n)

print("{:.2f}".format(tbc))

for i in range(m):
    for j in range(n):
        if matrix[i][j] > tbc:
            print(matrix[i][j], i + 1, j + 1)
