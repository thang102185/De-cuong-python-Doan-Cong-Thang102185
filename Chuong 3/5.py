#5.	Viết hàm tìm BCNN của 2 số nguyên dương a và b, viết chương trình áp dụng
def UCLN(a, b):
    while a*b!=0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b
def BCNN(a, b):
    return (a*b)//UCLN(a, b);

a, b = map(int, input().split())
if a > 0 and b > 0:
    print(BCNN(a, b))