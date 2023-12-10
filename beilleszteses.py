import time
import random

def generalveletlen(N):
    l=[]
    for i in range(N):
        l.append(int(random.random()*N))
    return l

def majdnemrendezett(N):
    l=[]
    for i in range(N):
        l.append(i)
    for i in range(10):
        cs=int(random.random()*N)
        cs2=int(random.random()*N)
        csere=l[cs]
        l[cs]=l[cs2]
        l[cs2]=csere
    return l

def javbeilleszteses(l):
    N=len(l)
    kezd=time.time()
    for i in range(1,N):
        s=l[i]
        j=i-1
        while j > 0 and l[j] > s:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=s
    vege=time.time()
    return vege-kezd,l

lista=generalveletlen(5000)
ido,l=javbeilleszteses(lista)
print(ido)
lista2=majdnemrendezett(5000)
ido,l=javbeilleszteses(lista2)
print(ido)
