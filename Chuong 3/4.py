#4.	Viết hàm tìm UCLN của 2 số nguyên dương a và b, viết chương trình áp dụng
def UCLN(a, b):
    while a*b!=0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

a, b = map(int, input().split())
if a > 0 and b > 0:
    print(UCLN(a, b))