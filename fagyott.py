N = int(input)
H = []
for i in range(N):
    H.append(int(input))

NF = []
for i in range(N):
    if H[i] > 0:
        NF.append(i)

print(len(NF),end=" ")
for sorszam in NF:
    print(sorszam+1,end=" ")