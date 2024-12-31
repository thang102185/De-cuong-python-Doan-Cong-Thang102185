class KhachHang:
    def __init__(self, ten="", ma="", dk=0, ck=0):
        self.ten = ten
        self.ma = ma
        self.dk = dk
        self.ck = ck

    def nhap(self):
        self.ten, self.ma, self.dk, self.ck = input().split()
        self.dk = int(self.dk)
        self.ck = int(self.ck)

    def luong_dien_tieu_thu(self):
        return int(self.ck - self.dk)

    def tien(self):
        luong_dien = self.luong_dien_tieu_thu()
        if self.ma[0] == 'H':
            return int(luong_dien * 1000)
        elif self.ma[0] == 'D':
            return int(luong_dien * 1000 * 1.05)
        elif self.ma[0] == 'K':
            return int(luong_dien * 1000 * 1.07)

    def xuat(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.ten, self.ma, self.dk, self.ck, self.luong_dien_tieu_thu(), self.tien())

n = int(input())
khachhanglist = []

for _ in range(n):
    kh = KhachHang()
    kh.nhap()
    khachhanglist.append(kh)

khach_hang_ho_kinh_doanh = [kh for kh in khachhanglist if kh.ma[0] == 'K']

if not khach_hang_ho_kinh_doanh:
    print("Khong co khach hang la ho kinh doanh.")
else:
    khach_hang_max = khach_hang_ho_kinh_doanh[0]
    for kh in khach_hang_ho_kinh_doanh:
        if kh.tien() > khach_hang_max.tien():
            khach_hang_max = kh
    print(khach_hang_max.xuat())