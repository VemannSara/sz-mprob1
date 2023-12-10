def beolvasas():
    N=int(input())
    adatok=[]
    for i in range(N):
        sor=input().split()
        adatok.append((sor[0],sor[1]))
    return N,adatok

def kivalogatas(N,adatok):
    allatevo=[]
    for i in range(N):
        for j  in range(N):
            if (adatok[i][1] == adatok[j][0]):
                allatevo.append(adatok[i][0])            
    return allatevo
def egyedi(allatevo):
    egyedilista=[]
    for allat in allatevo:
        if allat not in egyedilista:
            egyedilista.append(allat)
    return egyedilista

def kiiras(egyedilista):
    print(len(egyedilista),end="\n")
    for allat in egyedilista:
        print(allat,end="\n")

N,adatok=beolvasas()
allatevo=kivalogatas(N,adatok)
egyedilista=egyedi(allatevo)
kiiras(egyedilista)