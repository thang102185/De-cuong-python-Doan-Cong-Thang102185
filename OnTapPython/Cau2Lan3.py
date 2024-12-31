class HinhTron:
    def nhap(self):
        self.ma, self.x, self.y, self.bk = input().split()
        self.ma = int(self.ma)
        self.x = int(self.x)
        self.y = int(self.y)
        self.bk = float(self.bk)
        self.dientich = (self.bk ** 2) * 3.14159
        
    def xuat(self):
        print("{0} {1} {2} {3:.3f}".format(self.ma, self.x, self.y, self.bk))
        
n = int(input())
hinhtron_list = []
for i in range(n):
    hinhtron = HinhTron()
    hinhtron.nhap()
    hinhtron_list.append(hinhtron)
    
hinhtron_list.sort(key = lambda x : x.dientich, reverse = True)

print("Danh sach hinh tron da sap xep:", n)
for ht in hinhtron_list:
    ht.xuat()    