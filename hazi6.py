import math
print("Kérem az adatokat")
szamoklista = []
for szam in input().split():
    szamoklista.append(int(szam))


# legkisebb osztó
j = 2
for i in range (len(szamoklista)):
    N = szamoklista[i]
    j = 2
    while (i <= math.sqrt(N)) and N % j != 0:
        j = j + 1
    lko = j
van =(j <= math.sqrt(N))
if van:
    O = i
else:
    O = 1




