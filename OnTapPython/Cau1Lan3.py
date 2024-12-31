def strong(a):
    def snt(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in range(2, a + 1):
        if snt(i):
            if a % i == 0 and a % (i * i) == 0:
                return True
            
    return False

a = int(input())

if strong(a):
    print("true")
else:
    print("false")