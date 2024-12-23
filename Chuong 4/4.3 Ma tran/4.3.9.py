m, n = map(int, input().split())
A = []
for i in range(m):
    A.append(list(map(int, input().split())))

kq = []
for i in range(m):
    if sum(A[i]) % 7 == 0:
        kq.append(i + 2)

if len(kq) > 0:
    for i in kq:
        print(i)
else:
    print("NO")
