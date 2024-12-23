N, Q = map(int, input().split())
S = input().strip()

count = [[0] * 26 for _ in range(N + 1)]

for i in range(1, N + 1):
    char_index = ord(S[i-1]) - ord('a')
    for j in range(26):
        count[i][j] = count[i-1][j]
    count[i][char_index] += 1

kq = []
for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L), int(R)
    char_index = ord(C) - ord('a')
        
    result = count[R][char_index] - count[L-1][char_index]
    kq.append(result)

print("\n".join(map(str, kq)))
