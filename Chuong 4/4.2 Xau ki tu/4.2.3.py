#4.2.3.	Xoá kí tự trong xâu
def xoaKiTu(s, c):
    s1 = ""
    for i in s:
        if i != c:
            s1 += i
    return s1

s = input()
c = input()
kq = xoaKiTu(s, c)
print(kq)