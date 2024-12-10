#10.	Tính giá trị của biểu thức: S = 1 +  với n là số dấu căn bậc 2; n là số nguyên dương, x là số thực nhập vào từ bàn phím. In kết quả ra màn hình
import math
x, n = map(int, input().split())
s = 0
for i in range(n):
    s = math.sqrt(x + s)
print("{:.2f}".format(s+1))