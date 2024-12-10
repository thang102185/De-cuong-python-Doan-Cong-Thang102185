#2.	Giải và biện luận bất phương trình ax + b > 0
a , b = map(float, input().split())
if a == 0:
    if b == 0:
        print("VN")
    elif b > 0:
        print("VSN")
    elif b < 0:
        print("VN")
elif a > 0:
    print("x > {:.2f}".format(-b/a))
else:
    print("x < {:.2f}".format(-b/a))