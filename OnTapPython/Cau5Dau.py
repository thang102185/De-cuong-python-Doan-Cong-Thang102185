n = int(input())
a = list(map(int, input().split()))
tbc = sum(a)/n
kq = []
for i in a:
    if i >= tbc:
      kq.append(i)

print(*kq)
print("So phan tu thoa man:", len(kq))