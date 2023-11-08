import sys

print("Hany név jön?",file=sys.stderr)
N = int(input())
szulido = []
nev = []
for i in range(N):
    szulido.append(int(input().split(' ')[0]))
    #nev.append(str(input().split(' ')[1]))

print("A mai nap napokban: ", file=sys.stderr)
M = int(input())

i = 0
while i < N and (M-szulido[i]) <= 6574:
        i += 1
if i < N:
      print("VAN")
else:
      print("NINCS")
