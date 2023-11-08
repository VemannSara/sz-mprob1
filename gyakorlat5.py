import sys

print("Normál kimenetre írás")
print("Hiba kimenetre írás, a bíró nem figyeli",file=sys.stderr)

print("egy",end=",")
print("kettő")

listam = input().split(",") # ha csak split() van akkor szóköz mentén
print(listam)
szamlista = []
for elem in input().split():
    szamlista.append(int(elem))
print(szamlista)

szamlista2=[int(elem) for elem in input().split()] #úgy kapom meg a listát h a beírt adat első eleme lesz az első elem, az elem az minfig az input következő eleme

