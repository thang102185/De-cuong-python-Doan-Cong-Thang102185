class SinhVien:
    def __init__(self, ten = '', ma = 0, dT = 0.0, dTr = 0.0, dLTC = 0.0):
        self.ten = ten
        self.ma = ma
        self.dT = dT
        self.dTr = dTr
        self.dLTC = dLTC
        
    def diemTB(self):
        return (self.dT + self.dTr + self.dLTC) / 3
    
    def nhap(self):
        self.ten, self.ma, self.dT, self.dTr, self.dLTC = input().split()
        self.ma = int(self.ma)
        self.dT = float(self.dT)
        self.dTr= float(self.dTr)
        self.dLTC = float(self.dLTC)
        
    def xuat(self):
        return "{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.ma, self.ten, self.dT, self.dTr, self.dLTC, self.diemTB())
        
n = int(input())
sinhvien_list = []
for i in range(n):
    sinhvien = SinhVien()
    sinhvien.nhap()
    sinhvien_list.append(sinhvien)

cnt = 0
print("Danh sach sinh vien hoc lai")    
for s in sinhvien_list:
    if (s.dT < 4.0 and s.dTr < 4.0) or (s.dT < 4.0 and s.dLTC < 4.0) or (s.dLTC < 4.0 and s.dTr < 4.0):
        print(s.xuat())
        cnt += 1
        
print("Danh sanh nay co", cnt, "sinh vien phai hoc lai")