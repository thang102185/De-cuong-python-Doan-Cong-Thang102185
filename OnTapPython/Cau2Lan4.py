class ThiSinh:
    def nhap(self):
        self.ten, self.sbd, self.d1, self.d2, self.d3 = input().split()
        self.sbd = int(self.sbd)
        self.d1 = float(self.d1)
        self.d2 = float(self.d2)
        self.d3 = float(self.d3)
        self.tong = self.d1 + self.d2 + self.d3
        
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.sbd, self.ten, self.d1, self.d2, self.d3, self.tong))
    def da_do(self):
        return self.tong >= 15 and (self.d1 >= 1 and self.d2 >= 1 and self.d3 >= 1)
                
n = int(input())
thisinh_list = []
for i in range(n):
    thisinh = ThiSinh()
    thisinh.nhap()
    thisinh_list.append(thisinh)
    
dem = 0
for ts in thisinh_list:
    if ts.da_do():
        dem = 1
        break
    
if dem == 0:
    print("Khong co thi sinh thi do")
else:
    stt = 0
    thuKhoa = thisinh_list[0]
    for i in range(n):
        if thisinh_list[i].da_do() and thisinh_list[i].tong > thuKhoa.tong:
            thuKhoa = thisinh_list[i]
            stt = i
            
    print("So thu tu cua thu khoa:", stt)
    thuKhoa.xuat()