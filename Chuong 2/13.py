#13.	Tính tổng   Tìm số nguyên dương n nhỏ nhất sao cho 1 + 2 + 3 + …… + n > 1000
import math

def min_n():
    tong = 0
    n = 0
    while tong <= 1000:
        n += 1
        tong += n
    return n

n = min_n()
s = 0
for i in range(n + 1):
    s += 1 / math.factorial(2*i+1)
print(s)