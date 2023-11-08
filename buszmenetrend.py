import sys
print("Hány adat lesz",file=sys.stderr)
N = int(input())
sorok = []
for i in range(N):
    print("Mi a " + str(i+1) + ". elem",file=sys.stderr)
    sorok.append(input())

i = 0
while i < N and sorok[i][0:12] != "Szekszard -1":
    i += 1
van = i < N
if van:
    print("VAN")
else:
    print("NINCS")