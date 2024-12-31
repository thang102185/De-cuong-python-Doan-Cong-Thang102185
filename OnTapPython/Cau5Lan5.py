import math
def check(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a+b > c and b+c > a and a+c > b:
            return True
        else:
            return False
    else:
        return False
    
a, b, c = map(float, input().split())
if check(a, b, c):
    cv = a + b + c
    p = cv / 2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print("Dien tich tam giac: {:.2f}".format(s))
    print("Chu vi tam giac: {:.2f}".format(cv))
else:
    print("DL Sai")