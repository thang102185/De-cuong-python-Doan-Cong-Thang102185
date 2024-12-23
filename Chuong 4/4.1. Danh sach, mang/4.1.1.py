#4.1.1.	Tìm số trong mảng
n, k = map(int, input().split())
a = set(map(int, input().split()))
x = list(map(int, input().split()))
for i in range(k):
    if x[i] in a:
        print("YES")
    else:
        print("NO")