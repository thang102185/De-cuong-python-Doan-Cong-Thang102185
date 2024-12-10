#8.	Viết hàm đổi số nguyên dương n từ thập phân sang nhị phân và chương trình áp dụng (không dùng hàm có sẵn)
def thapsangnhi(n):
    if n == 0:
        return
    elif n > 0:
        thapsangnhi(n // 2)
        print(n % 2, end = "")

n = int(input())
if n >= 0:
    thapsangnhi(n)