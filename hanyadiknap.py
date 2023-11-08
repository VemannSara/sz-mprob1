N = int(input("Adj meg egy napot: "))
H = int(input("Adj meg egy hónapot 1 és 12 között: "))
ho = [31,28,31,30,31,30,31,31,30,31,30,31]

s = N
for i in range(1,H):
    s = s + ho[i]

print(s)

