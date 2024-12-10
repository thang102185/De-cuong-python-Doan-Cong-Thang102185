#14.	Tính tổng s:
# tới khi  , với 0 < a < 0,01 là số thực được nhập từ bàn phím.
import math

def find_n(a):
    if a <= 0 or a >= 0.01:
        return
    kq = (1 / a - 1) / 2
    return math.ceil(kq)

a = float(input())
n = find_n(a)
s = 0
for i in range(n + 1):
    s += 1 / math.factorial(2 * i + 1)
print("{:.2f}".format(s))
