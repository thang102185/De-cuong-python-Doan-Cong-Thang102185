def chuyen_vi(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j], a[j][i] = a[j][i], a[i][j]

def main():
    n = int(input())
    
    a = []
    for _ in range(n):
        row = list(map(float, input().split()))
        a.append(row)

    chuyen_vi(a)

    print(n)
    for row in a:
        print(" ".join("{:.2f}".format(value)for value in row))

# if __name__ == "__main__":
main()