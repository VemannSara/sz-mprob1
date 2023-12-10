def beolvasas():
    N=int(input())
    adatok= []
    for i in range(N):
        sor=input().split()
        adatok.append((sor[0],int(sor[1])))
    return N,adatok

def szetvalogatas(N,adatok):
    evszakok=([],[],[],[])
    for adat in adatok:
        if adat[1]==12 or adat[1]<3:
            evszakok[3].append(adat[0])
        elif adat[1]>2 and adat[1]<=5:
            evszakok[0].append(adat[0])
        elif adat[1]>=6 and adat[1]<=8:
            evszakok[1].append(adat[0])
        else:
            evszakok[2].append(adat[0])
    return evszakok

N,adatok=beolvasas()
evszakok=szetvalogatas(N,adatok)

print(evszakok)