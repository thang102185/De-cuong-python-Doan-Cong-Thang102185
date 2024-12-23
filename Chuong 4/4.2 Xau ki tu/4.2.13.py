def nen(s):
    result = []
    n = len(s)

    if n == 0:
        return ""

    dem = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            result.append(s[i - 1] + str(dem))
            dem = 1
    result.append(s[-1] + str(dem))

    return ''.join(result)

T = int(input())
for _ in range(T):
    s = input().strip()
    print(nen(s))
