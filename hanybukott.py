N = int(input("Hány db jegy legyen?"))
Jegy = []
for i in range(N):
    Jegy.append(int(input()))

s = 0
for i in range(N):
    if(Jegy[i] == 1):
        s += 1
print(s)