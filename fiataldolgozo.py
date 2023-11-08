import sys
print("Kerem az adatok szamat szokozzel elvalasztva? ",file=sys.stderr)
#darabolva = [int(sor) for sor in input().split()]
#N = darabolva[0]
#K = darabolva[1]
N,K = [int(sor) for sor in input().split()]
M=[]
for i in range(N):
    M.append(int(input().split()[1]))

db = 0
Y = []
for i in range(N):
    if(M[i] < K):
        Y.append(i)

print(len(Y),end=" ")
for sorszam in Y:
    print(sorszam+1,end=" ")


