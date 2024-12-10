import math
a, b, c = map(float, input().split())

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