#1.	Viết hàm tính giai thừa của 1 số và chương trình áp dụng
def giaithua(n):
    kq = 1;
    for i in range(1, n+1):
        kq *= i
    return kq

n = int(input())
print(giaithua(n))