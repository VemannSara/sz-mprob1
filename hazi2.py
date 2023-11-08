N = int(input("Adj meg egy számot 1 és 99 között!: "))
egyes = ["egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc", "kilenc"]
tizes = ["", "tizen", "huszon", "harminc", "negyven", "ötven", "hatvan", "hetven", "nyolcvan", "kilencven"]

if N == 10:
    S = "tíz"
elif N == 20:
    S = "húsz"
else:
    S = tizes[int((N / 10))] + egyes[int((N % 10)-1)]

print(S)