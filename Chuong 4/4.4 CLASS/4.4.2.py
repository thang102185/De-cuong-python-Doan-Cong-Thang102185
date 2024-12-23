class Sach:
    def __init__(self, ten = '', sotrang = 0, giatien = 0.0):
        self.ten = ten
        self.sotrang = sotrang
        self.giatien = giatien
        if sotrang > 0:
            self.tBinh = self.giatien / self.sotrang
        else:
            self.tBinh = 0
    def nhap(self):
        self.ten, self.sotrang, self.giatien = input().split()
        self.sotrang = int(self.sotrang)
        self.giatien = float(self.giatien)
        if self.sotrang > 0:
            self.tBinh = self.giatien / self.sotrang
        else:
            self.tBinh = 0
    def xuat(self):
        return "{0} {1} {2:.2f} {3:.2f}\n".format(self.ten, self.sotrang, self.giatien, self.tBinh)

n = int(input())
sach_list = []
for i in range(n):
    s = Sach()
    s.nhap()
    sach_list.append(s)
    
sach_list.sort(key = lambda x: x.tBinh) 

with open('sach.txt', 'w') as file:
    for sach in sach_list:
        file.write(sach.xuat())
        
with open('sach.txt', 'r') as file:
    noidung = file.read()
    print(noidung)       