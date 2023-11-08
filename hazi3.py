N = int(input())
H = []
for i in range(N):
    H.append(int(input()))

i = 0
while i < N and H[i] != 0:
    i += 1
van = i < N
if van:
    sorszam = i + 1
    print(sorszam)
else:
    print(-1)