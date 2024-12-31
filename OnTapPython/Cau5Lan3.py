a, b = map(int, input().split())
for i in range(a, b + 1):
    for j in range(i,10):
        print("{0}x{1}={2}".format(i, j, i*j))