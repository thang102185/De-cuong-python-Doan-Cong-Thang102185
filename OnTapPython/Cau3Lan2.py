class NhanVien:
    def nhap(self):
        self.ten, self.manv, self.heso, self.pcap = input().split()
        self.manv = int(self.manv)
        self.heso = float(self.heso)
        self.pcap = int(self.pcap)
        self.luong = self.heso * 2000000 + self.pcap
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.manv, self.ten, self.heso, self.pcap, self.luong))

n = int(input())
nhanvien_list = []
for i in range(n):
    nhanvien = NhanVien()
    nhanvien.nhap()
    nhanvien_list.append(nhanvien)

nv_max = nhanvien_list[0]
for i in range(n):
    if nv_max.luong < nhanvien_list[i].luong:
        nv_max = nhanvien_list[i]
    
print("Nhan vien co luong lon nhat")
nv_max.xuat()