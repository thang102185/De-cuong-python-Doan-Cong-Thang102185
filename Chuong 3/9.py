#9.	Viết hàm đổi số nguyên dương n từ thập phân sang thập lục phân và chương trình áp dụng (không dùng hàm có sẵn)
def thapSangThapLuc(n):
    if n == 0:
        return ""
    hex = "0123456789ABCDEF"
    return thapSangThapLuc(n // 16) + hex[n % 16]

n = int(input())
if n >= 0:
    print(thapSangThapLuc(n))
elif n == 0:
    print(0)