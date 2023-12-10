import time
import random

"""kezd=time.time()
s=""
for i in range(10000):
    s+=str(i)
veg=time.time()

print(veg-kezd)
"""
"""l=[]
for i in range(50000):
    l.append(int(random.random()*1000//10))
print(l)"""

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

def egyszerucseres(l):
    n=len(l)
    kezd=time.time()
    for i in range(n-1):
        for j in range(i+1,n):
            if l[i] > l[j]:
                csere=l[i]
                l[i]=l[j]
                l[j]=csere
    vege=time.time()
    return vege-kezd,l
lista=generalveletlen(5000)
ido,l=egyszerucseres(lista)
print(ido)
lista2=majdnemrendezett(5000)
ido,l=egyszerucseres(lista2)
print(ido)

def minimumrendezes(l):
    n=len(l)   
    kezd=time.time()
    for i in range(n-1):
        minI=i
        for j in range(i+1,n):
            if l[minI] > l[j]:
                minI=j
        csere=l[i]
        l[i]=l[minI]
        l[minI]=csere
    vege=time.time()
    return vege-kezd,l

ido,l=minimumrendezes(lista)
print(ido)
ido,l=minimumrendezes(lista2)
print(ido)

def buborekos(l):
    n=len(l)   
    kezd=time.time()
    for i in range(2,n):
        for j in range(1,i-1):
            if l[j] > l[j+1]:
                csere=l[j]
                l[j]=l[j+1]
                l[j+1]=csere
    vege=time.time()
    return vege-kezd,l

ido,l=buborekos(lista)
print(ido)
ido,l=buborekos(lista2)
print(ido)



