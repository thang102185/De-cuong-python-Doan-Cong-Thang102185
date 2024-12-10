#3.	Viết hàm kiểm tra một số có phải số hoàn hảo không, áp dụng hàm tìm các số hoàn hảo trong đoạn (a,b)
import math
def soHoanHao(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return n == sum

a, b = map(int , input().split())
for i in range(a, b+1):
    if soHoanHao(i):
        print(i, end = " ")