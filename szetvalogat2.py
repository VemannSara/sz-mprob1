def beolvasas():
    N=int(input())
    adatok= []
    for i in range(N):
        sor=input().split()
        adatok.append((sor[0],int(sor[1])))
    return N,adatok

def szetvalogatas(N,adatok):
    tel=[]
    tavasz=[]
    nyar=[]
    osz=[]
    for adat in adatok:
        if adat[1]==12 or adat[1]<3:
            tel.append(adat[0])
        elif adat[1]>2 and adat[1]<=5:
            tavasz.append(adat[0])
        elif adat[1]>=6 and adat[1]<=8:
            nyar.append(adat[0])
        else:
            osz.append(adat[0])
    return tel,tavasz,nyar,osz

def kiiras(tel,tavasz,nyar,osz):
    print(tel)
    print(tavasz)
    print(nyar)
    print(osz)

N,adatok=beolvasas()
tel,tavasz,nyar,osz=szetvalogatas(N,adatok)
kiiras(tel,tavasz,nyar,osz)

