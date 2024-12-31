def ve(h):
    print(h)
    if h > 0:
        for i in range(1, h+1):
            for j in range(h-i):
                print(" ", end = '')
            for j in range(i*2-1):
                print("*", end = '')
            print()
    elif h < 0:
        h = -h
        for i in range(1, h+1):
            for j in range(i-1):
                print(" ", end = '')
            for j in range((h-i+1)*2-1):
                print("*", end = '')
            print()

x, y, z = map(int, input().split())
ve(x)
ve(y)
ve(z)