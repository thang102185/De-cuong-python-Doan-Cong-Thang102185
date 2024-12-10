import math
def line(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
a = line(x1, y1, x2, y2)
b = line(x1, y1, x3, y3)
c = line(x3, y3, x2, y2)

if a > 0 and b > 0 and c > 0:
    if (a + b) > c and (c + b) > a and (a + c) > b:
        cv = a + b + c
        p = cv/2
        s = math.sqrt(p * (p-a) * (p-b) * (p-c))
        print("Chu vi: {0:.2f}, Dien tich: {1:.2f}".format(cv, s))
    else:
        print("Khong phai là tam giac")
else:
    print("Khong phai là tam giac")