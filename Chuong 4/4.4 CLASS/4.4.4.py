class NhanVien:
    def __init__(self, manv = 0, ten = '', hesoluong = 0.0, pcap = 0):
        self.ten = ten
        self.manv = manv
        self.hesoluong = hesoluong
        self.pcap = pcap
        
    def luong(self):
        return int(self.hesoluong * 2000000 + self.pcap)
    
    def nhap(self):
        self.manv, self.ten, self.hesoluong, self.pcap = input().split()
        self.manv = int(self.manv)
        self.hesoluong = float(self.hesoluong)
        self.pcap = int(self.pcap)
        
    def xuat(self):
        return "{0} {1} {2:.2f} {3} {4}".format(self.manv, self.ten, self.hesoluong, self.pcap, self.luong())

n = int(input())
nhanvien_list = []
for i in range(n):
    nhanvien = NhanVien()
    nhanvien.nhap()
    nhanvien_list.append(nhanvien)

min = nhanvien_list[0]
for nhanvien in nhanvien_list:
    if min.luong() > nhanvien.luong():
        min = nhanvien
    
print("Nhan vien co luong thap nhat")        
print("{0}".format(min.xuat()))