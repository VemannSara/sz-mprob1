def beolvasas():
    #adatok beolvasása egyszerre és egésszé alakítás
    N,M,K=[int(x) for x in input().split()]
    adatok=[]
    for i in range(N):
        adatok.append([int(x) for x in input().split()])
    return N,M,K,adatok

N,M,K,adatok=beolvasas()

def legmelegebb(N,M,K,adatok,atlag):
    maxi=0
    for i in range(N):
            if (atlag[maxi] < atlag[i]):
                maxi=i
    return maxi

def Atlaga(N,M,K,adatok):
    atlag=[]
    for i in range(N):
        s=0
        for j in range(M):  
            s=s+adatok[i][j]
        atlaga=s/M
        atlag.append(atlaga)
    return atlag

atlag=Atlaga(N,M,K,adatok)
maxi=legmelegebb(N,M,K,adatok,atlag)
print(maxi+1)
    
    


        
