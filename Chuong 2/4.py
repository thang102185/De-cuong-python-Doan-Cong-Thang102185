#4.	Giải và biện luận phương trình ax2 + bx + c = 0
import math
def ptBac1(a, b):
    if a == 0:
        if b == 0:
            print("VSN")
        else:
            print("VN")
    else:
        print("x = {:.2f}".format(-b / a))

a, b ,c = map(float, input().split())
if a != 0:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("VN")
    elif delta == 0:
        print("x1 = x2 = {:.2f}".format(-b / (2 * a)))
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("x1 = {0:.2f}, x2 = {1:.2f}".format(x1, x2))
else:
    ptBac1(b, c)