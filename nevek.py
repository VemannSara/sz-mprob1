import sys

def Beolvasas():
    print("Hany név jön?",file=sys.stderr)
    N=int(input())
    Nevek = []
    for i in range(N):
        print(str(i+1)+". nevet kérem", file=sys.stderr)
        Nevek.append(input())
    return N, Nevek    

def f(Nev,i):
    return str(i+1)+" "+ Nev

def Masolas(N,Nevek):
    Snevek=[]
    for i in range(N):
        Snevek.append(f(Nevek[i],i))
    return Snevek
    
def Kiiras(Snevek):
    for sor in Snevek:
        print(sor)

N,Nevek=Beolvasas()
Snevek=Masolas(N,Nevek)
Kiiras(Snevek)


