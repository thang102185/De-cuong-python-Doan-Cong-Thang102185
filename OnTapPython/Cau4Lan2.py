def namnhuan(n):
    check = False
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        check = True
    
    return check

n = int(input())
nam = 2016
ds = []
while n > 0:
    nam += 4
    if namnhuan(nam):
        ds.append(nam)
        n -= 1
        
print(*ds)