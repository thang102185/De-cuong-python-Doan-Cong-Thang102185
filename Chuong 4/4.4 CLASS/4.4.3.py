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

# n = int(input())
# sach_list = []
# for i in range(n):
#     sach = Sach()
#     sach.nhap()
#     sach_list.append(sach)
    
# sach_list.sort(key = lambda x: x.tBinh)
# with open('sach.txt', 'w') as file:
#     for sach in sach_list:
#         file.write(sach.xuat())

sachtxt_list =[]       
with open('sach.txt', 'r') as file:
    for i in file:
        ten, sotrang, giatien, tBinh = i.strip().split()
        sotrang = int(sotrang)
        giatien = float(giatien)
        tBinh = float(tBinh)
        sach = Sach(ten, sotrang, giatien)
        sachtxt_list.append(sach)
        
dieukien = []
for sach in sachtxt_list:
    if sach.giatien > 100000 and sach.sotrang < 200:
        dieukien.append(sach)
        
with open('ketqua.txt', 'w') as file:
    for sach in dieukien:
        file.write(sach.xuat())