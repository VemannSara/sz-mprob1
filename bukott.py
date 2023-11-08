N = int(input("Hány db jegy legyen?"))
Jegy = []
for i in range(N):
    Jegy.append(int(input()))

i = 0
while i<N and Jegy[i] != 1:
    i += 1
Bukott = i < N

if Bukott:
    print("Van")
else:
    print("Nincs")
