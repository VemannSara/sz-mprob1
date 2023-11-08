import sys
print("Kerem az adatok szamat szokozzel elvalasztva ",file=sys.stderr)
N,K = [int(sor) for sor in input().split()]
F=[]
for i in range(N):
    F.append(int(input()))

db = 0
Y=[]
for i in range(N):
    if(F[i]>K):
        db += 1
        Y.append(i)

print(db, end = " ")
for sorszam in Y:
    print(sorszam+1, end = " ")
