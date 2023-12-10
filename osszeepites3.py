def beolvasas():
    N=int(input())
    adatok=[]
    for i in range(N):
        v=input()
        l=int(input())
        r=int(input())
        adatok.append((v,l,r))
    return N,adatok

def kereses(N,adatok):
    i=0
    s=0
    while i<N and s<10000:
        s+=adatok[i][2]
        i+=1
    if i < N:
        van=i+1
    else:
        van=-1
    return van

N,adatok=beolvasas()
van=kereses(N,adatok)
print(van)




