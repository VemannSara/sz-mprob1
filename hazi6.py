import math
def Beolvasa():
    print("Kérem az adatokat")
    szamoklista = []
    for szam in input().split():
        szamoklista.append(int(szam))
    return szamoklista


# legkisebb osztó
def lko(N):
    i = 2
    while (i <= N) and (N % i != 0):
        i += 1
    van =(i <= N)
    if van:
        O = i
        return O
    else:
        return 1

# másolás
def masolas(szamoklista):
    oszto = []
    for i in range(len(szamoklista)):
        oszto.append(lko(szamoklista[i]))
    return oszto

# kiíráá
def Kiíras(oszto):
    for i in oszto:
        print(oszto[i], end=",")

szamoklista = Beolvasa()
oszto = masolas(szamoklista) 
Kiíras(oszto)