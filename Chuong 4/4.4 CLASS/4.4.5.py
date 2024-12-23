class NhanVien:
    def __init__(self, ten = '', manv = 0, heso = 0.0, pcap = 0):
        self.ten = ten
        self.manv = manv
        self.heso = heso
        self.pcap = pcap
    
    def luong(self):
        return self.heso * 2000000 + self.pcap
    
    def nhap(self):
        self.ten, self.manv, self.heso, self.pcap = input().split()
        self.manv = int(self.manv)
        self.heso = float(self.heso)
        self.pcap = int(self.pcap)
        
    def xuat(self):
        return "{0} {1} {2:.2f} {3} {4:.2f}".format(self.manv, self.ten, self.heso, self.pcap, self.luong())

n = int(input())
nhanvien_list = []
for i in range(n):
    nhanvien = NhanVien()
    nhanvien.nhap()
    nhanvien_list.append(nhanvien)

nhanvien_list.sort(key = lambda x: x.luong(), reverse=True)

print("Danh sach nhan vien da sap xep:", n)
for i in nhanvien_list:
    print(i.xuat())     