#4.2.1.	Chuẩn hoá xâu kí tự
def chuanHoa(s):
    s = " ".join(s.split())
    s = s.capitalize()
    return s

s = input()
kq = chuanHoa(s)
print(kq)
