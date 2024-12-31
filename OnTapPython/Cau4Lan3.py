def so(matran):
    for i in range(len(matran)):
        if matran[i] > 0:
            return "{0} {1:.3f}".format(i, matran[i])
        
    return "Khong co so duong trong mang."

n = int(input())
a = list(map(float, input().split()))
m = int(input())
b = list(map(float, input().split()))
print(so(a))
print(so(b))