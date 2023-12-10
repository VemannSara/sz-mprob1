def beolvas():
    N=int(input())
    utak=[]
    for i in range(N):
        sor=input().split()
        utak.append((int(sor[0]),int(sor[1])))
    return N, utak
def megszamolas(N,utak):
    db=0
    for i in range(N):
        if (Egyedi(utak[i][1],utak)):
            db+=1
    return db

def Egyedi(ar,utak):
    db=0
    for i in range(len(utak)):
        if utak[i][1] == ar:
            db+=1
    return db==1

N,utak=beolvas()
db=megszamolas(N,utak)
print(db)

