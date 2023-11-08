N = 3
idopont = []
összegek = []
mennyiség = []
for i in range(N):
    print(f"Az {i+1}. időpont:")
    idopont.append(str(input()))
    print(f"Az {i+1}. összeg:")
    összegek.append(int(input()))
    print(f"Az {i+1}. mennyiség:")
    mennyiség.append(int(input()))

#Eldöntés
i = 0
while i < N and összegek[i] > 10000:
    i = i + 1
if i >= N:
    print("Az összes rendelés 10000 Ft felett volt")
else:
    print("Nem mindegyik rendelés volt 10000 feletti")

#Megszámolás
Db = 0
for i in range(N):
    if(mennyiség[i]<20):
        Db += 1
print(Db)

#Maximum kiválasztás
MaxI = 0
for i in range(2,N):
    if (mennyiség[i] > mennyiség[MaxI]):
        MaxI = i
maxnap = idopont[MaxI]
print(f"A nap amikor a legtöbbet fogyasztotak: {maxnap}")


