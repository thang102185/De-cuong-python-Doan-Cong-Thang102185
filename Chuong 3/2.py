#2.	Viết hàm kiểm tra một số có phải nguyên tố không, áp dụng hàm tìm các số nguyên tố trong khoảng (1,n)
import math
def snt(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, math.isqrt(n)+1):
            if n % i == 0:
                return False
        return True

n = int(input())
for i in range(1, n+1):
    if snt(i):
        print(i, end = " ")