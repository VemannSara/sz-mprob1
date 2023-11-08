N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

s = 0
for i in range(N):
    s = s + M[i]

print(s)

