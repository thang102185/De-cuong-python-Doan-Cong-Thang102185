import math
class HinhTron:
    def nhap(self):
        self.ma, self.x, self.y, self.bk = input().split()
        self.ma = int(self.ma)
        self.x = int(self.x)
        self.y = int(self.y)
        self.bk = float(self.bk)
        self.dientich = self.bk ** 2 * 3.14159
    
    def kc(self):
        return math.sqrt(self.x**2 + self.y**2)
    def xuat(self):
        print("{0} {1} {2} {3:.3f}".format(self.ma, self.x, self.y, self.bk))
    
n = int(input())
ht_list = []
for i in range(n):
    ht = HinhTron()
    ht.nhap()
    ht_list.append(ht)
    
ht_max = ht_list[0]
for i in range(n):
    if ht_list[i].kc() > ht_max.kc():
        ht_max = ht_list[i]
        
ht_max.xuat()