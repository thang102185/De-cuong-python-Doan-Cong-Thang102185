a = list(map(int, input().split()))
b = int(input())
k = 0
x = 0
for i in a:
    if i % b == 0 and i > x:
        x = i
        k = 1
    
if k != 0:
    print(x)
else:
    print(k)