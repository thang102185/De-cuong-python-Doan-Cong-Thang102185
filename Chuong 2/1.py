#1.	Giải và biện luận phương trình ax + b = 0
a , b = map(float, input().split())
if a == 0:
    if b == 0:
        print("VSN")
    else:
        print("VN")
else:
    print("x = {:.2f}".format(-b/a))