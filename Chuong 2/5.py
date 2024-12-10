#5.	Giải và biện luận hệ phương trình bậc nhất 2 ẩn
a1, b1, c1 = map(float, input().split())
a2, b2, c2 = map(float, input().split())
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
if D == 0 and (Dx != 0 or Dy != 0):
    print("VN")
elif D == Dx == Dy == 0:
    print("VSN")
elif D != 0:
    print("x = {0:.2f}; y = {1:.2f}".format(Dx / D, Dy / D))